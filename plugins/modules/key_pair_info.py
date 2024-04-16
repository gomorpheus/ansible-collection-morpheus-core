#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: key_pair_info
short_description: Gather Key Pair Information
description:
    - Gathers Information of Key Pairs.
version_added: 0.6.0
author: James Riach (@McGlovin1337)
options:
    has_private_key:
        description:
            - Filter Key Pairs with or without a stored Private Key.
        type: bool
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
    type: list
    returned: always
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
            'has_private_key': {'type': 'bool'}
        }
    }

    mutually_exclusive = info_module.COMMON_MUTUALLY_EXCLUSIVE + [
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
        response = morpheus_api.common_get(ApiPath.KEY_PAIR_PATH, {'id': module.params['id']})
        result['key_pairs'] = [mf.dict_keys_to_snake_case(response)]
        module.exit_json(**result)

    api_params = info_module.param_filter(module, ['has_private_key'])

    response = morpheus_api.common_get(ApiPath.KEY_PAIR_PATH, api_params)

    response = info_module.response_filter(module, response)

    if module.params['has_private_key'] is not None:
        response = [kp for kp in response if kp['hasPrivateKey'] is module.params['has_private_key']]

    result['key_pairs'] = [mf.dict_keys_to_snake_case(kp) for kp in response]

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
