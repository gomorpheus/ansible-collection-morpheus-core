#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: key_pair
short_description: Create and Remove Key Pairs
description:
    - Create and Remove Key Pairs.
    - Keys can be user provided or generated.
version_added: 0.6.0
author: James Riach (@McGlovin1337)
options:
    state:
        description:
            - Create or Remove a Key Pair.
        default: present
        choices:
            - absent
            - present
        type: str
    id:
        description:
            - Required when O(state=absent), specify the Key Pair to remove.
        type: int
    name:
        description:
            - Required when O(state=present), specify the name of the Key Pair.
            - Specifying this parameter alone will generate a Key Pair.
        type: str
    private_key:
        description:
            - Specify the Private Key.
        type: str
    public_key:
        description:
            - Specify the Public Key.
        type: str
    passphrase:
        description:
            - Specify the Private Key passphrase.
        type: str
extends_documentation_fragment:
    - action_common_attributes
attributes:
    check_mode:
        support: none
    diff_mode:
        support: full
    platform:
        platforms:
            - httpapi
'''

EXAMPLES = r'''
- name: Generate a Key Pair
  morpheus.core.key_pair:
    state: present
    name: My Generated Key Pair

- name: Add a Key Pair
  morpheus.core.key_pair:
    state: present
    name: My Existing Key Pair
    private_key: "{{ q('ansible.builtin.file', 'path/to/private_key')[0] }}"
    public_key: "{{ q('ansible.builtin.file', 'path/to/public_key')[0] }}"
    passphrase: Password123

- name: Delete a Key Pair
  morpheus.core.key_pair:
    state: absent
    id: 50
'''

RETURN = r'''
key_pair:
    description:
        - Dictionary information about the Key Pair.
        - If this was a Generated Key Pair, it will include details of the Private Key.
    type: dict
    returned: always
    sample:
        "key_pair": {
            "account_id": 1,
            "date_created": "2023-10-23T11:56:56Z",
            "fingerprint": "0f:f7:4c:5a:71:60:47:11:56:bb:1b:1f:ff:b4:70:cb",
            "has_private_key": false,
            "id": 50,
            "last_updated": "2023-10-23T11:56:56Z",
            "name": "Ansible Created Key Pair",
            "private_key_hash": null,
            "public_key": "ssh-rsa AAAAB3N..."
        }

errors:
    description:
        - Any errors when generating or adding a Key Pair.
    type: dict
    returned: always
    sample:
        "errors" : {
            "private_key": "Unable to generate public key from private key"
        }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
try:
    import module_utils.morpheus_funcs as mf
    from module_utils.morpheusapi import ApiPath, MorpheusApi
except ModuleNotFoundError:
    import ansible_collections.morpheus.core.plugins.module_utils.morpheus_funcs as mf
    from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import ApiPath, MorpheusApi


def create_key_pair(module: AnsibleModule, morpheus_api: MorpheusApi) -> dict:
    """Create or Generate Key Pair from Module Parameters

    Args:
        module (AnsibleModule): Instance of AnsibleModule
        morpheus_api (MorpheusApi): Instance of MorpheusApi

    Returns:
        dict: Result Dictionary
    """
    api_params = module.params.copy()
    del api_params['state']
    del api_params['id']

    response = morpheus_api.create_key_pair(api_params)
    response = mf.dict_keys_to_snake_case(response)
    key_pair = response['key_pair']

    if 'private_key' in key_pair:
        key_pair['private_key_lines'] = list(key_pair['private_key'].split('\n'))

    try:
        changed = key_pair['id'] is not None
    except KeyError:
        changed = False

    try:
        err = response['errors']
    except KeyError:
        err = {}

    result = {
        'changed': changed,
        'errors': err,
        'failed': len(err) > 0,
        'key_pair': key_pair
    }

    if module._diff and not result['failed']:
        result['diff'] = {
            'prepared': 'Create Key Pair "{0}"'.format(key_pair['name'])
        }

    return result


def remove_key_pair(module: AnsibleModule, morpheus_api: MorpheusApi) -> dict:
    """Delete a Key Pair by specified Module Parameters

    Args:
        module (AnsibleModule): Instance of AnsibleModule
        morpheus_api (MorpheusApi): Instance of MorpheusApi

    Returns:
        dict: Result Dictionary
    """
    response = morpheus_api.common_delete(ApiPath.KEY_PAIR_PATH, module.params['id'])

    success, msg = mf.success_response(response)

    result = {
        'changed': success,
        'failed': not success,
        'msg': msg
    }

    if module._diff and not result['failed']:
        result['diff'] = {
            'prepared': 'Delete Key Pair with Id {0}'.format(module.params['id'])
        }

    return result


def run_module():
    argument_spec = {
        'state': {'type': 'str', 'choices': ['absent', 'present'], 'default': 'present'},
        'id': {'type': 'int'},
        'name': {'type': 'str'},
        'private_key': {'type': 'str', 'no_log': True},
        'public_key': {'type': 'str'},
        'passphrase': {'type': 'str', 'no_log': True}
    }

    mutually_exclusive = [
        ('id', 'name'),
        ('id', 'private_key'),
        ('id', 'public_key'),
        ('id', 'passphrase')
    ]

    required_by = {
        'passphrase': 'private_key'
    }

    required_if = [
        ('state', 'absent', ('id',)),
        ('state', 'present', ('name',))
    ]

    result = {
        'changed': False,
        'key_pair': {}
    }

    module = AnsibleModule(
        argument_spec=argument_spec,
        mutually_exclusive=mutually_exclusive,
        required_by=required_by,
        required_if=required_if,
        supports_check_mode=False
    )

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    action = {
        'absent': remove_key_pair,
        'present': create_key_pair
    }.get(module.params['state'])

    action_result = action(module=module, morpheus_api=morpheus_api)

    result.update(action_result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
