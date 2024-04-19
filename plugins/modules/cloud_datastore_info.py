#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: cloud_datastore_info
short_description: Datastore information for a specified cloud
description:
    - Retrieves Datastore information for a specified cloud.
version_added: 0.7.0
author: James Riach (@McGlovin1337)
options:
    detail:
        description:
            - Level of detail returned.
        default: summary
        choices:
            - summary
            - full
        type: str
    zone_id:
        description:
            - Id of the Cloud to query.
        required: true
        type: int
        aliases:
            - cloud_id
    active:
        description:
            - Filter by whether the Datastore is active or not.
        type: bool
    online:
        description:
            - Filter by whether the Datastore is online or not.
        type: bool
    visibility:
        description:
            - Filter by visibility of the Datastore.
        choices:
            - private
            - public
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
- name: Retrieve all Datastores for specified Cloud
  morpheus.core.cloud_datastore_info:
    zone_id: 15

- name: Retrieve all offline Datastores
  morpheus.core.cloud_datastore_info:
    zone_id: 15
    online: false

- name: Retrieve all Online, but inactive Datastores
  morpheus.core.cloud_datastore_info:
    zone_id: 15
    online: true
    active: false
'''

RETURN = r'''
datastores:
    description:
        - A List of Datastores.
    type: list
    returned: always
    sample:
        "datastores": [
            {
                "active": true,
                "free_space": 52737672740864,
                "id": 200,
                "name": "vmware-ds001",
                "online": true,
                "type": "cluster",
                "visibility": "public",
                "zone": {
                    "id": 5,
                    "name": "vmware cloud"
                }
            }
        ]
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
try:
    import module_utils.info_module_common as info_module
    import module_utils.morpheus_funcs as mf
    from module_utils.morpheusapi import MorpheusApi
except ModuleNotFoundError:
    import ansible_collections.morpheus.core.plugins.module_utils.info_module_common as info_module
    import ansible_collections.morpheus.core.plugins.module_utils.morpheus_funcs as mf
    from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import MorpheusApi


API_FILTER_KEYS = {
    'summary': (
        'id',
        'name',
        'type',
        'active',
        'online',
        'freeSpace',
        'visibility',
        'zone'
    )
}


def run_module():
    argument_spec = {
        **info_module.COMMON_ARG_SPEC,
        **{
            'detail': {'type': 'str', 'choices': ['full', 'summary'], 'default': 'summary'},
            'zone_id': {'type': 'int', 'required': True, 'aliases': ['cloud_id']},
            'active': {'type': 'bool'},
            'online': {'type': 'bool'},
            'visibility': {'type': 'str', 'choices': ['private', 'public']}
        }
    }

    result = {
        'changed': False,
        'datastores': []
    }

    module = AnsibleModule(
        argument_spec=argument_spec,
        mutually_exclusive=info_module.COMMON_MUTUALLY_EXCLUSIVE,
        supports_check_mode=True
    )

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    api_params = info_module.param_filter(module, ['active', 'visibility'])

    response = morpheus_api.get_cloud_datastores(api_params)

    response = info_module.response_filter(module, response, API_FILTER_KEYS)

    if module.params['visibility'] is not None:
        response = [response_item for response_item in response if response_item['visibility'] == module.params['visibility']]

    if module.params['active'] is not None:
        response = [response_item for response_item in response if bool(response_item['active']) is module.params['active']]

    if module.params['online'] is not None:
        response = [response_item for response_item in response if bool(response_item['online']) is module.params['online']]

    result['datastores'] = [mf.dict_keys_to_snake_case(response_item) for response_item in response]

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
