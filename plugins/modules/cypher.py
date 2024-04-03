#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: cypher
short_description: Manage items stored in Cypher
description:
    - Create and Delete items stored in Cypher.
version_added: 0.x.x
author: James Riach
options:
    state:
        description:
            - State of the stored item.
        type: string
        choices:
            - absent
            - present
        default: present
    cypher_path:
        description:
            - Specify a full Cypher mount and key path.
        type: string
    mount:
        description:
            - Specify the Cypher mount point.
            - Mutually exclusive with O(cypher_path).
        type: string
        choices:
            - key
            - password
            - secret
            - tfvars
            - uuid
    name:
        description:
            - Specify the Key Name.
            - Required when O(mount) is specified.
            - Mutually exclusive with O(cypher_path).
        type: string
    length:
        description:
            - Required if O(mount) is either V(key) or V(password)
            - For O(mount=key) specify the bit length for the generated key.
            - For O(mount=password) specify the character length for the generated password.
            - Mutually exclusive with O(cypher_path).
        type: int
    value:
        description:
            - Specify the data to be stored when O(mount) is either V(secret) or V(tfvars).
            - Required when O(mount) is either V(secret) or V(tfvars).
        type: string
    ttl:
        description:
            - Specify the lease duration either in seconds or human readable format, e.g 15m, 8h, 7d.
        type: string
        default: '0'
        aliases:
            - lease_duration
            - duration
extends_documentation_fragment:
    - action_common_attributes
attributes:
    check_mode:
        support: none
    diff_mode:
        support: none
'''

EXAMPLES = r'''
- name: Generate a 7 Character Password
  morpheus.core.cypher:
    state: present
    cypher_path: password/7/my_password

- name: Generate a 1024bit Key
  morpheus.core.cypher:
    state: present
    mount: key
    name: my_key
    length: 1024

- name: Add a Secret with a 7 day Lease
  morpheus.core.cypher:
    state: present
    mount: secret
    name: my_secret
    value: 5uper5ecret
    ttl: 7d

- name: Remove a UUID item
  morpheus.core.cypher:
    state: absent
    cypher_path: uuid/my_uuid
'''

RETURN = r'''
cypher:
    description:
        - Details of the Cypher item.
    returned: always
    sample:
        "cypher": {
            "created_by": "130",
            "data": "rf[TVB>1VNQpW5!%b{Sj=I60o!`q.V%jXk\Aga^0&B_/p/w>Q08~+0[ze_fhyfQrx)",
            "date_created": null,
            "expire_date": null,
            "id": 165,
            "item_key": "password/64/my_pass",
            "last_accessed": "2024-01-01T00:00:01Z",
            "last_updated": "2024-01-01T00:00:01Z",
            "lease_duration": null,
            "lease_timeout": 0,
            "success": true,
            "type": "string"
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


def create_cypher(module: AnsibleModule, morpheus_api: MorpheusApi) -> dict:
    api_params = module_to_api_params(module.params)
    path_ext = api_params.pop('cypher_path')

    if api_params['ttl'] is not None:
        path_ext = '{0}?ttl={1}'.format(path_ext, api_params.pop('ttl'))

    response = morpheus_api.common_create(ApiPath.CYPHER_PATH, api_params, path_ext, True)

    response = mf.dict_keys_to_snake_case(response)

    if 'cypher' in response:
        for k in response['cypher']:
            response[k] = response['cypher'][k]
        del response['cypher']

    return {
        'changed': 'id' in response,
        'cypher': response
    }


def module_to_api_params(module_params: dict) -> dict:
    api_params = module_params.copy()

    if api_params['cypher_path'] is None:
        api_params['cypher_path'] = '{0}/{1}/{2}'.format(api_params.pop('mount'), api_params.pop('length'), api_params.pop('name')) \
            if api_params['length'] is not None else '{0}/{1}'.format(api_params.pop('mount'), api_params.pop('name'))

    for k in ['state', 'mount', 'name', 'length']:
        if k in api_params:
            del api_params[k]

    if api_params['ttl'].isnumeric():
        api_params['ttl'] = int(api_params['ttl'])

    return api_params


def remove_cypher(module: AnsibleModule, morpheus_api: MorpheusApi) -> dict:
    api_params = module_to_api_params(module.params)

    response = morpheus_api.common_delete(ApiPath.CYPHER_PATH, api_params['cypher_path'])

    success, msg = mf.success_response(response)

    return {
        'changed': success,
        'failed': not success,
        'msg': msg
    }


def run_module():
    argument_spec = {
        'state': {'type': 'str', 'choices': ['absent', 'present'], 'default': 'present'},
        'cypher_path': {'type': 'str'},
        'mount': {'type': 'str', 'choices': ['key', 'password', 'secret', 'tfvars', 'uuid']},
        'name': {'type': 'str'},
        'length': {'type': 'str'},
        'value': {'type': 'str', 'no_log': True},
        'ttl': {'type': 'str', 'default': '0', 'aliases': ['lease_duration', 'duration']}
    }

    mutually_exclusive = [
        ('cypher_path', 'mount'),
        ('cypher_path', 'name'),
        ('cypher_path', 'length')
    ]

    required_one_of = [
        ('cypher_path', 'mount')
    ]

    required_together = [
        ('mount', 'name')
    ]

    required_if = [
        ('mount', 'key', ('length',)),
        ('mount', 'password', ('length',))
    ]

    result = {
        'changed': False,
        'cypher': {}
    }

    module = AnsibleModule(
        argument_spec=argument_spec,
        mutually_exclusive=mutually_exclusive,
        required_one_of=required_one_of,
        required_together=required_together,
        required_if=required_if,
        supports_check_mode=False
    )

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    action = {
        'absent': remove_cypher,
        'present': create_cypher
    }.get(module.params['state'])

    response = action(module, morpheus_api)

    result.update(response)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
