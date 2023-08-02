from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
name: morph_api_classes
short_description: Shared Morpheus API Classes
description:
    - Shared Classes for Morpheus API Modules
version_added: 0.x.x
author: James Riach
'''

try:
    from morpheusapi import dict_keys_to_snake_case
except ModuleNotFoundError:
    from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import dict_keys_to_snake_case


class InstanceSnapshots():
    def __init__(self, instance_name: str, instance_id: int, snapshots: list[dict]) -> None:
        self.instance_name = instance_name
        self.instance_id = instance_id
        self.snapshot_count = len(snapshots)
        self.snapshots = [dict_keys_to_snake_case(snapshot) for snapshot in snapshots]
