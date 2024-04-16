#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: cloud_type_info
short_description: Return available Cloud types
description:
    - Returns the available Cloud Types.
version_added: 0.7.0
author: James Riach (@McGlovin1337)
options:
    code:
        description:
            - Filter Cloud Types by code.
        type: str
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
- name: Return all Cloud Types
  morpheus.core.cloud_type_info:

- name: Return Cloud Type by Type Code
  morpheus.core.cloud_type_info:
    code: vmware

- name: Return Full Info about Cloud Types
  morpheus.core.cloud_type_info:
    detail: full
'''

RETURN = r'''
cloud_types:
    description:
        - List of Cloud Type Info.
    type: list
    returned: always
    sample:
        "cloud_types": [
            {
                "cloud": "private",
                "code": "fusion",
                "enabled": true,
                "id": 38,
                "name": "VMware Fusion"
            },
            {
                "cloud": "private",
                "code": "vmware",
                "enabled": true,
                "id": 28,
                "name": "VMware vCenter"
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
        'enabled',
        'cloud'
    )
}


def run_module():
    argument_spec = {
        **info_module.COMMON_ARG_SPEC,
        **{
            'code': {'type': 'str'},
            'detail': {'type': 'str', 'choices': ['summary', 'full'], 'default': 'summary'}
        }
    }

    mutually_exclusive = info_module.COMMON_MUTUALLY_EXCLUSIVE + [
        ('id', 'code')
    ]

    result = {
        'changed': False,
        'cloud_types': []
    }

    module = AnsibleModule(
        argument_spec=argument_spec,
        mutually_exclusive=mutually_exclusive,
        supports_check_mode=True
    )

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    api_params = info_module.param_filter(module)

    response = morpheus_api.common_get(ApiPath.CLOUD_TYPES, api_params)

    response = info_module.response_filter(module, response, API_FILTER_KEYS)

    result['cloud_types'] = [mf.dict_keys_to_snake_case(response_item) for response_item in response]

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
