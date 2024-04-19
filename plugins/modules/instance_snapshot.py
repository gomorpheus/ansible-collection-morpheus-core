#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: instance_snapshot
short_description: Manage Instance Snapshots
description:
    - Manage Snapshots of Morpheus Instances.
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
            - Manage snapshot state of the specified instance(s)
        choices:
            - absent
            - present
            - revert
            - remove_all
        default: present
        type: str
    snapshot_id:
        description:
            - Specify snapshot by id when using O(state=absent) or O(state=revert).
        type: int
    snapshot_name:
        description:
            - Specify snapshot name.
            - Can be used with O(state=present), O(state=absent), O(state=revert).
        type: str
    snapshot_description:
        description:
            - Specify description for snapshot.
            - Used with O(state=present)
        type: str
    snapshot_age:
        description:
            - Specify the age of the snapshot to match.
        choices:
            - latest
            - oldest
        default: latest
        type: str
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
- name: Snapshot All Instances
  morpheus.core.instance_snapshot:
    name: ^.*$
    match_name: all
    regex_name: true
    snapshot_name: Ansible Snapshot
    snapshot_description: Snapshot Created via Ansible
    state: present

- name: Remove All Snapshots for Specific Instance
  morpheus.core.instance_snapshot:
    id: 200
    state: remove_all

- name: Revert Instance to Oldest Snapshot matching Name
  morpheus.core.instance_snapshot:
    name: WebServer001
    snapshot_name: Ansible Snapshot
    snapshot_age: oldest
    state: revert

- name: Remove Specific Snapshot by Id
  morpheus.core.instance_snapshot:
    snapshot_id: 50
    state: absent

- name: Remove the Latest Snapshot matching Name for all Instances
  morpheus.core.instance_snapshot:
    name: ^.*$
    match_name: all
    regex_name: true
    snapshot_name: Ansible Snapshot
    state: absent
'''

RETURN = r'''
snapshot_results:
    description:
        - List of results of each action performed against each instance and/or snapshot.
    type: list
    returned: always
    sample:
        "snapshot_results": [
            {
                "action": "create",
                "instance_id": 1,
                "instance_name": "WebServer001",
                "msg": "",
                "snapshot_date": null,
                "snapshot_description": "Snapshot Created via Ansible",
                "snapshot_id": null,
                "snapshot_name": "Ansible Snapshot",
                "success": true
            }
        ]
