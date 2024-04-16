#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: cloud_info
short_description: Retrieves Cloud Info
description:
    - Retrieves information about Morpheus Clouds.
version_added: 0.7.0
author: James Riach (@McGlovin1337)
options:
    detail:
        description:
            - Level of detail returned.
        default: summary
        choices:
            - summary
            - full
        type: str
    type:
        description:
            - Filter Clouds by Cloud Type Code.
        type: str
extends_documentation_fragment:
    - morpheus.core.generic_name_filter
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
- name: Return all Clouds
  morpheus.core.cloud_info:

- name: Return all VMware Clouds
  morpheus.core.cloud_info:
    type: vmware

- name: Return Cloud matching Name
  morpheus.core.cloud_info:
    name: ProdCloud

- name: Return all Clouds matching Regex Name
  morpheus.core.cloud_info:
    name: ^Dev.*$
    regex_name: true

- name: Return Clouds with Full Detailed Info
  morpheus.core.cloud_info:
    detail: full
'''

RETURN = r'''
clouds:
    description:
        - List of Clouds with Info.
    type: list
    returned: always
    sample:
        "clouds": [
            {
                "agent_mode": "cloudInit",
                "code": "linuxCloud",
                "enabled": true,
                "id": 20,
                "location": "UKSouth",
                "name": "Linux Cloud South",
                "server_count": 3,
                "stats": {
                    "server_counts": {
                        "all": 3,
                        "baremetal": 0,
                        "container_host": 0,
                        "host": 3,
                        "hypervisor": 3,
                        "unmanaged": 0,
                        "vm": 0
                    }
                }
            }
        ]
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
try:
    import module_utils.info_module_common as info_module
    import module_utils.morpheus_funcs as mf
    from module_utils.morpheusapi import ApiPath, MorpheusApi
except ModuleNotFoundError:
    import ansible_collections.morpheus.core.plugins.module_utils.info_module_common as info_module
    import ansible_collections.morpheus.core.plugins.module_utils.morpheus_funcs as mf
    from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import ApiPath, MorpheusApi


API_FILTER_KEYS = {
    'summary': (
        'id',
        'name',
        'code',
        'location',
        'visibility',
        'enabled',
        'status',
        'zoneType',
        'agentMode',
        'stats',
        'serverCount'
    )
}


def run_module():
    argument_spec = {
        **info_module.COMMON_ARG_SPEC,
        **{
            'detail': {'type': 'str', 'choices': ['full', 'summary'], 'default': 'summary'},
            'type': {'type': 'str'}
        }
    }

    mutually_exclusive = info_module.COMMON_MUTUALLY_EXCLUSIVE + [
        ('id', 'type')
    ]

    result = {
        'changed': False,
        'clouds': []
    }

    module = AnsibleModule(
        argument_spec=argument_spec,
        mutually_exclusive=mutually_exclusive,
        supports_check_mode=True
    )

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    api_params = info_module.param_filter(module)

    response = morpheus_api.common_get(ApiPath.CLOUDS, api_params)

    response = info_module.response_filter(module, response, API_FILTER_KEYS)

    result['clouds'] = [mf.dict_keys_to_snake_case(response_item) for response_item in response]

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
