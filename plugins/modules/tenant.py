#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: tenant
short_description: Manage Tenants
description:
    - Create, Update and Remove Tenants.
version_added: 0.7.0
author: James Riach (@McGlovin1337)
options:
    state:
        description:
            - The state of the Tenant.
        type: str
        choices:
            - absent
            - present
        default: present
    id:
        description:
            - The Id of an existing Tenant.
        type: int
    name:
        description:
            - The name of the Tenant.
        type: str
    description:
        description:
            - Description for the Tenant.
        type: str
    account_name:
        description:
            - Additional Tenant Identifier.
        type: str
    account_number:
        description:
            - Additional Tenant Identifier.
        type: str
    customer_number:
        description:
            - Additional Tenant Identifier.
        type: str
    role:
        description:
            - Id of a Role to act as the Tenant base role.
        type: int
    subdomain:
        description:
            - Subdomain name used in login URL and subtenant users.
        type: str
extends_documentation_fragment:
    - action_common_attributes
    - morpheus.core.currency_option
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
- name: Create / Update Tenant
  morpheus.core.tenant:
    name: Test Tenant
    description: Testing Tenant
    role: 4
    subdomain: test
    currency: GBP

- name: Remove Tenant
  morpheus.core.tenant:
    state: absent
    name: Test Tenant
'''

RETURN = r'''
tenant:
    description:
        - Details of the Tenant state.
    type: dict
    returned: always
    sample:
        "tenant": {
            "account_name": null,
            "account_number": null,
            "active": true,
            "currency": "GBP",
            "customer_number": null,
            "date_created": "2024-01-01T00:00:01Z",
            "description": "Testing Tenant",
            "external_id": null,
            "id": 30,
            "last_updated": "2024-01-01T00:00:01Z",
            "master": false,
            "name": "Test Tenant",
            "role": {
                "authority": "Customer Base Role",
                "description": null,
                "id": 4,
                "name": "Customer Base Role"
            },
            "stats": {
                "instance_count": 0,
                "user_count": 0
            },
            "subdomain": "test"
        }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from functools import partial
try:
    import module_utils.morpheus_funcs as mf
    from module_utils.morpheus_const import CURRENCY_OPTIONS
    from module_utils.morpheusapi import ApiPath, MorpheusApi
except ModuleNotFoundError:
    import ansible_collections.morpheus.core.plugins.module_utils.morpheus_funcs as mf
    from ansible_collections.morpheus.core.plugins.module_utils.morpheus_const import CURRENCY_OPTIONS
    from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import ApiPath, MorpheusApi


MOCK_TENANT = {
    "account_name": None,
    "account_number": None,
    "active": True,
    "currency": "GBP",
    "customer_number": "TST001",
    "date_created": "2024-01-01T00:00:01Z",
    "description": None,
    "external_id": None,
    "id": 10,
    "last_updated": "2024-01-01T00:00:01Z",
    "master": False,
    "name": "TST001 - Test Tenant 001",
    "role": {
        "authority": "Customer Base Role",
        "description": None,
        "id": 4,
        "name": "Customer Base Role"
    },
    "stats": {
        "instance_count": 0,
        "user_count": 2
    },
    "subdomain": "test"
}


def create_update_tenant(module: AnsibleModule, morpheus_api: MorpheusApi, existing_tenant: dict = None) -> dict:
    """Create a new Tenant or Update an existing one.

    Args:
        module (AnsibleModule): An instantiated AnsibleModule Class
        morpheus_api (MorpheusApi): An instantiated MorpheusApi Class
        existing_tenant (dict, optional): A dictionary of an existing Tenant. Defaults to None.

    Returns:
        dict: Result Dictionary
    """
    if module.params['role'] is not None:
        if not validate_role(module.params['role'], morpheus_api):
            module.fail_json(
                msg='Invalid role specified'
            )

    if 'id' not in existing_tenant and module.params['role'] is None:
        module.fail_json(
            msg='role parameter required when creating a new Tenant'
        )

    api_params = module_to_api_params(module.params)

    if 'id' in existing_tenant and api_params['id'] is None:
        api_params['id'] = existing_tenant['id']

    action = {
        'False': partial(morpheus_api.common_create, path=ApiPath.TENANTS_PATH, api_params=api_params),
        'True': partial(morpheus_api.common_set, path=ApiPath.TENANTS_PATH, item_id=api_params.pop('id'), api_params=api_params),
        'Check': partial(parse_check_mode, api_params=api_params, state=module.params['state'], existing_tenant=existing_tenant)
    }.get(str('id' in existing_tenant) if not module.check_mode else 'Check')

    action_result = action()
    action_result = mf.dict_keys_to_snake_case(action_result)

    changed, diff = mf.dict_diff(action_result, existing_tenant, {'last_updated', 'server_count', 'stats'})
    result = {
        'changed': changed and 'id' in action_result,
        'tenant': action_result
    }

    if module._diff:
        diffs = []

        if result['changed']:
            if 'id' in existing_tenant:
                diffs.append({
                    'after_header': '{0} ({1})'.format(action_result['name'], action_result['id']),
                    'after': '\n'.join([d['after'] for d in diff]),
                    'before_header': '{0} ({1})'.format(existing_tenant['name'], existing_tenant['id']),
                    'before': '\n'.join([d['before'] for d in diff])
                })
            else:
                diffs.append({
                    'after_header': '{0} ({1})'.format(action_result['name'], action_result['id']),
                    'after': 'Create new Tenant\n',
                    'before_header': 'Non-existent Tenant',
                    'before': 'Non-existent Tenant\n'
                })

        result['diff'] = diffs

    return result


