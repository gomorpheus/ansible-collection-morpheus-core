#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: cypher_info
short_description: Return Cypher Information
description:
    - Returns items stored in Cypher.
version_added: 0.7.0
author: James Riach (@McGlovin1337)
options:
    cypher_path:
        description:
            - Filter Cypher items by path.
        type: str
    regex_match:
        description:
            - Specify to treat O(cypher_path) as regex.
        type: bool
        default: false
    decrypt:
        description:
            - Specify to decrypt matching Cypher items.
            - Requires O(cypher_path) to be specified, cannot be used to decrypt all items when no parameters are specified.
        type: bool
extends_documentation_fragment:
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
- name: List all items in Cypher
  morpheus.core.cypher_info:

- name: List items matching regex pattern
  morpheus.core.cypher_info:
    cypher_path: ^.*vcenter.*$
    regex_match: true

- name: Return a specific item and decrypt
  morpheus.core.cypher_info:
    cypher_path: secret/my_secret
    decrypt: true

- name: List items matching pattern and decrypt
  morpheus.core.cypher_info:
    cypher_path: ^password/.*/my_pass$
    regex_match: true
    decrypt: true
'''

RETURN = r'''
cyphers:
    description:
        - List of items stored in Cypher.
    type: list
    returned: always
    sample:
        "cyphers": [
            {
                "created_by": "15",
                "date_created": "2024-01-01T00:00:01Z",
                "expire_date": null,
                "id": 99,
                "item_key": "secret/netbox_token",
                "last_accessed": "2024-03-28T15:36:38Z",
                "last_updated": "2024-01-01T00:00:01Z",
                "lease_timeout": 0
            },
            {
                "created_by": "1",
                "date_created": null,
                "expire_date": null,
                "id": 100,
                "item_key": "secret/redhat8templatepass",
                "last_accessed": "2024-01-01T00:00:01Z",
                "last_updated": "2024-01-01T00:00:01Z",
                "lease_timeout": 0
            }
        ]
'''

import re
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
try:
    import module_utils.morpheus_funcs as mf
    from module_utils.morpheusapi import ApiPath, MorpheusApi
except ModuleNotFoundError:
    import ansible_collections.morpheus.core.plugins.module_utils.morpheus_funcs as mf
    from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import ApiPath, MorpheusApi


def module_to_api_params(module_params: dict) -> dict:
    """Convert Module Parameters to API Parameters.

    Args:
        module_params (dict): Ansible Module Parameters

    Returns:
        dict: Dictionary of API Parameters
    """
    api_params = module_params.copy()

    api_params['key'] = api_params.pop('cypher_path') if not api_params['regex_match'] else None

    for k in ['regex_match', 'decrypt', 'cypher_path']:
        if k in api_params:
            del api_params[k]

    return api_params


def run_module():
    argument_spec = {
        'cypher_path': {'type': 'str'},
        'regex_match': {'type': 'bool', 'default': 'false'},
        'decrypt': {'type': 'bool'}
    }

    required_by = {
        'decrypt': 'cypher_path'
    }

    result = {
        'changed': False,
        'cyphers': []
    }

    module = AnsibleModule(
        argument_spec=argument_spec,
        required_by=required_by,
        supports_check_mode=True
    )

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    api_params = module_to_api_params(module.params)

    response = morpheus_api.common_get(ApiPath.CYPHER_PATH, api_params)

    if module.params['regex_match']:
        response = [
            response_item for response_item in response
            if re.match(module.params['cypher_path'], response_item['itemKey'])
        ]

    if module.params['decrypt']:
        response = [
            morpheus_api.common_get(ApiPath.CYPHER_PATH, {}, response_item['itemKey'])
            for response_item in response
        ]

    for response_item in response:
        if 'cypher' in response_item:
            for k in response_item['cypher']:
                response_item[k] = response_item['cypher'][k]
            del response_item['cypher']

    result['cyphers'] = [mf.dict_keys_to_snake_case(response_item) for response_item in response]

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
