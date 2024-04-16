#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: role_info
short_description: Retrieves Role Information
description:
    - Retrieves list of Morpheus Roles.
version_added: 0.7.0
author: James Riach (@McGlovin1337)
options:
    diverged:
        description:
            - Filter roles that have diverged.
        type: bool
    multitenant:
        description:
            - Filter Multi-Tenant Roles.
        type: bool
    role_type:
        description:
            - Filter by Type of Role.
            - V(account) and V(tenant) are the same.
        choices:
            - account
            - tenant
            - user
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
- name: Get all Roles
  morpheus.core.role_info:

- name: Get Role by specific Id
  morpheus.core.role_info:
    id: 120

- name: Get all Account/Tenant Roles
  morpheus.core.role_info:
    role_type: tenant

- name: Get all multitenant Roles
  morpheus.core.role_info:
    multitenant: true
'''

RETURN = r'''
roles:
    description:
        - List of matching roles.
    type: list
    returned: always
    sample:
        "roles": [
            {
                "authority": "Support",
                "date_created": "2022-01-01T00:00:01Z",
                "default_persona": null,
                "description": "Support Role",
                "diverged": false,
                "id": 10,
                "last_updated": "2022-01-01T00:00:01Z",
                "multitenant": true,
                "multitenant_locked": true,
                "name": "Support",
                "owner": {
                    "id": 1,
                    "name": "Owner"
                },
                "owner_id": 1,
                "parent_role_id": null,
                "role_type": "user",
                "scope": "Account"
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


def run_module():
    argument_spec = {
        **info_module.COMMON_ARG_SPEC,
        **{
            'diverged': {'type': 'bool'},
            'multitenant': {'type': 'bool'},
            'role_type': {'type': 'str', 'choices': ['account', 'tenant', 'user']}
        }
    }

    mutually_exclusive = info_module.COMMON_MUTUALLY_EXCLUSIVE + [
        ('id', 'multitenant'),
        ('id', 'role_type')
    ]

    result = {
        'changed': False,
        'roles': []
    }

    module = AnsibleModule(
        argument_spec=argument_spec,
        mutually_exclusive=mutually_exclusive,
        supports_check_mode=True
    )

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    api_params = info_module.param_filter(module, ['diverged', 'multitenant'])
    if module.params['role_type'] == 'tenant':
        api_params['role_type'] = 'account'

    response = morpheus_api.common_get(ApiPath.ROLES_PATH, api_params)

    response = info_module.response_filter(module, response)

    if module.params['diverged'] is not None:
        response = [response_item for response_item in response if response_item['diverged'] is module.params['diverged']]

    if module.params['multitenant'] is not None:
        response = [response_item for response_item in response if response_item['multitenant'] is module.params['multitenant']]

    result['roles'] = [mf.dict_keys_to_snake_case(response_item) for response_item in response]

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
