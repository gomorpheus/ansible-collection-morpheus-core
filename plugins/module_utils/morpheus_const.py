from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
name: morpheus_consts
short_description: Shared Constant Variables
description:
    - Shared Constant Variables for Morpheus Modules
version_added: 0.6.0
author: James Riach
'''

# This is an argspec common to cloud modules
CLOUD_OPTIONS_COMMON = {
    'state': {'type': 'str', 'choices': ['absent', 'present'], 'default': 'present'},
    'id': {'type': 'int', 'aliases': ['cloud_id', 'zone_id']},
    'name': {'type': 'str'},
    'description': {'type': 'str'},
    'code': {'type': 'str'},
    'location': {'type': 'str'},
    'visibility': {'type': 'str', 'choices': ['private', 'public']},
    'group_id': {'type': 'int'},
    'account_id': {'type': 'int', 'aliases': ['tenant_id']},
    'enabled': {'type': 'bool'},
    'agent_mode': {'type': 'str', 'choices': ['cloudinit', 'guestexec', 'ssh', 'winrm', 'unattend']},
    'auto_recover_power_state': {'type': 'bool'},
    'costing_mode': {'type': 'str', 'choices': ['off', 'costing'], 'aliases': ['costing']},
    'guidance_mode': {'type': 'str', 'choices': ['off', 'manual'], 'aliases': ['guidance']},
    'scale_priority': {'type': 'int'},
    'security_mode': {'type': 'str', 'choices': ['internal', 'off']},
    'credential_id': {'type': 'int'},
    'timezone': {'type': 'str'},
    'remove_resources': {'type': 'bool', 'default': 'false'},
    'force_remove': {'type': 'bool', 'default': 'false'}
}

CLOUD_OPTIONS_COMMON_CONFIG = {
    'appliance_url': {'type': 'str'},
    'datacenter_name': {'type': 'str'},
    'username': {'type': 'str'},
    'password': {'type': 'str', 'no_log': True}
}
