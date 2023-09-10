#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: instance_snapshot
short_description: Manage Instance Snapshots
description:
    - Manage Snapshots of Morpheus Instances.
version_added: 0.x.x
author: James Riach
options:
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
            - Manage snapshot state of the specified instance(s)
        choices:
            - absent
            - present
            - revert
            - remove_all
        default: present
        type: string
    snapshot_id:
        description:
            - Specify snapshot by id when using I(state=absent) or I(state=revert).
        type: int
    snapshot_name:
        description:
            - Specify snapshot name.
            - Can be used with I(state=present), I(state=absent), I(state=revert).
        type: string
    snapshot_description:
        description:
            - Specify description for snapshot.
            - Used with I(state=present)
        type: string
    snapshot_age:
        description:
            - Specify the age of the snapshot to match.
        choices:
            - newest
            - oldest
        default: newest
        type: string
extends_documentation_fragment:
    - morepheus.core.instance_filter_base
'''

EXAMPLES = r'''
'''

RETURN = r'''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
try:
    from module_utils.morpheusapi import MorpheusApi
    from module_utils.morpheus_classes import InstanceSnapshots, SnapshotAction
    from module_utils.morpheus_funcs import instance_filter
except ModuleNotFoundError:
    from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import MorpheusApi
    from ansible_collections.morpheus.core.plugins.module_utils.morpheus_classes import InstanceSnapshots, SnapshotAction
    from ansible_collections.morpheus.core.plugins.module_utils.morpheus_funcs import instance_filter


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


def run_module():
    argument_spec = {
        'id': {'type': 'str'},
        'name': {'type': 'str'},
        'regex_name': {'type': 'bool', 'default': 'false'},
        'match_name': {'type': 'str', 'choices': ['none', 'first', 'last', 'all'], 'default': 'none'},
        'state': {'type': 'str', 'choices': ['absent', 'present', 'revert', 'remove_all']},
        'snapshot_id': {'type': 'int'},
        'snapshot_name': {'type': 'str'},
        'snapshot_description': {'type': 'str'},
        'snapshot_age': {'type': 'str', 'choices': ['newest', 'oldest'], 'default': 'newest'}
    }

    mutually_exclusive = [
        ('id', 'name'),
        ('id', 'regex_name'),
        ('id', 'match_name'),
        ('snapshot_id', 'snapshot_name'),
        ('snapshot_id', 'snapshot_description'),
        ('snapshot_id', 'match_age')
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
        supports_check_mode=False
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

    if module.params['id'] is not None or module.params['name'] is not None:
        instances = instance_filter(morpheus_api, module.params)
        sort = module.params['snapshot_age'] == 'newest'
        instance_snapshots = [
            InstanceSnapshots(instance['name'],
                              instance['id'],
                              morpheus_api.get_instance_snapshots(instance['id']))
            for instance in instances
        ]
        for snapshot in instance_snapshots:
            snapshot.sort(reverse=sort)
            if module.params['state'] == 'absent':
                snapshot.snapshots = [snapshot.snapshots[0]]

    if module.params['state'] == 'remove_all':
        snapshot_actions = [
            SnapshotAction(
                morpheus_api=morpheus_api,
                action='remove_all',
                instance_id=instance['id'],
                instance_name=instance['name']
            )
            for instance in instances
        ]

    if module.params['state'] == 'present':
        snapshot_actions = [
            SnapshotAction(
                morpheus_api=morpheus_api,
                action='create',
                instance_id=instance['id'],
                instance_name=instance['name'],
                snapshot_name=module.params['snapshot_name'],
                snapshot_description=module.params['snapshot_description']
            )
            for instance in instances
        ]

    if module.params['state'] in ['absent', 'revert']:
        if module.params['snapshot_id'] is not None:
            if module.params['state'] == 'revert':
                snapshot_actions = [
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
                    if snapshot['id'] == module.params['snapshot_id']
                ]
            else:
                snapshot_actions = [
                    SnapshotAction(
                        morpheus_api=morpheus_api,
                        action='remove',
                        snapshot_id=module.params['snapshot_id']
                    )
                ]

        if module.params['snapshot_name'] is not None:
            snapshot_actions = [
                SnapshotAction(
                    morpheus_api=morpheus_api,
                    action='remove' if module.params['state'] == 'absent' else 'revert',
                    instance_id=instance.instance_id,
                    instance_name=instance.instance_name,
                    snapshot_id=snapshot['id'],
                    snapshot_name=snapshot['name'],
                    snapshot_date=snapshot['date_created'],
                    snapshot_description=snapshot['description']
                )
                for instance in instance_snapshots
                for snapshot in instance.snapshots
                if snapshot['name'] == module.params['snapshot_name']
            ]

        if module.params['state'] == 'revert':
            instance_reverts = []
            for action in snapshot_actions:
                if not any(action.instance_id == revert.instance_id for revert in instance_reverts):
                    instance_reverts.append(action)
            snapshot_actions = instance_reverts

    result['snapshot_results'] = exec_snapshot_actions(snapshot_actions)
    result['changed'] = any(action_result['success'] for action_result in result['snapshot_results'])

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
