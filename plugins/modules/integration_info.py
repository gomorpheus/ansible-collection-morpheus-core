#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: integration_info
short_description: Retrieves Integration Info
description:
    - Retrieves information about Integrations.
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
- name: Get Info for a Specific Integration by id
  morpheus.core.integration_info:
    id: 3

- name: Get Integrations Matching Regex Pattern
  morpheus.core.integration_info:
    name: ^.*ansible.*$
    regex_name: true

- name: Get Full Info for all Integrations
  morpheus.core.integration_info:
    detail: full
'''

RETURN = r'''
integrations:
    description:
        - List of integrations.
    type: list
    returned: always
    sample:
        "integrations": [
            {
                "enabled": true,
                "id": 3,
                "name": "Bitbucket",
                "status": "ok",
                "type": "git"
            },
            {
                "enabled": true,
                "id": 4,
                "name": "Morpheus-Ansible",
                "status": "ok",
                "type": "ansible"
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
    'summary': (
        'id',
        'name',
        'code',
        'enabled',
        'type',
        'status'
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
        'integrations': []
    }

    module = AnsibleModule(
        argument_spec=argument_spec,
        mutually_exclusive=info_module.COMMON_MUTUALLY_EXCLUSIVE,
        supports_check_mode=True
    )

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    api_params = info_module.param_filter(module)

    response = morpheus_api.get_integrations(api_params)

    response = info_module.response_filter(module, response, API_FILTER_KEYS)

    result['integrations'] = [mf.dict_keys_to_snake_case(response_item) for response_item in response]

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
