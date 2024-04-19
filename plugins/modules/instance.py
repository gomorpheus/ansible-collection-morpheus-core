#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: instance
short_description: Basic Management of Morpheus Instances
description:
    - This module provides basic management of Morpheus Instances, such as setting running state, backup, deletion and lock status.
version_added: 0.5.0
author: James Riach (@McGlovin1337)
options:
    match_name:
        description:
            - Define instance selection method when specifying O(name) should more than one instance match.
        default: none
        choices:
            - none
            - first
            - last
            - all
        type: str
    state:
        description:
            - Set the State of the Instance.
            - V(eject) - Ejects ISO media from the instance.
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
        type: str
    remove_options:
        description:
            - When O(state=absent) specify additional removal options.
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
extends_documentation_fragment:
    - action_common_attributes
    - morpheus.core.instance_filter_base
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
    type: list
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

from copy import deepcopy
from functools import partial
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
try:
    import module_utils.morpheus_funcs as mf
    from module_utils.morpheusapi import ApiPath, MorpheusApi
except ModuleNotFoundError:
    import ansible_collections.morpheus.core.plugins.module_utils.morpheus_funcs as mf
    from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import ApiPath, MorpheusApi


INSTANCE_INFO_KEYS = (
    'id',
    'name',
    'locked',
    'status'
)


def instance_state(morpheus_api: MorpheusApi, instance_id: int) -> dict:
    response = morpheus_api.get_instances(
        {
            'id': instance_id
        }
    )

    return mf.dict_filter(response, INSTANCE_INFO_KEYS)


def module_to_api_params(params: dict) -> dict:
    api_params = {}

    for k, v in params['remove_options'].items():
        api_params[k] = v

    return api_params


def parse_check_mode(module_params: dict, instance: dict) -> dict:
    state_key = 'status' if module_params['state'] not in ['locked', 'unlocked'] else 'locked'

    instance[state_key] = {
        'absent': 'removing',
        'backup': instance[state_key],
        'eject': instance[state_key],
        'locked': True,
        'restarted': 'restarting',
        'running': 'starting',
        'started': 'starting',
        'stopped': 'stopping',
        'suspended': 'suspended',
        'unlocked': False
    }.get(module_params['state'])

    return instance


def run_module():
    argument_spec = {
        'id': {'type': 'int'},
        'name': {'type': 'str'},
        'regex_name': {'type': 'bool', 'default': 'false'},
        'match_name': {'type': 'str', 'choices': ['none', 'first', 'last', 'all'], 'default': 'none'},
        'state': {'type': 'str',
                  'choices': ['running', 'started', 'stopped', 'restarted', 'suspended', 'locked', 'unlocked', 'backup', 'absent', 'eject'],
                  'required': True},
        'remove_options': {
            'type': 'dict',
            'apply_defaults': True,
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
        'failed': False,
        'instance_state': []
    }

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    instances = mf.instance_filter(morpheus_api, module.params, INSTANCE_INFO_KEYS)

    action_func = {
        'absent': partial(morpheus_api.common_delete, path=ApiPath.INSTANCES_PATH, api_params=module_to_api_params(module.params)),
        'backup': partial(morpheus_api.instance_action, action='backup'),
        'eject': partial(morpheus_api.instance_action, action='eject'),
        'locked': partial(morpheus_api.instance_action, action='lock'),
        'restarted': partial(morpheus_api.instance_action, action='restart'),
        'running': partial(morpheus_api.instance_action, action='start'),
        'started': partial(morpheus_api.instance_action, action='start'),
        'stopped': partial(morpheus_api.instance_action, action='stop'),
        'suspended': partial(morpheus_api.instance_action, action='suspend'),
        'unlocked': partial(morpheus_api.instance_action, action='unlock')
    }.get(module.params['state'])

    if not module.check_mode:
        results = [mf.dict_keys_to_snake_case(action_func(item_id=instance['id'])) for instance in instances]

        for response in results:
            success, msg = mf.success_response(response[list(response.keys())[0]]) \
                if module.params['state'] not in ['absent', 'locked', 'unlocked'] \
                else mf.success_response(response)
            result['changed'] = success if not result['changed'] else False
            result['failed'] = not success if not result['failed'] else False
    else:
        result['changed'] = True

    result['instance_state'] = [
        instance_state(morpheus_api, inst['id']) for inst in instances
    ] if not module.check_mode else [
        parse_check_mode(
            module_params=module.params,
            instance=inst
        ) for inst in deepcopy(instances)
    ]

    if module._diff:
        result['diff'] = []

        inst_idx = {v['id']: idx for idx, v in enumerate(instances)}

        for after_state in result['instance_state']:
            if module.params['state'] in ['backup', 'eject']:
                result['diff'].append({
                    'prepared': 'Eject media from {0} ({1})\n'.format(after_state['name'], after_state['id'])
                    if module.params['state'] == 'eject' else
                    'Backup {0} ({1})\n'.format(after_state['name'], after_state['id'])
                })
            else:
                changed, diff = mf.dict_diff(after_state, instances[inst_idx[after_state['id']]])
                if changed:
                    result['diff'].append({
                        'after_header': '{0} ({1})'.format(after_state['name'], after_state['id']),
                        'after': '\n'.join(d['after'] for d in diff),
                        'before_header': '{0} ({1})'.format(after_state['name'], after_state['id']),
                        'before': '\n'.join([d['before'] for d in diff])
                    })

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
