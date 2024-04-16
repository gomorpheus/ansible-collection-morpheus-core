#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: tenant_info
short_description: Retrieves Tenant Info
description:
    - Returns information about Morpheus Tenants.
version_added: 0.7.0
author: James Riach (@McGlovin1337)
options:
    account_name:
        description:
            - Filter tenants by account name.
        type: str
    account_number:
        description:
            - Filter tenants by account number.
        type: str
    customer_number:
        description:
            - Filter tenants by customer number.
        type: str
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
- name: Get Info for a Specific Tenant by id
  morpheus.core.tenant_info:
    id: 50

- name: Get Tenants Matching Regex Name
  morpheus.core.tenant_info:
    name: ^tenant.*$
    regex_name: true

- name: Get Tenant with Matching Customer Number
  morpheus.core.tenant_info:
    customer_number: T3ST
'''

RETURN = r'''
tenants:
    description:
        - List of matching tenants.
    type: list
    returned: always
    sample:
        "tenants": [
            {
                "account_name": null,
                "account_number": null,
                "active": true,
                "currency": "GBP",
                "customer_number": "T3ST",
                "date_created": "2022-01-01T0:00:01Z",
                "description": null,
                "external_id": null,
                "id": 10,
                "last_updated": "2022-01-01T0:00:01Z",
                "master": true,
                "name": "TestTenant",
                "role": {
                    "authority": "Tenant Base Role",
                    "description": null,
                    "id": 5,
                    "name": "Tenant Base Role"
                },
                "stats": {
                    "instance_count": 5,
                    "user_count": 10
                },
                "subdomain": "test"
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
        'tenants': []
    }

    argument_spec = {
        **info_module.COMMON_ARG_SPEC,
        **{
            'account_name': {'type': 'str'},
            'account_number': {'type': 'str'},
            'customer_number': {'type': 'str'}
        }
    }

    mutually_exclusive = info_module.COMMON_MUTUALLY_EXCLUSIVE + [
        ('id', 'account_name'),
        ('id', 'account_number'),
        ('id', 'customer_number')
    ]

    module = AnsibleModule(
        argument_spec=argument_spec,
        mutually_exclusive=mutually_exclusive,
        supports_check_mode=True
    )

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    api_params = info_module.param_filter(module, ['account_name', 'account_number', 'customer_number'])

    response = morpheus_api.common_get(ApiPath.TENANTS_PATH, api_params)

    response = info_module.response_filter(module, response)

    if module.params['account_name'] is not None:
        response = [response_item for response_item in response if response_item['accountName'] == module.params['account_name']]

    if module.params['account_number'] is not None:
        response = [response_item for response_item in response if response_item['accountNumber'] == module.params['account_number']]

    if module.params['customer_number'] is not None:
        response = [response_item for response_item in response if response_item['customerNumber'] == module.params['customer_number']]

    result['tenants'] = [mf.dict_keys_to_snake_case(response_item) for response_item in response]

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
