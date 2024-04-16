#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: appliance_maintenance_mode
short_description: Toggle Maintenance Mode of the target Morpheus Appliance
description:
    - Toggles Maintenance Mode of the target Morpheus Appliance
version_added: 0.4.0
author: James Riach (@McGlovin1337)
options:
    state:
        description:
            - Enable or Disable Maintenance Mode
        default: enabled
        choices:
            - enabled
            - disabled
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
- name: Enable Appliance Maintenance Mode
  morpheus.core.appliance_maintenance_mode:
    state: enabled

- name: Disable Appliance Maintenance Mode
  morpheus.core.appliance_maintenance_mode:
    state: disabled
'''

RETURN = r'''
success:
    description:
        - If the API Request was Successful
    returned: always
    type: bool
    sample:
        "success": true
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
        'state': {
            'type': 'str',
            'default': 'enabled',
            'choices': ['enabled', 'disabled']
        }
    }

    result = {
        'changed': False
    }

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True
    )

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    # It seems some versions of the API has this key, and others don't
    try:
        original_state = morpheus_api.get_appliance_settings()['maintenanceMode']
    except KeyError:
        original_state = 'unknown'

    desired_state = True if module.params['state'] == 'enabled' else False
    diff = []

    if module.check_mode:
        if original_state != desired_state:
            result['changed'] = True
            diff.append(
                {
                    'after': 'maintenanceMode = {}\n'.format(desired_state),
                    'before': 'maintenanceMode = {}\n'.format(original_state)
                }
            )

            if module._diff:
                result['diff'] = diff

        module.exit_json(**result)

    response = morpheus_api.set_appliance_maintenance_mode(desired_state)

    result['success'] = mf.success_response(response)

    if not result['success']:
        module.fail_json('API Request Failed', **result)

    # It seems some versions of the API has this key, and others don't
    # If it doesn't exist we assume the state based on the success of the API request
    try:
        updated_state = morpheus_api.get_appliance_settings()['maintenanceMode']
    except KeyError:
        updated_state = True if result['success'] else False

    result['changed'] = True if updated_state != original_state else False

    if module._diff:
        if updated_state != original_state:
            diff.append(
                {
                    'after': 'maintenanceMode = {}\n'.format(updated_state),
                    'before': 'maintenanceMode = {}\n'.format(original_state)
                }
            )
        result['diff'] = diff

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
