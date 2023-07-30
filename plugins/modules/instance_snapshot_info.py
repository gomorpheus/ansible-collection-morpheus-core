#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: instance_snapshot_info
short_description: Gather Snapshot information for instances
description:
    - Gather Snapshot information for instances.
version_added: 0.x.x
author: James Riach
extends_documentation_fragment:
    - morpheus.core.instance_filter_base
    - morpheus.core.instance_filter_extended
'''

EXAMPLES = r'''
- name: Get Snapshots for specific instance
  morpheus.core.instance_snapshot_info:
    id: 200

- name: Get Snapshots for instances matching regex pattern
  morpheus.core.instance_snapshot_info:
    name: ^PRODWEB.*$
    regex_name: true

- name: Get Snapshots for instances with assigned labels
  morpheus.core.instance_snapshot_info:
    labels:
      - PROD
      - WEB
'''

RETURN = r'''
instance_snapshots:
    description:
        - List of Instances and their snapshots
    returned: always
    sample:
        "instance_snapshots": [
            {
                "instance_id": 200,
                "instance_name": "PRODWEBSVR001",
                "snapshot_count": 1,
                "snapshots": [
                    {
                        "currently_active": true,
                        "datastore": null,
                        "date_created": "2023-07-29T15:33:05Z",
                        "description": "Pre-maintenance Snapshot",
                        "external_id": "snapshot-100000",
                        "id": 1,
                        "name": "PRODWEBSVR001-2023-07-29T15:32:51.774Z",
                        "parent_snapshot": null,
                        "snapshot_created": "2023-07-29T15:33:36Z",
                        "snapshot_type": "vm",
                        "state": null,
                        "status": "complete",
                        "zone": {
                            "id": 5,
                            "name": "Web Cloud"
                        }
                    }
                ]
            }
        ]
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import MorpheusApi, dict_keys_to_snake_case


class InstanceSnapshots():
    def __init__(self, instance_name: str, instance_id: int, snapshots: list[dict]) -> None:
        self.instance_name = instance_name
        self.instance_id = instance_id
        self.snapshot_count = len(snapshots)
        self.snapshots = [dict_keys_to_snake_case(snapshot) for snapshot in snapshots]


def run_module():
    argument_spec = {
        'id': {'type': 'int'},
        'name': {'type': 'str'},
        'regex_name': {'type': 'bool', 'default': 'false'},
        'environment': {'type': 'str'},
        'labels': {'type': 'list', 'elements': 'str'},
        'match_all_labels': {'type': 'bool', 'default': 'false'},
        'tags': {'type': 'str'}
    }

    mutually_exclusive = [
        ('id', 'name'),
        ('id', 'regex_name')
    ]

    result = {
        'changed': False,
        'instance_snapshots': []
    }

    module = AnsibleModule(
        argument_spec=argument_spec,
        mutually_exclusive=mutually_exclusive,
        supports_check_mode=True
    )

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    api_params = module.params.copy()
    if module.params['regex_name']:
        api_params['name'] = None
    api_params['all_labels'] = api_params.pop('labels') if module.params['match_all_labels'] else None

    for k in ['match_all_labels', 'regex_name']:
        del api_params[k]

    instances = morpheus_api.get_instances(api_params)

    if not isinstance(instances, list):
        instances = [instances]

    for instance in instances:
        snapshots = morpheus_api.get_instance_snapshots(instance['id'])
        instance_snapshots = InstanceSnapshots(instance['name'], instance['id'], snapshots)
        result['instance_snapshots'].append(vars(instance_snapshots))

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
