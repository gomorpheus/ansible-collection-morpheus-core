#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: instance_snapshot_info
short_description: Gather Snapshot information for instances
description:
    - Gather Snapshot information for instances.
version_added: 0.5.0
author: James Riach (@McGlovin1337)
options:
    match_name:
        description:
            - Define instance selection method when specifying I(name) should more than one instance match.
        default: all
        choices:
            - none
            - first
            - last
            - all
        type: str
extends_documentation_fragment:
    - morpheus.core.instance_filter_base
    - morpheus.core.instance_filter_extended
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
    type: list
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

try:
    import module_utils.info_module_common as info_module
    import module_utils.morpheus_funcs as mf
    from module_utils.morpheusapi import MorpheusApi
    from module_utils.morpheus_classes import InstanceSnapshots
except ModuleNotFoundError:
    import ansible_collections.morpheus.core.plugins.module_utils.info_module_common as info_module
    import ansible_collections.morpheus.core.plugins.module_utils.morpheus_funcs as mf
    from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import MorpheusApi
    from ansible_collections.morpheus.core.plugins.module_utils.morpheus_classes import InstanceSnapshots


def run_module():
    argument_spec = {
        **info_module.COMMON_ARG_SPEC,
        **{
            'match_name': {'type': 'str', 'choices': ['none', 'first', 'last', 'all'], 'default': 'all'},
            'environment': {'type': 'str'},
            'labels': {'type': 'list', 'elements': 'str'},
            'match_all_labels': {'type': 'bool', 'default': 'false'},
            'tags': {'type': 'list', 'elements': 'str'}
        }
    }

    result = {
        'changed': False,
        'instance_snapshots': []
    }

    module = AnsibleModule(
        argument_spec=argument_spec,
        mutually_exclusive=info_module.COMMON_MUTUALLY_EXCLUSIVE,
        supports_check_mode=True
    )

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    instances = mf.instance_filter(morpheus_api, module.params)

    result['instance_snapshots'] = [
        mf.class_to_dict(InstanceSnapshots(
            instance_name=instance['name'],
            instance_id=instance['id'],
            morpheus_api=morpheus_api
        ))
        for instance in instances
    ]

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
