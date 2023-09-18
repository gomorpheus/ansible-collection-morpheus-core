#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: instance
short_description: Basic Management of Morpheus Instances
description:
    - This module provides basic management of Morpheus Instances, such as setting running state, backup, deletion and lock status.
version_added: 0.x.x
author: James Riach
options:
    id:
        description:
            - The id of the Instance to Manage.
            - Mutually Exclusive with I(name).
        type: string
    name:
        description:
            - The name of the Instance to Manage. Required if id is not specified.
            - Mutually Exclusive with I(id).
        type: string
    regex_name:
        description:
            - Treat the name parameter as a regular expression.
        default: false
        type: bool
    match_name:
        description:
            - Define instance selection method when specifying I(name) should more than one instance match.
        default: none
        choices:
            - none
            - first
            - last
            - all
        type: string
    state:
        description:
            - Set the State of the Instance.
            - C(eject) - Ejects ISO media from the instance.
        choices:
            - running
            - started
            - stopped
            - restarted
            - suspended
            - locked
            - unlocked
            - backup
            - absent
            - eject
        required: true
        type: string
    remove_options:
        description:
            - When I(state=absent) specify additional removal options.
        type: dict
        suboptions:
            preserve_volumes:
                description:
                    - Preserve the instances volumes.
                default: false
                type: bool
            keep_backups:
                description:
                    - Keep instances backups.
                default: false
                type: bool
            release_floating_ips:
                description:
                    - Release instances floating IP Addresses.
                default: false
                type: bool
            force:
                description:
                    - Force removal of instance.
                default: false
                type: bool
attributes:
    check_mode:
        support: full
    diff_mode:
        support: partial
'''

EXAMPLES = r'''
- name: Restart a specific instance
  morpheus.core.instance:
    id: 200
    state: restarted

- name: Stop all instances matching regex name pattern
  morpheus.core.instance:
    name: ^PROD.*$
    regex_name: true
    match_name: all
    state: stopped

- name: Suspend the first instance that matches name
  morpheus.core.instance:
    name: PRODWEBSVR001
    match_name: first
    state: suspended

- name: Remove instance but keep backups
  morpheus.core.instance:
    name: PRODWEBSVR002
    match_name: first
    state: absent
    remove_options:
      keep_backups: true

- name: Backup all instances
  morpheus.core.instance:
    name: ^.*$
    regex_name: true
    match_name: all
    state: backup
'''

RETURN = r'''
instance_state:
    description:
        - State of the instance(s) following the requested action.
    returned: always
    sample:
        "instance_state": [
            {
                "id": 200,
                "locked": true,
                "name": "PRODWEBSVR001",
                "status": "running"
            }
        ]
