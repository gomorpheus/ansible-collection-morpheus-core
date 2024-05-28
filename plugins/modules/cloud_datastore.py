#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: cloud_datastore
short_description: Configure Cloud Datastores
description:
    - Update the configuration of Cloud Datastores.
version_added: 0.7.0
author: James Riach (@McGlovin1337)
options:
    id:
        description:
            - The Id of the Datastore.
        type: int
        required: true
    zone_id:
        description:
            - The Id of the Cloud the Datastore belongs to.
        type: int
        required: true
        aliases:
            - cloud_id
    state:
        description:
            - The active state of the Datastore.
        choices:
            - active
            - inactive
        type: str
    visibility:
        description:
            - The visibility of the Datastore.
        choices:
            - private
            - public
        type: str
    tenant_permissions:
        description:
            - List of Tenant Permissions on the Datastore.
        type: list
        elements: dict
        suboptions:
            state:
                description:
                    - If the Account should have access or not.
                choices:
                    - absent
                    - present
                default: present
                type: str
            tenant_id:
                description:
                    - The id of the tenant to add or remove permissions for.
                type: int
                required: true
            default_target:
                description:
                    - Set the Datastore as the default for the specified tenant.
                type: bool
            default_store:
                description:
                    - Set the Datastore as the default image store for the specified tenant.
                type: bool
    resource_permissions:
        description:
            - Resource permissions for the Datastore.
        type: dict
        suboptions:
            all_groups:
                description:
                    - Allow or disallow access to all groups.
                type: bool
            groups:
                description:
                    - List of groups that are allowed access to the Datastore.
                type: list
                elements: dict
                suboptions:
                    state:
                        description:
                            - If the Group should have access or not.
                        choices:
                            - absent
                            - present
                        default: present
                        type: str
                    group_id:
                        description:
                            - Id of the group to allow access.
                        type: int
                        aliases:
                            - site_id
                aliases:
                    - sites
            all_plans:
                description:
                    - Allow access to all plans.
                type: bool
            plans:
                description:
                    - List of Plans to allow access.
                type: list
                elements: dict
                suboptions:
                    state:
                        description:
                            - If the plan should be present or not.
                        choices:
                            - absent
                            - present
                        default: present
                        type: str
                    plan_id:
                        description:
                            - Id of the Plan to allow access.
                        type: int
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
- name: Set a Datastore to Active and Public Visibility
  morpheus.core.cloud_datastore:
    id: 30
    cloud_id: 5
    state: active
    visibility: public

- name: Configure Tenant Access to Datastore
  morpheus.core.cloud_datastore:
    id: 30
    cloud_id: 5
    tenant_permissions:
        - state: present
          tenant_id: 50
          default_target: true
        - state: present
          tenant_id: 51
          default_target: true
          default_store: true
        - state: absent
          tenant_id: 2

- name: Configure Group Access and Allow all Price Plans
  morpheus.core.cloud_datastore:
    id: 35
    cloud_id: 6
    resource_permissions:
        groups:
            - state: present
              group_id: 7
        all_plans: true
'''

RETURN = r'''
datastore:
    description:
        - Information about the datastore after changes.
    type: dict
    returned: always
    sample:
        "datastore": {
            "active": true,
            "free_space": 17589585575936,
            "id": 100,
            "name": "vmfs01",
            "online": true,
            "resource_permission": {
                "all": true,
                "all_plans": false,
                "plans": [],
                "sites": []
            },
            "tenants": [
                {
                    "default_store": false,
                    "default_target": false,
                    "id": 1,
                    "name": "MasterTenant"
                }
            ],
            "type": "vmfs",
            "visibility": "private",
            "zone": {
                "id": 20,
                "name": "VMware Cloud"
            }
        }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from functools import partial
try:
    import module_utils.morpheus_funcs as mf
    from module_utils.morpheusapi import MorpheusApi
except ModuleNotFoundError:
    import ansible_collections.morpheus.core.plugins.module_utils.morpheus_funcs as mf
    from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import MorpheusApi


def parse_check_mode(current_state: dict, api_params: dict) -> dict:
    params = mf.dict_keys_to_camel_case(api_params)

    for k in params:
        if k not in ['cloudId', 'id', 'zoneId', 'tenantPermissions', 'resourcePermissions'] and params[k] is not None:
            current_state[k] = params[k]

    return current_state


def parse_resource_permissions(permissions: dict, params: dict) -> dict:
    """Parse existing resource permissions with any changes specified in params

    Args:
        permissions (dict): Existing permissions
        params (dict): Module Parameters specifying changes

    Returns:
        dict: API Formatted Dictionary
    """
    resource_sites = [site['id'] for site in permissions['sites']]
    resource_plans = [plan['id'] for plan in permissions['plans']]

    if params['groups'] is not None:
        for site in params['groups']:
            if site['state'] == 'present' and site['group_id'] not in resource_sites:
                resource_sites.append(site['group_id'])
                continue

            if site['state'] == 'absent' and site['group_id'] in resource_sites:
                resource_sites.remove(site['group_id'])

    if params['plans'] is not None:
        for plan in params['plans']:
            if plan['state'] == 'present' and plan['plan_id'] not in resource_plans:
                resource_plans.append(plan['plan_id'])
                continue

            if plan['state'] == 'absent' and plan['plan_id'] in resource_plans:
                resource_plans.remove(plan['plan_id'])

    return {
        'all': params['all_groups'],
        'sites': [{'id': v} for v in resource_sites],
        'all_plans': params['all_plans'],
        'plans': [{'id': v} for v in resource_plans]
    }