'''

from copy import deepcopy
from functools import partial
from time import sleep
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
try:
    import module_utils.morpheus_funcs as mf
    from module_utils.morpheusapi import MorpheusApi
    from module_utils.morpheus_classes import InstanceSnapshots, SnapshotAction
except ModuleNotFoundError:
    import ansible_collections.morpheus.core.plugins.module_utils.morpheus_funcs as mf
    from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import MorpheusApi
    from ansible_collections.morpheus.core.plugins.module_utils.morpheus_classes import InstanceSnapshots, SnapshotAction


def exec_snapshot_actions(actions: list[SnapshotAction]) -> list[dict]:
    """Execute the Actions from a List of SnapshotAction objects

    Args:
        actions (list[SnapshotAction]): List of SnapshotAction Objects

    Returns:
        list[dict]: List of SnapshotAction Execution Dictionaries
    """
    results = []
    for action in actions:
        results.append(action.execute())

    return results


def parse_check_mode(module_params: dict, instance_snapshot: InstanceSnapshots,
                     action: SnapshotAction) -> InstanceSnapshots:

    if module_params['state'] == 'remove_all':
        instance_snapshot.snapshots = []
        instance_snapshot.snapshot_count = 0
        return instance_snapshot

    if module_params['state'] == 'absent':
        instance_snapshot.snapshots = [
            snapshot for snapshot in instance_snapshot.snapshots
            if snapshot['id'] != action.snapshot_id
        ]
        instance_snapshot.snapshot_count = len(instance_snapshot.snapshots)
        return instance_snapshot

    if module_params['state'] == 'present':
        instance_snapshot.snapshots.append({
            'name': action.snapshot_name,
            'description': action.snapshot_description
        })
        instance_snapshot.snapshot_count = len(instance_snapshot.snapshots)
        return instance_snapshot


def snapshot_create(module_params: dict, morpheus_api: MorpheusApi, instances: list) -> list[SnapshotAction]:
    return [
        SnapshotAction(
            morpheus_api=morpheus_api,
            action='create',
            instance_id=instance['id'],
            instance_name=instance['name'],
            snapshot_name=module_params['snapshot_name'],
            snapshot_description=module_params['snapshot_description']
        )
        for instance in instances
    ]


def snapshot_remove(module_params: dict, morpheus_api: MorpheusApi, instance_snapshots: InstanceSnapshots = None) -> list[SnapshotAction]:
    if module_params['snapshot_id'] is not None:
        return [
            SnapshotAction(
                morpheus_api=morpheus_api,
                action='remove',
                snapshot_id=module_params['snapshot_id']
            )
        ]

    if module_params['snapshot_name'] is not None:
        return [
            SnapshotAction(
                morpheus_api=morpheus_api,
                action='remove',
                instance_id=instance.instance_id,
                instance_name=instance.instance_name,
                snapshot_id=snapshot['id'],
                snapshot_name=snapshot['name'],
                snapshot_date=snapshot['date_created'],
                snapshot_description=snapshot['description']
            )
            for instance in instance_snapshots
            for snapshot in instance.snapshots
            if snapshot['name'] == module_params['snapshot_name']
        ]


def snapshot_remove_all(morpheus_api: MorpheusApi, instances: list) -> list[SnapshotAction]:
    return [
        SnapshotAction(
            morpheus_api=morpheus_api,
            action='remove_all',
            instance_id=instance['id'],
            instance_name=instance['name']
        )
        for instance in instances
    ]


def snapshot_revert(module_params: dict, morpheus_api: MorpheusApi, instance_snapshots: InstanceSnapshots) -> list[SnapshotAction]:
    if module_params['snapshot_id'] is not None:
        actions = [
            SnapshotAction(
                morpheus_api=morpheus_api,
                action='revert',
                instance_id=instance.instance_id,
                instance_name=instance.instance_name,
                snapshot_id=snapshot['id'],
                snapshot_name=snapshot['name'],
                snapshot_date=snapshot['date_created'],
                snapshot_description=snapshot['description']
            )
            for instance in instance_snapshots
            for snapshot in instance.snapshots
            if snapshot['id'] == module_params['snapshot_id']
        ]

    if module_params['snapshot_name'] is not None:
        actions = [
            SnapshotAction(
                morpheus_api=morpheus_api,
                action='revert',
                instance_id=instance.instance_id,
                instance_name=instance.instance_name,
                snapshot_id=snapshot['id'],
                snapshot_name=snapshot['name'],
                snapshot_date=snapshot['date_created'],
                snapshot_description=snapshot['description']
            )
            for instance in instance_snapshots
            for snapshot in instance.snapshots
            if snapshot['name'] == module_params['snapshot_name']
        ]

    # Filter actions to ensure an instance is only reverted once
    snapshot_actions = []
    for action in actions:
        if not any(action.instance_id == revert.instance_id for revert in snapshot_actions):
            snapshot_actions.append(action)

    return snapshot_actions


def run_module():
    argument_spec = {
        'id': {'type': 'int'},
        'name': {'type': 'str'},
        'regex_name': {'type': 'bool', 'default': 'false'},
        'match_name': {'type': 'str', 'choices': ['none', 'first', 'last', 'all'], 'default': 'none'},
        'state': {'type': 'str', 'choices': ['absent', 'present', 'revert', 'remove_all'], 'default': 'present'},
        'snapshot_id': {'type': 'int'},
        'snapshot_name': {'type': 'str'},
        'snapshot_description': {'type': 'str'},
        'snapshot_age': {'type': 'str', 'choices': ['latest', 'oldest'], 'default': 'latest'}
    }

    mutually_exclusive = [
        ('id', 'name'),
        ('id', 'regex_name'),
        ('id', 'match_name'),
        ('snapshot_id', 'snapshot_name'),
        ('snapshot_id', 'snapshot_description')
    ]

    required_one_of = [
        ('id', 'name', 'snapshot_id')
    ]

    result = {
        'changed': False,
        'snapshot_results': []
    }

    module = AnsibleModule(
        argument_spec=argument_spec,
        mutually_exclusive=mutually_exclusive,
        required_one_of=required_one_of,
        supports_check_mode=True
    )

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    # additional parameter validation
    if module.params['snapshot_id'] is not None and module.params['state'] not in ['absent', 'revert']:
        module.fail_json(
            msg='snapshot_id only valid when state is one of: absent, revert',
            **result
        )

    if module.params['state'] == 'revert' and module.params['id'] is None and module.params['name'] is None:
        module.fail_json(
            msg='id or name required when state is: revert',
            **result
        )

    instances = None
    instance_snapshots = None
    if module.params['id'] is not None or module.params['name'] is not None:
        instances = mf.instance_filter(morpheus_api, module.params)
        sort = module.params['snapshot_age'] == 'latest'
        instance_snapshots = [
            InstanceSnapshots(instance['name'],
                              instance['id'],
                              morpheus_api,
                              sort)
            for instance in instances
        ]
        for inst_snapshot in instance_snapshots:
            if module.params['state'] == 'absent':
                try:
                    inst_snapshot.snapshots = [inst_snapshot.snapshots[0]]
                except IndexError:
                    inst_snapshot.snapshots = []

    action_func = {
        'absent': partial(
            snapshot_remove,
            module_params=module.params,
            instance_snapshots=instance_snapshots
        ),
        'present': partial(
            snapshot_create,
            module_params=module.params,
            instances=instances
        ),
        'remove_all': partial(
            snapshot_remove_all,
            instances=instances
        ),
        'revert': partial(
            snapshot_revert,
            module_params=module.params,
            instance_snapshots=instance_snapshots
        )
    }.get(module.params['state'])

    snapshot_actions = action_func(morpheus_api=morpheus_api)

    result['snapshot_results'] = exec_snapshot_actions(snapshot_actions) \
        if not module.check_mode else [mf.class_to_dict(action) for action in snapshot_actions]

    result['changed'] = any(action_result['success'] for action_result in result['snapshot_results']) \
        if not module.check_mode else True

    if module._diff:
        result['diff'] = []
        sleep(3)  # Allow enough time for actions to fully execute

        if module.params['state'] == 'revert':
            prepared_actions = [
                'Revert {0} ({1}) to snapshot_id: {2}'.format(
                    action.instance_name, action.instance_id, action.snapshot_id
                )
                for action in snapshot_actions
            ]
            result['diff'].append({
                'prepared': '\n'.join(prepared_actions)
            })

        if module.params['state'] == 'absent' and instances is None:
            prepared_actions = [
                'Remove snapshot_id {0}'.format(action.snapshot_id)
                for action in snapshot_actions
            ]
            result['diff'].append({
                'prepared': '\n'.join(prepared_actions)
            })

        if instances is not None and module.params['state'] != 'revert':
            updated_snapshots = [
                InstanceSnapshots(instance['name'],
                                  instance['id'],
                                  morpheus_api,
                                  sort)
                for instance in instances
            ] if not module.check_mode else [
                parse_check_mode(
                    module_params=module.params,
                    instance_snapshot=inst_snapshot,
                    action=snapshot_action
                )
                for inst_snapshot in deepcopy(instance_snapshots)
                for snapshot_action in snapshot_actions
                if inst_snapshot.instance_id == snapshot_action.instance_id
            ]

            for inst_snapshot in updated_snapshots:
                before = mf.class_to_dict(
                    next((inst for inst in instance_snapshots if inst.instance_id == inst_snapshot.instance_id), ValueError)
                )
                after = mf.class_to_dict(inst_snapshot)

                changed, diff = mf.dict_diff(after, before)

                if changed:
                    result['diff'].append({
                        'after_header': '{0} ({1})'.format(inst_snapshot.instance_name, inst_snapshot.instance_id),
                        'after': '\n'.join([d['after'] for d in diff]),
                        'before_header': '{0} ({1})'.format(inst_snapshot.instance_name, inst_snapshot.instance_id),
                        'before': '\n'.join([d['before'] for d in diff])
                    })

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
