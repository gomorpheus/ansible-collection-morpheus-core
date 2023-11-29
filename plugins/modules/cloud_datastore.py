#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: cloud_datastore
short_description: Configure Cloud Datastores
description:
    - Update the configuration of Cloud Datastores.
version_added: 0.x.x
author: James Riach
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
        type: string
    visibility:
        description:
            - The visibility of the Datastore.
        choices:
            - private
            - public
        type: string
    tenant_permissions:
        description:
            - List of Tenant Permissions on the Datastore.
        type: list
        elements: dict
        suboptions:
            accounts:
                description:
                    - List of Tenant Account Id's that are allowed access.
                type: list
                elements: int
            default_target:
                description:
                    - List of Tenant Account Id's to use the specified Datastore as the default.
                type: list
                elements: int
            default_store:
                description:
                    - List of Tenant Account Id's to use the specified Datastore as default Image target.
                type: list
                elements: int
    resource_permissions:
        description:
            - Resource permissions for the Datastore.
        type: dict
        suboptions:
            all:
                description:
                    - Allow or disallow access to all groups.
                type: bool
            sites:
                description:
                    - List of groups that are allowed access to the Datastore.
                type: list
                elements: dict
                suboptions:
                    id:
                        description:
                            - Id of the group to allow access.
                        type: int
                aliases:
                    - groups
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
                    id:
                        description:
                            - Id of the Plan to allow access.
                        type: int
'''

EXAMPLES = r'''
'''

RETURN = r'''
'''

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
        'id': {'type': 'int', 'required': True},
        'zone_id': {'type': 'int', 'required': True, 'aliases': ['cloud_id']},
        'state': {'type': 'str', 'choices': ['active', 'inactive']},
        'visibility': {'type': 'str', 'choices': ['private', 'public']},
        'tenant_permissions': {
            'type': 'list',
            'elements': 'dict',
            'options': {
                'accounts': {'type': 'list', 'elements': 'int'},
                'default_target': {'type': 'list', 'elements': 'int'},
                'default_store': {'type': 'list', 'elements': 'int'}
            }
        },
        'resource_permissions': {
            'type': 'dict',
            'options': {
                'all': {'type': 'bool'},
                'sites': {
                    'type': 'list',
                    'elements': 'dict',
                    'options': {
                        'id': {'type': 'int'}
                    },
                    'aliases': ['groups']
                },
                'all_plans': {'type': 'bool'},
                'plans': {
                    'type': 'list',
                    'elements': 'dict',
                    'options': {
                        'id': {'type': 'int'}
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
        supports_check_mode=False
    )

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    api_params = module.params.copy()
    if api_params['state'] is not None:
        api_params['active'] = api_params['state'] == 'active'
    del api_params['state']

    before_state = morpheus_api.get_cloud_datastores(api_params)

    response = morpheus_api.set_cloud_datastore(api_params)

    result['changed'] = not mf.dict_compare_equality(before_state, response)

    result['datastore'] = mf.dict_keys_to_snake_case(response)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
