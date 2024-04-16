#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: group_info
short_description: Retrieves Group Info
description:
    - Retrieves information about Groups.
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
- name: Get Info for a Specific Group by id
  morpheus.core.group_info:
    id: 5

- name: Get Groups Matching Regex Pattern
  morpheus.core.group_info:
    name: ^linux.*$
    regex_name: true

- name: Get Full Info for all Groups
  morpheus.core.group_info:
    detail: full
'''

RETURN = r'''
groups:
    description:
        - List of groups information.
    type: list
    returned: always
    sample:
        "groups": [
            {
                "account_id": 1,
                "active": true,
                "code": "linuxClouds",
                "config": {
                    "config_cmdb_discovery": false,
                    "service_registry_id": ""
                },
                "date_created": "2024-01-01T00:00:01Z",
                "id": 5,
                "last_updated": "2024-01-01T00:00:01Z",
                "location": null,
                "name": "Linux Cloud Group",
                "server_count": 9,
                "stats": {
                    "instance_counts": {
                        "all": 2
                    },
                    "server_counts": {
                        "all": 9,
                        "baremetal": 0,
                        "container_host": 0,
                        "host": 9,
                        "hypervisor": 9,
                        "unmanaged": 0,
                        "vm": 3
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
        'active',
        'accountId',
        'serverCount'
    )
}


def run_module():
    argument_spec = {
        **info_module.COMMON_ARG_SPEC,
        **{
            'detail': {'type': 'str', 'choices': ['full', 'summary'], 'default': 'summary'}
        }
    }

    result = {
        'changed': False,
        'groups': []
    }

    module = AnsibleModule(
        argument_spec=argument_spec,
        mutually_exclusive=info_module.COMMON_MUTUALLY_EXCLUSIVE,
        supports_check_mode=True
    )

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    api_params = info_module.param_filter(module)

    response = morpheus_api.common_get(ApiPath.GROUPS_PATH, api_params)

    response = info_module.response_filter(module, response, API_FILTER_KEYS)

    result['groups'] = [mf.dict_keys_to_snake_case(response_item) for response_item in response]

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