def parse_tenant_permissions(tenants: list, params: dict) -> dict:
    """Parse existing Tenant Permisions with any changes specified in params.

    Args:
        tenants (list): List of existing Tenant permissions
        params (dict): Module Parameters specifying chaanges

    Returns:
        dict: API Formatted Dictionary
    """
    tenant_access = [t['id'] for t in tenants]
    tenant_store = [t['id'] for t in tenants if t['defaultStore']]
    tenant_target = [t['id'] for t in tenants if t['defaultTarget']]

    if params is not None:
        for tenant_permission in params:
            if tenant_permission['state'] == 'present':
                tenant_access.append(tenant_permission['tenant_id'])

                if tenant_permission['default_store'] is not None:
                    if tenant_permission['default_store'] and tenant_permission['tenant_id'] not in tenant_store:
                        tenant_store.append(tenant_permission['tenant_id'])
                    elif not tenant_permission['default_store'] and tenant_permission['tenant_id'] in tenant_store:
                        tenant_store.remove(tenant_permission['tenant_id'])

                if tenant_permission['default_target'] is not None:
                    if tenant_permission['default_target'] and tenant_permission['tenant_id'] not in tenant_target:
                        tenant_target.append(tenant_permission['tenant_id'])
                    elif not tenant_permission['default_target'] and tenant_permission['tenant_id'] in tenant_target:
                        tenant_target.remove(tenant_permission['tenant_id'])
                continue

            if tenant_permission['state'] == 'absent':
                if tenant_permission['tenant_id'] in tenant_access:
                    tenant_access.remove(tenant_permission['tenant_id'])

                if tenant_permission['tenant_id'] in tenant_store:
                    tenant_store.remove(tenant_permission['tenant_id'])

                if tenant_permission['tenant_id'] in tenant_target:
                    tenant_target.remove(tenant_permission['tenant_id'])

    return {
        'accounts': tenant_access,
        'default_target': tenant_target,
        'default_store': tenant_store
    }


def run_module():
    argument_spec = {
        'id': {'type': 'int', 'required': True},
        'zone_id': {'type': 'int', 'required': True, 'aliases': ['cloud_id']},
        'state': {'type': 'str', 'choices': ['active', 'inactive']},
        'visibility': {'type': 'str', 'choices': ['private', 'public']},
        'tenant_permissions': {
            'type': 'list',
            'elements': 'dict',
            'options': {
                'state': {'type': 'str', 'choices': ['absent', 'present'], 'default': 'present'},
                'tenant_id': {'type': 'int', 'required': True},
                'default_target': {'type': 'bool'},
                'default_store': {'type': 'bool'}
            },
            'apply_defaults': False
        },
        'resource_permissions': {
            'type': 'dict',
            'options': {
                'all_groups': {'type': 'bool'},
                'groups': {
                    'type': 'list',
                    'elements': 'dict',
                    'options': {
                        'state': {'type': 'str', 'choices': ['absent', 'present'], 'default': 'present'},
                        'group_id': {'type': 'int', 'aliases': ['site_id']},
                    },
                    'aliases': ['sites']
                },
                'all_plans': {'type': 'bool'},
                'plans': {
                    'type': 'list',
                    'elements': 'dict',
                    'options': {
                        'state': {'type': 'str', 'choices': ['absent', 'present'], 'default': 'present'},
                        'plan_id': {'type': 'int'}
                    }
                }
            }
        }
    }

    result = {
        'changed': False,
        'datastore': {}
    }

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True
    )

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    api_params = module.params.copy()
    if api_params['state'] is not None:
        api_params['active'] = api_params['state'] == 'active'
    for k in ['state', 'tenant_permissions', 'resource_permissions']:
        del api_params[k]

    before_state = morpheus_api.get_cloud_datastores(api_params.copy())

    if module.params['resource_permissions'] is not None:
        api_params['resource_permissions'] = parse_resource_permissions(before_state['resourcePermission'], module.params['resource_permissions'])

    if module.params['tenant_permissions'] is not None:
        api_params['tenant_permissions'] = parse_tenant_permissions(before_state['tenants'], module.params['tenant_permissions'])

    action = {
        'True': partial(parse_check_mode, current_state=before_state.copy()),
        'False': morpheus_api.set_cloud_datastore
    }.get(str(module.check_mode))

    response = action(api_params=api_params)

    changed, diff = mf.dict_diff(response, before_state)

    if module._diff:
        result['diff'] = []

        if changed:
            result['diff'].append({
                'after_header': '{0} ({1})'.format(before_state['name'], before_state['id']),
                'after': '\n'.join([d['after'] for d in diff]),
                'before_header': '{0} ({1})'.format(response['name'], response['id']),
                'before': '\n'.join([d['before'] for d in diff])
            })

    result['changed'] = changed

    result['datastore'] = mf.dict_keys_to_snake_case(response)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
