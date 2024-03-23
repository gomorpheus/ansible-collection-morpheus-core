#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: group_info
short_description: Retrieves Group Info
description:
    - Retrieves information about Groups.
version_added: 0.x.x
author: James Riach
options:
    detail:
        description:
            - Level of detail returned.
        default: summary
        choices:
            - summary
            - full
        type: string
extends_documentation_fragment:
    - morpheus.core.generic_name_filter
'''

EXAMPLES = r'''
'''

RETURN = r'''
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

    response = morpheus_api.get_groups(api_params)

    response = info_module.response_filter(module, response, API_FILTER_KEYS)

    result['groups'] = [mf.dict_keys_to_snake_case(response_item) for response_item in response]

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