def get_existing_tenant(module: AnsibleModule, morpheus_api: MorpheusApi) -> dict:
    """Return details of an existing Tenant if it exists, based on module parameters.

    Args:
        module (AnsibleModule): An instantiated AnsibleModule Class
        morpheus_api (MorpheusApi): An instantiated MorpheusApi Class

    Returns:
        dict: Dictionary details of existing Tenant
    """
    existing_tenant = morpheus_api.common_get(
        ApiPath.TENANTS_PATH,
        {
            'id': module.params['id'],
            'name': module.params['name']
        }
    )

    if isinstance(existing_tenant, list):
        if len(existing_tenant) > 1:
            module.fail_json(
                msg='Number of matching tenants exceeded 1, got {0}'.format(len(existing_tenant))
            )
        existing_tenant = existing_tenant[0] if len(existing_tenant) == 1 else {}

    return mf.dict_keys_to_snake_case(existing_tenant)


def module_to_api_params(module_params: dict):
    """Convert Module Parameters to API Parameters.

    Args:
        module_params (dict): Ansible Module Parameters

    Returns:
        dict: Dictionary of API Parameters
    """
    api_params = module_params.copy()

    del api_params['state']

    api_params['role'] = {'id': api_params.pop('role')}

    return api_params


def parse_check_mode(state: str, api_params: dict, existing_tenant: dict):
    """Returns a predicted result when the module is run in check mode.

    Args:
        state (str): The value of the module state parameter
        api_params (dict): API Parameters
        existing_tenant (dict): Details of an existing tenant if it exists

    Returns:
        dict: Predicted result
    """
    if state == 'absent':
        return {'success': True, 'msg': ''}

    updated_tenant = existing_tenant.copy() if len(existing_tenant) > 0 else MOCK_TENANT

    if 'id' not in existing_tenant:
        existing_tenant = MOCK_TENANT

    for k, v in api_params.items():
        if k in existing_tenant and k != 'role' and v is not None:
            updated_tenant[k] = v

    if api_params['role']['id'] is not None:
        updated_tenant['role']['id'] = api_params['role']['id']

    return updated_tenant


def remove_tenant(module: AnsibleModule, morpheus_api: MorpheusApi, existing_tenant: dict) -> dict:
    """Remove an existing Tenant.

    Args:
        module (AnsibleModule): An instantiated AnsibleModule Class
        morpheus_api (MorpheusApi): An instantiated MorpheusApi Class
        existing_tenant (dict): Dictionary details of an existing tenant

    Returns:
        dict: Result Dictionary
    """
    if 'id' not in existing_tenant:
        module.fail_json(
            msg='Specified Tenant not found'
        )

    action = {
        'False': partial(morpheus_api.common_delete, path=ApiPath.TENANTS_PATH, item_id=existing_tenant['id']),
        'True': partial(parse_check_mode, state=module.params['state'], api_params={}, existing_tenant=existing_tenant)
    }.get(str(module.check_mode))

    response = action()

    success, msg = mf.success_response(response)

    result = {
        'changed': success,
        'failed': not success,
        'msg': msg
    }

    if module._diff and not result['failed']:
        result['diff'] = {
            'prepared': 'Delete Tenant with Id {0}'.format(existing_tenant['id'])
        }

    return result


def validate_role(role_id: int, morpheus_api: MorpheusApi) -> bool:
    """Validate if the given role_id is a tenant role.

    Args:
        role_id (int): The Id of the role.
        morpheus_api (MorpheusApi): An instantiated MorpheusApi Class.

    Returns:
        bool: True if role is valid, otherwise False.
    """
    role = morpheus_api.common_get(
        ApiPath.ROLES_PATH,
        {'id': role_id}
    )

    role = mf.dict_keys_to_snake_case(role)

    if 'role_type' not in role or role['role_type'] != 'account':
        return False

    return True


def run_module():
    argument_spec = {
        'state': {'type': 'str', 'choices': ['absent', 'present'], 'default': 'present'},
        'id': {'type': 'int'},
        'name': {'type': 'str'},
        'description': {'type': 'str'},
        'account_name': {'type': 'str'},
        'account_number': {'type': 'str'},
        'customer_number': {'type': 'str'},
        'role': {'type': 'int'},
        'subdomain': {'type': 'str'},
        'currency': {'type': 'str', 'choices': CURRENCY_OPTIONS}
    }

    result = {
        'changed': False,
        'tenant': {}
    }

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True
    )

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    existing_tenant = get_existing_tenant(module, morpheus_api)

    action = {
        'absent': remove_tenant,
        'present': create_update_tenant
    }.get(module.params['state'])

    action_result = action(
        module=module,
        morpheus_api=morpheus_api,
        existing_tenant=existing_tenant
    )

    result.update(action_result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
