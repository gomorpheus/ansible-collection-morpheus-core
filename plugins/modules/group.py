#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: group
short_description: Manage Groups
description:
    - Create, Update and Remove Groups.
version_added: 0.7.0
author: James Riach (@McGlovin1337)
options:
    state:
        description:
            - V(present) will create or update a Group, or V(absent) will remove a Group.
        choices:
            - absent
            - present
        default: present
        type: str
    id:
        description:
            - Id of an existing Group.
        type: int
    name:
        description:
            - Name of the Group.
        type: str
    code:
        description:
            - Short Code name for the Group.
        type: str
    labels:
        description:
            - List of Labels for the Group.
        type: list
        elements: str
    location:
        description:
            - Location information for the Group.
        type: str
    dns_id:
        description:
            - Id of a DNS Integration.
        type: int
    cmdb_id:
        description:
            - Id of a CMDB Integration.
        type: int
    cm_id:
        description:
            - Id of a Change Management Integration.
        type: int
    service_registry_id:
        description:
            - Id of a Service Registry Integration.
        type: int
    config_management_id:
        description:
            - Id of a Configuration Management Integration.
        type: int
    cmdb_discovery:
        description:
            - Enable/Disable CMDB Discovery.
        type: bool
    zones:
        description:
            - Set the state of Clouds/Zones in this Group.
        type: list
        elements: dict
        suboptions:
            state:
                description:
                    - The state of the Cloud/Zone in the Group.
                choices:
                    - absent
                    - present
                default: present
                type: str
            id:
                description:
                    - The Id of the Cloud/Zone.
                type: int
                required: true
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
- name: Create/Update a Group
  morpheus.core.group:
    state: present
    name: MyGroup
    code: my_group
    location: Earth

- name: Update Clouds/Zones in Group
  morpheus.core.group:
    state: present
    name: MyGroup
    zones:
      - state: present
        id: 17
      - state: present
        id: 18

- name: Remove Group
  morpheus.core.group:
    state: absent
    name: MyGroup
'''

RETURN = r'''
group:
    description:
        - Group Information.
    type: dict
    returned: always
    sample:
        "group": {
            "account_id": 1,
            "active": true,
            "code": "my_group",
            "config": {
                "config_cm_id": null,
                "config_cmdb_discovery": false,
                "config_cmdb_id": null,
                "config_management_id": null,
                "dns_integration_id": null,
                "service_registry_id": null
            },
            "date_created": "2024-01-01T00:00:01Z",
            "id": 284,
            "last_updated": "2024-01-01T00:00:01Z",
            "location": "Earth",
            "name": "MyGroup",
            "server_count": 0,
            "stats": {
                "instance_counts": {
                    "all": 0
                },
                "server_counts": {
                    "all": 0,
                    "baremetal": 0,
                    "container_host": 0,
                    "host": 0,
                    "hypervisor": 0,
                    "unmanaged": 0,
                    "vm": 0
                }
            },
            "zones": [
                {
                    "id": 17,
                    "name": "MyCloud"
                }
            ]
        }
