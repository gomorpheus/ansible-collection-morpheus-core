#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: ssl_certificate
short_description: Manage SSL Certificates
description:
    - Create, Update or Delete SSL Certificates.
version_added: 0.6.0
author: James Riach (@McGlovin1337)
options:
    state:
        description:
            - When O(state=present) create or update an SSL Certificate.
        default: present
        choices:
            - absent
            - present
        type: str
    id:
        description:
            - Specify the Id of a SSL Certificate to Update or Remove.
        type: int
    name:
        description:
            - Name of the SSL Certificate.
        type: str
    domain_name:
        description:
            - The Domain Name this SSL Certificate is responsible for.
        type: str
    wildcard:
        description:
            - Is this a wildcard certificate.
        type: bool
    certificate:
        description:
            - The SSL Certificate contents.
        type: str
    key:
        description:
            - The Private Key contents.
        type: str
extends_documentation_fragment:
    - action_common_attributes
attributes:
    check_mode:
        support: full
    diff_mode:
        support: full
    platform:
        platforms:
            - httpapi
'''

EXAMPLES = r'''
- name: Create SSL Certificate
  morpheus.core.ssl_certificate:
    state: present
    name: WebSvr SSL Cert
    domain_name: www.domain.tld
    wildcard: false
    certificate: "{{ q('ansible.builtin.file', '/path/to/cert.crt') }}"
    key: "{{ q('ansible.builtin.file', '/path/to/private_key.pem') }}"

- name: Remove SSL Certificate
  morpheus.core.ssl_certificate:
    state: absent
    name: WebSvr SSL Cert

- name: Change Name of SSL Certificate
  morpheus.core.ssl_certificate:
    id: 17
    name: New Name SSL Cert
'''

RETURN = r'''
certificate:
    description:
        - SSL Certificate Details.
    type: dict
    returned: always
    sample:
        "certificate": {
            "account_id": 0,
            "category": null,
            "cert_type": "server",
            "common_name": null,
            "description": null,
            "domain_name": "host.domain.tld",
            "enabled": true,
            "generated": false,
            "id": 82,
            "integration_id": null,
            "key_file_md5": "aaaa....",
            "name": "My Domain Cert",
            "self_signed": false,
            "type": {
                "code": "internal",
                "id": 1
            },
            "wildcard": false
        }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from functools import partial
try:
    import module_utils.morpheus_funcs as mf
    from module_utils.morpheusapi import ApiPath, MorpheusApi
except ModuleNotFoundError:
    import ansible_collections.morpheus.core.plugins.module_utils.morpheus_funcs as mf
    from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import ApiPath, MorpheusApi


MOCK_SSL_CERT = {
    "accountId": 0,
    "category": None,
    "certType": "server",
    "commonName": None,
    "description": None,
    "domainName": "host.domain.tld",
    "enabled": True,
    "generated": False,
    "id": 0,
    "integrationId": None,
    "keyFileMd5": "aaaa....",
    "name": "certificate name",
    "selfSigned": False,
    "type": {
        "code": "internal",
        "id": 1
    },
    "wildcard": False
}


def create_update_cert(module: AnsibleModule, morpheus_api: MorpheusApi) -> dict:
    cert = get_cert(module, morpheus_api)
    cert = mf.dict_keys_to_snake_case(cert)

    api_params = module_to_api_params(module.params)

    if 'id' in cert:
        api_params['id'] = cert['id']

    action = {
        0: partial(morpheus_api.common_create, path=ApiPath.SSL_CERTIFICATES_PATH, api_params=api_params),
        1: partial(morpheus_api.common_set, path=ApiPath.SSL_CERTIFICATES_PATH, item_id=api_params.pop('id'), api_params=api_params),
        2: partial(parse_check_mode, state=module.params['state'], api_params=api_params, existing_cert=cert)
    }.get('id' in cert if not module.check_mode else 2)

    action_result = action()

    action_result = mf.dict_keys_to_snake_case(action_result)

    changed, diff = mf.dict_diff(action_result, cert)

    result = {
        'changed': changed and 'id' in action_result,
        'certificate': action_result
    }

    if module._diff:
        diffs = []

        if result['changed']:
            if 'id' in cert:
                diffs.append({
                    'after_header': '{0} ({1})'.format(action_result['name'], action_result['id']),
                    'after': '\n'.join([d['after'] for d in diff]),
                    'before_header': '{0} ({1})'.format(cert['name'], cert['id']),
                    'before': '\n'.join([d['before'] for d in diff])
                })
            else:
                diffs.append({
                    'after_header': '{0} ({1})'.format(action_result['name'], action_result['id']),
                    'after': 'Create new SSL Certificate\n',
                    'before_header': 'Non-existent SSL Certificate',
                    'before': 'Non-existent SSL Certificate\n'
                })

        result['diff'] = diffs

    return result


def get_cert(module: AnsibleModule, morpheus_api: MorpheusApi) -> dict:
    api_params = module_to_api_params(module.params)

    cert = morpheus_api.common_get(ApiPath.SSL_CERTIFICATES_PATH, api_params)

    if isinstance(cert, list) and len(cert) > 1:
        module.fail_json(
            msg='More than one certificate matched'
        )

    if isinstance(cert, list):
        try:
            cert = cert[0]
        except IndexError:
            cert = {}

    return cert


def module_to_api_params(module_params: dict) -> dict:
    api_params = module_params.copy()

    del api_params['state']
    api_params['cert_file'] = api_params.pop('certificate')
    api_params['key_file'] = api_params.pop('key')

    return api_params


def parse_check_mode(state: str, api_params: dict = None, existing_cert: dict = None) -> dict:
    if state == 'absent':
        return {'success': True, 'msg': ''}

    updated_cert = existing_cert.copy()

    if 'id' not in updated_cert:
        updated_cert = MOCK_SSL_CERT

    api_params = mf.dict_keys_to_camel_case(api_params)

    for k, v in api_params.items():
        if k in updated_cert and v is not None:
            updated_cert[k] = v

    return updated_cert


def remove_cert(module: AnsibleModule, morpheus_api: MorpheusApi) -> dict:
    cert = get_cert(module, morpheus_api)
    cert = mf.dict_keys_to_snake_case(cert)

    if 'id' not in cert:
        module.fail_json(
            msg='No matching certificate found'
        )

    response = morpheus_api.common_delete(ApiPath.SSL_CERTIFICATES_PATH, cert['id']) if not module.check_mode \
        else parse_check_mode(state=module.params['state'])

    success, msg = mf.success_response(response)

    result = {
        'changed': success,
        'failed': not success,
        'msg': msg
    }

    if module._diff:
        diffs = []

        if result['changed']:
            diffs.append({
                'prepared': 'Remove SSL Certificate "{0}" ({1})'.format(cert['name'], cert['id'])
            })

        result['diff'] = diffs

    return result


def run_module():
    argument_spec = {
        'state': {'type': 'str', 'choices': ['absent', 'present'], 'default': 'present'},
        'id': {'type': 'int'},
        'name': {'type': 'str'},
        'domain_name': {'type': 'str'},
        'wildcard': {'type': 'bool'},
        'certificate': {'type': 'str'},
        'key': {'type': 'str', 'no_log': True}
    }

    result = {
        'changed': False,
        'certificate': {}
    }

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True
    )

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    action = {
        'absent': remove_cert,
        'present': create_update_cert
    }.get(module.params['state'])

    action_result = action(
        module=module,
        morpheus_api=morpheus_api
    )

    result.update(action_result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
