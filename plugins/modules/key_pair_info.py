#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: key_pair_info
short_description: Gather Key Pair Information
description:
    - Gathers Information of Key Pairs.
version_added: 0.x.x
author: James Riach
options:
    id:
        description:
            - Specify Id of Key Pair.
        type: int
    name:
        description:
            - The name of the Key Pair.
        type: string
    regex_name:
        description:
            - Treat name as a Regular Expression.
        default: false
        type: bool
    has_private_key:
        description:
            - Filter Key Pairs with or without a stored Private Key.
        type: bool
'''

EXAMPLES = r'''
- name: Get Specific Key by Id
  morpheus.core.key_pair_info:
    id: 20

- name: Get Keys matching Regular Expression
  morpheus.core.key_pair_info:
    name: ^morpheus_.*$
    regex_name: true

- name: Get All Keys with Private Key
  morpheus.core.key_pair_info:
    has_private_key: true
'''

RETURN = r'''
key_pairs:
    description:
        - List of Key Pairs.
    sample:
        "key_pairs": [
            {
                "account_id": 1,
                "date_created": "2023-07-18T08:39:48Z",
                "fingerprint": null,
                "has_private_key": false,
                "id": 1,
                "last_updated": "2023-07-18T08:39:48Z",
                "name": "dev-ssh-key",
                "private_key_hash": null,
                "public_key": "ssh-rsa AAAAB3..."
            },
            {
                "account_id": 1,
                "date_created": "2023-07-18T08:39:48Z",
                "fingerprint": null,
                "has_private_key": false,
                "id": 2,
                "last_updated": "2023-07-18T08:39:48Z",
                "name": "test-ssh-key",
                "private_key_hash": null,
                "public_key": "ssh-rsa AAAAB3..."
            }
        ]
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


def run_module():
    argument_spec = {
        'id': {'type': 'int'},
        'name': {'type': 'str'},
        'regex_name': {'type': 'bool', 'default': 'false'},
        'has_private_key': {'type': 'bool'}
    }

    mutually_exclusive = [
        ('id', 'name'),
        ('id', 'regex_name'),
        ('id', 'has_private_key')
    ]

    result = {
        'changed': False,
        'key_pairs': []
    }

    module = AnsibleModule(
        argument_spec=argument_spec,
        mutually_exclusive=mutually_exclusive,
        supports_check_mode=True
    )

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    if module.params['id'] is not None:
        response = morpheus_api.get_key_pairs({'id': module.params['id']})
        result['key_pairs'] = [mf.dict_keys_to_snake_case(response)]
        module.exit_json(**result)

    api_params = module.params.copy()

    if module.params['regex_name']:
        api_params['name'] = None

    for k in ['regex_name', 'has_private_key']:
        del api_params[k]

    response = morpheus_api.get_key_pairs(api_params)

    if module.params['regex_name']:
        response = [kp for kp in response if re.match(module.params['name'], kp['name'])]

    if module.params['has_private_key'] is not None:
        response = [kp for kp in response if kp['hasPrivateKey'] is module.params['has_private_key']]

    result['key_pairs'] = [mf.dict_keys_to_snake_case(kp) for kp in response]

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
