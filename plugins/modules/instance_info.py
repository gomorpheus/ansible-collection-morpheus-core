#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: instance_info
short_description: Gather information about instances
description:
    - Gathers information about Morpheus instances
version_added: 0.4.0
author: James Riach
options:
    id:
        description:
            - Specify the id of an instance.
        type: int
    name:
        description:
            - Filter instances by name.
        type: string
    regex_name:
        description:
            - Treat the name parameter as a regular expression.
        default: false
        type: bool
    detail:
        description:
            - Specify the level of detail returned for matching instances.
        default: minimal
        choices:
            - minimal
            - full
            - extra
            - summary
        type: string
    instance_type:
        description:
            - Filter by the instance type code.
        type: string
    agent_installed:
        description:
            - Filter by if agent is installed or not.
        type: bool
    status:
        description:
            - Filter by instance status, e.g. running
        type: string
    environment:
        description:
            - Filter instances by environment.
        type: string
    deleted:
        description:
            - Include, Exclude or Only show deleted instances or those pending removal.
        choices:
            - exclude
            - include
            - only
        default: exclude
        type: string
    labels:
        description:
            - Filter instances by matching labels.
        type: list
        elements: string
    match_all_labels:
        description:
            - If labels have been specified, filter instances by those that match all specified labels.
        default: false
        type: bool
    tags:
        description:
            - Filter instances by matching tags.
        type: list
        elements: string
'''

EXAMPLES = r'''
- name: Get Info for a Specific Instance by id
  morpheus.core.instance_info:
    id: 200

- name: Get a short summary of instances
  morpheus.core.instance_info:
    detail: summary

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

import re
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import MorpheusApi, dict_filter, dict_keys_to_snake_case


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
        'id': {'type': 'int'},
        'name': {'type': 'str'},
        'regex_name': {'type': 'bool', 'default': 'false'},
        'detail': {'type': 'str', 'choices': ['minimal', 'full', 'extra', 'summary'], 'default': 'basic'},
        'instance_type': {'type': 'str'},
        'agent_installed': {'type': 'bool'},
        'status': {'type': 'str'},
        'environment': {'type': 'str'},
        'deleted': {'type': 'str', 'choices': ['exclude', 'include', 'only'], 'default': 'exclude'},
        'labels': {'type': 'list', 'elements': 'str'},
        'match_all_labels': {'type': 'bool', 'default': 'false'},
        'tags': {'type': 'str'}
    }

    mutually_exclusive = [
        ('id', 'name'),
        ('id', 'regex_name'),
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

    api_params = module.params
    if module.params['regex_name']:
        api_params['name'] = None
    api_params['details'] = 'extra' in module.params['detail']
    api_params['show_deleted'] = 'include' in module.params['deleted']
    api_params['deleted'] = 'only' in module.params['deleted']
    api_params['all_labels'] = api_params.pop('labels') if module.params['match_all_labels'] else None

    for k in ['detail', 'match_all_labels', 'regex_name']:
        del api_params[k]

    response = morpheus_api.get_instances(api_params)

    if not isinstance(response, list):
        response = [response]

    if module.params['name'] is not None and module.params['regex_name']:
        response = [inst for inst in response if re.match(module.params['name'], inst['name'])]

    if module.params['detail'] in ['minimal', 'summary']:
        filter_keys = API_FILTER_KEYS[module.params['detail']]

        filtered_info = [dict_filter(instance, list(filter_keys)) for instance in response]

        result['morpheus_instances'] = [dict_keys_to_snake_case(simple_item) for simple_item in filtered_info]
        module.exit_json(**result)

    result['morpheus_instances'] = [dict_keys_to_snake_case(response_item) for response_item in response]

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