'''

import re
from functools import partial
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
try:
    from module_utils.morpheusapi import (
        MorpheusApi, dict_diff, dict_filter, dict_keys_to_snake_case
    )
except ModuleNotFoundError:
    from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import (
        MorpheusApi, dict_diff, dict_filter, dict_keys_to_snake_case
    )


INSTANCE_INFO_KEYS = (
    'id',
    'name',
    'locked',
    'status'
)


def instance_filter(morpheus_api: MorpheusApi, module_params: dict) -> list:
    api_params = module_params.copy()
    if module_params['regex_name']:
        api_params['name'] = None

    for k in ['regex_name', 'match_name', 'state', 'remove_options']:
        del api_params[k]

    response = morpheus_api.get_instances(api_params)
    if not isinstance(response, list):
        response = [response]

    if module_params['name'] is not None and module_params['regex_name']:
        response = [inst for inst in response if re.match(module_params['name'], inst['name'])]

    if len(response) > 1:
        if module_params['match_name'] == 'none':
            return []

        if module_params['match_name'] == 'first':
            return [dict_filter(response[0], INSTANCE_INFO_KEYS)]

        if module_params['match_name'] == 'last':
            return [dict_filter(response[-1], INSTANCE_INFO_KEYS)]

    return [dict_filter(instance, INSTANCE_INFO_KEYS) for instance in response]


def instance_state(morpheus_api: MorpheusApi, instance_id: int) -> dict:
    response = morpheus_api.get_instances(
        {
            'id': instance_id
        }
    )

    return dict_filter(response, INSTANCE_INFO_KEYS)


def mock_diff(instance: dict, expected_state: str, state_key: str = 'status') -> dict:
    diff = {
        'after': '{0} ({1}) {2} = {3}\n'.format(instance['name'], instance['id'], state_key, expected_state),
        'before': '{0} ({1}) {2} = {3}\n'.format(instance['name'], instance['id'], state_key, instance['status'])
    }
    return diff


def run_module():
    argument_spec = {
        'id': {'type': 'str'},
        'name': {'type': 'str'},
        'regex_name': {'type': 'bool', 'default': 'false'},
        'match_name': {'type': 'str', 'choices': ['none', 'first', 'last', 'all'], 'default': 'none'},
        'state': {'type': 'str',
                  'choices': ['running', 'started', 'stopped', 'restarted', 'suspended', 'locked', 'unlocked', 'backup', 'absent', 'eject'],
                  'required': 'true'},
        'remove_options': {
            'type': 'dict',
            'apply_defaults': 'true',
            'options': {
                'preserve_volumes': {'type': 'bool', 'default': 'false'},
                'keep_backups': {'type': 'bool', 'default': 'false'},
                'release_floating_ips': {'type': 'bool', 'default': 'false'},
                'force': {'type': 'bool', 'default': 'false'}
            }
        }
    }

    mutually_exclusive = [
        ('id', 'name'),
        ('id', 'regex_name'),
        ('id', 'match_name')
    ]

    required_one_of = [
        ('id', 'name')
    ]

    module = AnsibleModule(
        argument_spec=argument_spec,
        mutually_exclusive=mutually_exclusive,
        required_one_of=required_one_of,
        supports_check_mode=True
    )

    result = {
        'changed': False,
        'check_mode': module.check_mode,
        'diff': [],
        'failed': False,
        'instance_state': []
    }

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    instances = instance_filter(morpheus_api, module.params)

    action_func = None

    if module.params['state'] == 'absent':
        action_func = partial(morpheus_api.delete_instance, api_params=module.params['remove_options'])
        if module.check_mode:
            result['changed'] = True
        if module._diff and module.check_mode:
            result['diff'] = [
                mock_diff(inst, 'absent')
                for inst in instances
            ]

    elif module.params['state'] == 'restarted':
        action_func = morpheus_api.restart_instance
        if module.check_mode:
            result['changed'] = any(inst['status'] not in ['restarting'] for inst in instances)
        if module._diff and module.check_mode:
            result['diff'] = [
                mock_diff(inst, 'restarting')
                for inst in instances if inst['status'] not in ['restarting']
            ]

    elif module.params['state'] == 'stopped':
        action_func = morpheus_api.stop_instance
        if module.check_mode:
            result['changed'] = any(inst['status'] not in ['stopped', 'starting'] for inst in instances)
        if module._diff and module.check_mode:
            result['diff'] = [
                mock_diff(inst, 'stopped')
                for inst in instances if inst['status'] not in ['stopped', 'stopping']
            ]

    elif module.params['state'] in ['running', 'started']:
        action_func = morpheus_api.start_instance
        if module.check_mode:
            result['changed'] = any(inst['status'] not in ['running', 'starting'] for inst in instances)
        if module._diff and module.check_mode:
            result['diff'] = [
                mock_diff(inst, 'running')
                for inst in instances if inst['status'] not in ['running', 'starting']
            ]

    elif module.params['state'] == 'suspended':
        action_func = morpheus_api.suspend_instance
        if module.check_mode:
            result['changed'] = any(inst['status'] not in ['suspended', 'stopped', 'stopping'] for inst in instances)
        if module._diff and module.check_mode:
            result['diff'] = [
                mock_diff(inst, 'suspended')
                for inst in instances if inst['status'] not in ['suspended', 'stopped', 'stopping']
            ]

    elif module.params['state'] == 'locked':
        action_func = morpheus_api.lock_instance
        if module.check_mode:
            result['changed'] = any(inst['locked'] for inst in instances)
        if module._diff and module.check_mode:
            result['diff'] = [
                mock_diff(inst, 'True', 'locked')
                for inst in instances if not inst['locked']
            ]

    elif module.params['state'] == 'unlocked':
        action_func = morpheus_api.unlock_instance
        if module.check_mode:
            result['changed'] = not any(inst['locked'] for inst in instances)
        if module._diff and module.check_mode:
            result['diff'] = [
                mock_diff(inst, 'False', 'locked')
                for inst in instances if inst['locked']
            ]

    elif module.params['state'] == 'backup':
        action_func = morpheus_api.backup_instance
        if module.check_mode:
            result['changed'] = True

    elif module.params['state'] == 'eject':
        action_func = morpheus_api.eject_instance
        if module.check_mode:
            result['changed'] = True

    if module.check_mode:
        module.exit_json(**result)

    results = [dict_keys_to_snake_case(action_func(instance['id'])) for instance in instances]

    # Check Success Results
    if module.params['state'] not in ['absent', 'locked', 'unlocked']:
        for instance in results:
            for k in instance.keys():
                if instance[k]['success']:
                    result['changed'] = True
                else:
                    result['failed'] = True
    else:
        for instance in results:
            if instance['success']:
                result['changed'] = True
            else:
                result['failed'] = True

    result['instance_state'] = [instance_state(morpheus_api, inst['id']) for inst in instances]

    if module._diff:
        inst_idx = {v['id']: idx for idx, v in enumerate(instances)}

        for after_state in result['instance_state']:
            changed, diff = dict_diff(after_state, instances[inst_idx[after_state['id']]])
            if changed:
                for d in diff:
                    d['after'] = '{0} ({1}) {2}'.format(after_state['name'], after_state['id'], d['after'])
                    d['before'] = '{0} ({1}) {2}'.format(after_state['name'], after_state['id'], d['before'])
                    result['diff'].append(d)

    if result['failed']:
        module.fail_json(
            msg='One or more instances failed to complete the request',
            **result
        )

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
