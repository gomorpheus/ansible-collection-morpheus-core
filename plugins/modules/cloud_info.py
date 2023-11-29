#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: cloud_info
short_description: Retrieves Cloud Info
description:
    - Retrieves information about Morpheus Clouds.
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
    type:
        description:
            - Filter Clouds by Cloud Type Code.
        type: string
extends_documentation_fragment:
    - morpheus.core.generic_name_filter
'''

EXAMPLES = r'''
'''

RETURN = r'''
'''

import re
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
try:
    import module_utils.morpheus_funcs as mf
    from module_utils.morpheusapi import MorpheusApi
except ModuleNotFoundError:
    import ansible_collections.morpheus.core.plugins.module_utils.morpheus_funcs as mf
    from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import MorpheusApi


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
        'id': {'type': 'int'},
        'name': {'type': 'str'},
        'regex_name': {'type': 'bool', 'default': 'false'},
        'detail': {'type': 'str', 'choices': ['full', 'summary'], 'default': 'summary'},
        'type': {'type': 'str'}
    }

    mutually_exclusive = [
        ('id', 'name'),
        ('id', 'regex_name'),
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

    api_params = module.params.copy()
    for param in ['detail', 'regex_name']:
        del api_params[param]

    if module.params['regex_name']:
        api_params['name'] = None

    response = morpheus_api.get_clouds(api_params)

    if not isinstance(response, list):
        response = [response]

    if module.params['name'] is not None and module.params['regex_name']:
        response = [response_item for response_item in response if re.match(module.params['name'], response_item['name'])]

    if module.params['detail'] in API_FILTER_KEYS:
        response = [mf.dict_filter(response_item, API_FILTER_KEYS[module.params['detail']]) for response_item in response]

    result['clouds'] = [mf.dict_keys_to_snake_case(response_item) for response_item in response]

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
