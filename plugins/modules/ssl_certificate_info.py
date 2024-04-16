#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: ssl_certificate_info
short_description: Gather information about SSL Certificates
description:
    - Gathers information about SSL Certificates.
version_added: 0.6.0
author: James Riach (@McGlovin1337)
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
    type: list
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
    result = {
        'changed': False,
        'certificates': []
    }

    module = AnsibleModule(
        argument_spec=info_module.COMMON_ARG_SPEC,
        mutually_exclusive=info_module.COMMON_MUTUALLY_EXCLUSIVE,
        supports_check_mode=True
    )

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    if module.params['id'] is not None:
        response = morpheus_api.common_get(ApiPath.SSL_CERTIFICATES_PATH, {'id': module.params['id']})
        result['certificates'] = [mf.dict_keys_to_snake_case(response)]
        module.exit_json(**result)

    api_params = info_module.param_filter(module)

    response = morpheus_api.common_get(ApiPath.SSL_CERTIFICATES_PATH, api_params)

    response = info_module.response_filter(module, response)

    result['certificates'] = [mf.dict_keys_to_snake_case(cert) for cert in response]

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
