#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: instance_info
short_description: Gather information about instances
description:
    - Gathers information about Morpheus instances
version_added: 0.4.0
author: James Riach (@McGlovin1337)
options:
    detail:
        description:
            - Specify the level of detail returned for matching instances.
        default: minimal
        choices:
            - minimal
            - full
            - extra
            - summary
        type: str
    instance_type:
        description:
            - Filter by the instance type code.
        type: str
    agent_installed:
        description:
            - Filter by if agent is installed or not.
        type: bool
    status:
        description:
            - Filter by instance status, e.g. running
        type: str
    deleted:
        description:
            - Include, Exclude or Only show deleted instances or those pending removal.
        choices:
            - exclude
            - include
            - only
        default: exclude
        type: str
extends_documentation_fragment:
    - morpheus.core.instance_filter_base
    - morpheus.core.instance_filter_extended
    - action_common_attributes
attributes:
    check_mode:
        support: N/A
        details: Not Required, Module does not make changes.
    diff_mode:
        support: N/A
    platform:
        platforms:
            - httpapi
'''

EXAMPLES = r'''
- name: Get Info for a Specific Instance by id
  morpheus.core.instance_info:
    id: 200

- name: Get a short summary of instances
  morpheus.core.instance_info:
    detail: summary

- name: Get Info for instance by name
  morpheus.core.instance_info:
    name: WebServer001

- name: Get Info for instances where name matches regular expression
  morpheus.core.instance_info:
    name: ^WebServer.*$
    regex_name: true

- name: Get Extra Info for a Specific Instance by id
  morpheus.core.instance_info:
    id: 200
    detail: extra

- name: Get Info for all Instances with any of the specified labels
  morpheus.core.instance_info:
    labels:
      - foo
      - bar
      - prod

- name: Get Info of all Running Instances
  morpheus.core.instance_info:
    status: running
'''

RETURN = r'''
morpheus_instances:
    description:
        - List of instances with info
    type: list
    returned: always
    sample:
        "morpheus_instances": [
            {
                "cloud": {
                    "id": 31,
                    "name": "VMWare Cloud",
                    "type": "vmware"
                },
                "connection_info": [
                    {
                        "ip": "192.168.0.10",
                        "name": null,
                        "port": null
                    }
                ],
                "date_created": "2023-06-01T13:37:00Z",
                "description": "Webserver Instance",
                "id": 100,
                "instance_type": {
                    "code": "win2019",
                    "id": 110,
                    "name": "Windows Server 2019"
                },
                "instance_version": "2019",
                "interfaces": [
                    {
                        "id": "network-100",
                        "ip_address": null,
                        "ip_mode": null,
                        "network": {
                            "dhcp_server": false,
                            "group": null,
                            "id": 150,
                            "name": "inside-network-001",
                            "pool": {
                                "id": 30,
                                "name": "inside-network-pool-001"
                            },
                            "subnet": null
                        },
                        "network_interface_type_id": null
                    }
                ],
                "labels": [
                    "production",
                    "webservers"
                ],
                "name": "WebServ001",
                "owner": {
                    "username": "patrick.clifton@domain.tld"
                },
                "plan": {
                    "name": "Cheap Plan 001"
                },
                "stats": {
                    "cpu_usage": 0,
                    "cpu_usage_avg": 0,
                    "cpu_usage_peak": 0.0,
                    "max_memory": 4293943296,
                    "max_storage": 53687091200,
                    "used_cpu": 0.0,
                    "used_memory": 2080228608,
                    "used_storage": 25341928960
                },
                "status": "running",
                "volumes": [
                    {
                        "name": "root",
                        "resizeable": true,
                        "root_volume": true,
                        "size": 50
                    }
                ]
            }
        ]
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
try:
    import module_utils.info_module_common as info_module
    import module_utils.morpheus_funcs as mf
    from module_utils.morpheusapi import MorpheusApi
except ModuleNotFoundError:
    import ansible_collections.morpheus.core.plugins.module_utils.info_module_common as info_module
    import ansible_collections.morpheus.core.plugins.module_utils.morpheus_funcs as mf
    from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import MorpheusApi


API_FILTER_KEYS = {
    'minimal': (
        'id',
        'name',
        'description',
        'cloud',
        'connectionInfo',
        'dateCreated',
        ('owner', ['username']),
        ('instanceType', ['id', 'code', 'name']),
        'instanceVersion',
        'labels',
        ('plan', ['name']),
        'interfaces',
        'stats',
        'status',
        ('volumes', ['name', 'rootVolume', 'resizeable', 'size'])
    ),
    'summary': (
        'id',
        'name',
        ('connectionInfo', ['ip']),
        'status'
    )
}


def run_module():
    argument_spec = {
        **info_module.COMMON_ARG_SPEC,
        **{
            'detail': {'type': 'str', 'choices': ['minimal', 'full', 'extra', 'summary'], 'default': 'minimal'},
            'instance_type': {'type': 'str'},
            'agent_installed': {'type': 'bool'},
            'status': {'type': 'str'},
            'environment': {'type': 'str'},
            'deleted': {'type': 'str', 'choices': ['exclude', 'include', 'only'], 'default': 'exclude'},
            'labels': {'type': 'list', 'elements': 'str'},
            'match_all_labels': {'type': 'bool', 'default': 'false'},
            'tags': {'type': 'list', 'elements': 'str'}
        }
    }

    mutually_exclusive = info_module.COMMON_MUTUALLY_EXCLUSIVE + [
        ('id', 'instance_type'),
        ('id', 'agent_installed'),
        ('id', 'status'),
        ('id', 'environment'),
        ('id', 'deleted'),
        ('id', 'labels'),
        ('id', 'match_all_labels'),
        ('id', 'tags')
    ]

    result = {
        'changed': False,
        'morpheus_instances': []
    }

    module = AnsibleModule(
        argument_spec=argument_spec,
        mutually_exclusive=mutually_exclusive,
        supports_check_mode=True
    )

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    api_params = info_module.param_filter(module)
    api_params['details'] = 'extra' in module.params['detail']
    api_params['show_deleted'] = 'include' in module.params['deleted']
    api_params['deleted'] = 'only' in module.params['deleted']
    api_params['all_labels'] = api_params.pop('labels') if module.params['match_all_labels'] else None

    response = morpheus_api.get_instances(api_params)

    response = info_module.response_filter(module, response, API_FILTER_KEYS)

    result['morpheus_instances'] = [mf.dict_keys_to_snake_case(response_item) for response_item in response]

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