'''

from functools import partial
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
try:
    import module_utils.morpheus_funcs as mf
    from module_utils.morpheusapi import ApiPath, MorpheusApi
except ModuleNotFoundError:
    import ansible_collections.morpheus.core.plugins.module_utils.morpheus_funcs as mf
    from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import ApiPath, MorpheusApi


MOCK_GROUP = {
    "account_id": 0,
    "active": True,
    "code": "Known After Create",
    "config": {
        "config_cmdb_discovery": False,
        "config_management_id": "",
        "service_registry_id": ""
    },
    "date_created": "",
    "id": 0,
    "last_updated": "",
    "location": "",
    "name": "Known After Create",
    "server_count": 0,
    "stats": {
        "instance_counts": {
            "all": 0
        },
        "server_counts": {
            "all": 0,
            "baremetal": 0,
            "container_host": 0,
            "host": 0,
            "hypervisor": 0,
            "unmanaged": 0,
            "vm": 0
        }
    },
    "uuid": "Known After Create",
    "zones": []
}


def create_update_group(module: AnsibleModule, morpheus_api: MorpheusApi, existing_group: dict) -> dict:
    """Create a new Group or Update and existing one.

    Args:
        module (AnsibleModule): An instantiated AnsibleModule Class
        morpheus_api (MorpheusApi): An instantiated MorpheusApi Class
        existing_group (dict): Details of an existing Group

    Returns:
        dict: Result of the creation or update request
    """
    api_params = module_to_api_params(module.params)

    if 'id' in existing_group and api_params['id'] is None:
        api_params['id'] = existing_group['id']

    action = {
        'False': partial(morpheus_api.common_create, path=ApiPath.GROUPS_PATH, api_params=api_params),
        'True': partial(morpheus_api.common_set, path=ApiPath.GROUPS_PATH, item_id=api_params.pop('id'), api_params=api_params),
        'Check': partial(parse_check_mode, state=module.params['state'], api_params=api_params, existing_group=existing_group)
    }.get(str('id' in existing_group) if not module.check_mode else 'Check')

    action_result = action()
    action_result = mf.dict_keys_to_snake_case(action_result)

    changed, diff = mf.dict_diff(action_result, existing_group, {'last_updated', 'server_count', 'stats'})
    result = {
        'changed': changed and 'id' in action_result,
        'group': action_result
    }

    if module.params['zones'] is not None:
        zone_params = zone_update_params(
            zone_states=module.params['zones'],
            current_zones=existing_group['zones'] if 'zones' in existing_group else []
        )

        if not module.check_mode:
            zone_update = morpheus_api.update_group_zones({
                **{'id': action_result['id'] if 'id' in action_result else existing_group['id']},
                **zone_params
            })

            success, msg = mf.success_response(zone_update)

            if success:
                updated_group = morpheus_api.common_get(ApiPath.GROUPS_PATH, {'id': action_result['id'] if 'id' in action_result else existing_group['id']})
                updated_group = mf.dict_keys_to_snake_case(updated_group)
                result['group'] = updated_group
                changed, diff = mf.dict_diff(updated_group, existing_group, {'last_updated', 'server_count', 'stats'})
                result['changed'] = changed
        else:
            zone_update = parse_check_mode(
                state='present',
                api_params=zone_params,
                existing_group=action_result if 'id' in action_result else existing_group
            )
            result['group'] = zone_update
            changed, diff = mf.dict_diff(zone_update, existing_group, {'last_updated', 'server_count', 'stats'})
            result['changed'] = changed

    if module._diff:
        diffs = []

        if result['changed']:
            if 'id' in existing_group:
                diffs.append({
                    'after_header': '{0} ({1})'.format(action_result['name'], action_result['id']),
                    'after': '\n'.join([d['after'] for d in diff]),
                    'before_header': '{0} ({1})'.format(existing_group['name'], existing_group['id']),
                    'before': '\n'.join([d['before'] for d in diff])
                })
            else:
                diffs.append({
                    'after_header': '{0} ({1})'.format(action_result['name'], action_result['id']),
                    'after': 'Create new Group\n',
                    'before_header': 'Non-existent Group',
                    'before': 'Non-existent Group\n'
                })

        result['diff'] = diffs

    return result


def get_existing_group(module: AnsibleModule, morpheus_api: MorpheusApi) -> dict:
    """Returns an existing group if one matches the module parameters.

    Args:
        module (AnsibleModule): An instantiated AnsibleModule Class
        morpheus_api (MorpheusApi): An instantiated MorpheusApi Class

    Returns:
        dict: Dictionary details of the existing group if it exists
    """
    existing_group = morpheus_api.common_get(
        ApiPath.GROUPS_PATH,
        {
            'id': module.params['id'],
            'name': module.params['name']
        }
    )

    if isinstance(existing_group, list):
        if len(existing_group) > 1:
            module.fail_json(
                msg='Number of matching groups exceeded 1, got {0}'.format(len(existing_group))
            )
        existing_group = existing_group[0] if len(existing_group) == 1 else {}

    return mf.dict_keys_to_snake_case(existing_group)


def module_to_api_params(module_params: dict) -> dict:
    """Convert Module Parameters to API Parameters.

    Args:
        module_params (dict): Ansible Module Parameters

    Returns:
        dict: Dictionary of API Parameters
    """
    api_params = module_params.copy()

    api_params['config'] = {
        'dns_integration_id': api_params.pop('dns_id'),
        'config_cmdb_id': api_params.pop('cmdb_id'),
        'config_cm_id': api_params.pop('cm_id'),
        'service_registry_id': api_params.pop('service_registry_id'),
        'config_management_id': api_params.pop('config_management_id'),
        'config_cmdb_discovery': api_params.pop('cmdb_discovery')
    }

    for param in ['state', 'zones']:
        del api_params[param]

    return api_params


def parse_check_mode(state: str, api_params: dict, existing_group: dict) -> dict:
    """Returns a predicted result when the module is run in check mode.

    Args:
        state (str): The value of the module state parameter
        api_params (dict): API Parameters
        existing_group (dict): Details of an existing group if it exists

    Returns:
        dict: Predicted result
    """
    if state == 'absent':
        return {'success': True, 'msg': ''}

    updated_group = existing_group.copy() if len(existing_group) > 0 else MOCK_GROUP

    if 'id' not in existing_group:
        existing_group = MOCK_GROUP

    for k, v in api_params.items():
        if k in existing_group and k != 'config' and v is not None:
            updated_group[k] = v

    for k, v in api_params['config'].items():
        if v is not None:
            updated_group['config'][k] = v

    return updated_group


def remove_group(module: AnsibleModule, morpheus_api: MorpheusApi, existing_group: dict) -> dict:
    """Removes an existing group.

    Args:
        module (AnsibleModule): An instantiated AnsibleModule Class
        morpheus_api (MorpheusApi): An instantiated MorpheusApi Class
        existing_group (dict): Dictionary details of an existing group

    Returns:
        dict: Result dictionary
    """
    if 'id' not in existing_group:
        module.fail_json(
            msg='Specified Group does not exist'
        )

    action = {
        'False': partial(morpheus_api.common_delete, path=ApiPath.GROUPS_PATH, item_id=existing_group['id']),
        'True': partial(parse_check_mode, state='absent', api_params={}, existing_group=existing_group)
    }.get(str(module.check_mode))

    response = action()
    success, msg = mf.success_response(response)

    return {
        'changed': success,
        'failed': not success,
        'msg': msg
    }


def zone_update_params(zone_states: list, current_zones: list) -> dict:
    """Compares the existing zones in a group and updates the list from those
    specified in the module parameters.

    Args:
        zone_states (list): List of Dictionaries with expected state of each specified zone
        current_zones (list): The List of Zones in the existing group

    Returns:
        dict: An API formated list of zones to apply.
    """
    current_zone_ids = [zone['id'] for zone in current_zones]

    removals = [zone['id'] for zone in zone_states if zone['state'] == 'absent']
    additions = [{'id': zone['id']} for zone in zone_states if zone['state'] == 'present']

    new_zone_ids = [{'id': zone} for zone in current_zone_ids if zone not in removals] + additions

    return {'zones': new_zone_ids}


def run_module():
    argument_spec = {
        'state': {'type': 'str', 'choices': ['absent', 'present'], 'default': 'present'},
        'id': {'type': 'int'},
        'name': {'type': 'str'},
        'code': {'type': 'str'},
        'labels': {'type': 'list', 'elements': 'str'},
        'location': {'type': 'str'},
        'dns_id': {'type': 'int'},
        'cmdb_id': {'type': 'int'},
        'cm_id': {'type': 'int'},
        'service_registry_id': {'type': 'int'},
        'config_management_id': {'type': 'int'},
        'cmdb_discovery': {'type': 'bool'},
        'zones': {'type': 'list', 'elements': 'dict', 'options': {
            'state': {'type': 'str', 'choices': ['absent', 'present'], 'default': 'present'},
            'id': {'type': 'int', 'required': True}
        }}
    }

    result = {
        'changed': False,
        'group': {}
    }

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True
    )

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    existing_group = get_existing_group(module, morpheus_api)

    action = {
        'absent': remove_group,
        'present': create_update_group
    }.get(module.params['state'])

    action_result = action(module=module, morpheus_api=morpheus_api, existing_group=existing_group)

    result.update(action_result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
