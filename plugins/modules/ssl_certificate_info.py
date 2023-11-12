#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: ssl_certificate_info
short_description: Gather information about SSL Certificates
description:
    - Gathers information about SSL Certificates.
version_added: 0.6.0
author: James Riach
options:
    id:
        description:
            - The Id of a specific SSL Certificate.
        type: int
    name:
        description:
            - The name of the SSL Certificate.
        type: string
    regex_name:
        description:
            - Treat the name parameter as a Regular Expression.
        default: false
        type: bool
'''

EXAMPLES = r'''
- name: Get All SSL Certificates
  morpheus.core.ssl_certificate_info:

- name: Get Specific Certificate by Id
  morpheus.core.ssl_certificate_info:
    id: 20

- name: Get Certificates matching Regular Expression
  morpheus.core.ssl_certificate_info:
    name: ^Web.*$
    regex_name: true
'''

RETURN = r'''
certificates:
    description:
        - List of SSL Certificates.
    returned: always
    sample:
        "certificates": [
            {
                "account_id": 1,
                "category": null,
                "cert_type": "server",
                "common_name": null,
                "description": "Dev Web Server",
                "domain_name": "dev.domain.tld",
                "enabled": true,
                "generated": false,
                "id": 73,
                "integration_id": null,
                "key_file_md5": "0000....",
                "name": "Dev Web Server",
                "self_signed": false,
                "type": {
                    "code": "internal",
                    "id": 1
                },
                "wildcard": false
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
        'regex_name': {'type': 'bool', 'default': 'false'}
    }

    mutually_exclusive = [
        ('id', 'name'),
        ('id', 'regex_name')
    ]

    result = {
        'changed': False,
        'certificates': []
    }

    module = AnsibleModule(
        argument_spec=argument_spec,
        mutually_exclusive=mutually_exclusive,
        supports_check_mode=True
    )

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    if module.params['id'] is not None:
        response = morpheus_api.get_ssl_certificates({'id': module.params['id']})
        result['certificates'] = [mf.dict_keys_to_snake_case(response)]
        module.exit_json(**result)

    api_params = module.params.copy()

    if module.params['regex_name']:
        api_params['name'] = None

    del api_params['regex_name']

    response = morpheus_api.get_ssl_certificates(api_params)

    if module.params['regex_name']:
        response = [cert for cert in response if re.match(module.params['name'], cert['name'])]

    result['certificates'] = [mf.dict_keys_to_snake_case(cert) for cert in response]

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
