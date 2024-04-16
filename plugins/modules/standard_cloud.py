#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: standard_cloud
short_description: Manage a Standard Morpheus Cloud
description:
    - Manage Standard Morpheus Clouds.
version_added: 0.7.0
author: James Riach (@McGlovin1337)
options:
    enable_network_type_selection:
        description:
            - Enable user to select the Network Interface type.
        type: bool
    import_existing:
        description:
            - Inventory Cloud and Import existing Virtual Machines.
        type: bool
extends_documentation_fragment:
    - action_common_attributes
    - morpheus.core.cloud_options_common
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
- name: Create Standard Cloud
  morpheus.core.standard_cloud:
    state: present
    name: Std Cloud
    description: Morpheus Std Cloud
    code: stdcloud
    location: everywhere
    auto_recover_power_state: false
    guidance: off
    costing: off
    group_id: 200
    account_id: 1
    timezone: Europe/London
    import_existing: false
    enable_network_type_selection: true
    agent_mode: cloudinit

- name: Remove Standard Cloud
  morpheus.core.standard_cloud:
    state: absent
    name: Std Cloud
    force_remove: true

- name: Refresh Cloud
  morpheus.core.standard_cloud:
    state: refresh
    name: Std Cloud
    refresh_mode: daily
'''

RETURN = r'''
cloud:
    description:
        - Information related to the specified cloud.
    type: dict
    returned: always
    sample:
        "cloud": {
            "account": {
                "id": 1,
                "name": "MasterTenant"
            },
            "account_id": 1,
            "agent_mode": "cloudInit",
            "api_proxy": null,
            "auto_recover_power_state": false,
            "code": "stdcloud",
            "config": {
                "appliance_url": null,
                "config_cmdb_discovery": false,
                "datacenter_name": null,
                "enable_network_type_selection": true,
                "import_existing": false
            },
            "console_keymap": null,
            "container_mode": "docker",
            "cost_last_sync": null,
            "cost_last_sync_duration": null,
            "cost_status": "ok",
            "cost_status_date": null,
            "cost_status_message": null,
            "costing_mode": "off",
            "credential": {
                "type": "local"
            },
            "dark_image_path": null,
            "date_created": "2024-01-01T00:00:01Z",
            "domain_name": "localdomain",
            "enabled": true,
            "external_id": null,
            "groups": [
                {
                    "account_id": 1,
                    "id": 200,
                    "name": "STD Group"
                }
            ],
            "guidance_mode": "off",
            "id": 60,
            "image_path": null,
            "inventory_level": "off",
            "last_sync": null,
            "last_sync_duration": null,
            "last_updated": "2024-01-01T00:00:01Z",
            "location": "everywhere",
            "name": "Std Cloud",
            "network_domain": null,
            "network_server": null,
            "next_run_date": null,
            "owner": {
                "id": 1,
                "name": "MasterTenant"
            },
            "provisioning_proxy": null,
            "region_code": null,
            "scale_priority": 1,
            "security_mode": "off",
            "security_server": null,
            "server_count": 0,
            "service_version": null,
            "stats": {
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
            "status": "initializing",
            "status_date": null,
            "status_message": null,
            "storage_mode": "standard",
            "timezone": "Europe/London",
            "user_data_linux": null,
            "user_data_windows": null,
            "visibility": "private",
            "zone_type": {
                "code": "standard",
                "id": 3,
                "name": "Morpheus"
            },
            "zone_type_id": 3
        }
'''

from ansible.module_utils.basic import AnsibleModule
try:
    import module_utils.cloud_module_common as cloud
except ModuleNotFoundError:
    import ansible_collections.morpheus.core.plugins.module_utils.cloud_module_common as cloud


STD_CLOUD_OPTIONS = {
    'enable_network_type_selection': {'type': 'bool'},
    'import_existing': {'type': 'bool'}
}

MOCK_STD_CLOUD = {
    'id': 'Known After Create',
    'uuid': 'Known After Create',
    'name': '',
    'code': 'standard',
    'labels': [],
    'location': None,
    'owner': {
        'id': 0,
        'name': ''
    },
    'accountId': 0,
    'account': {
        'id': 0,
        'name': ''
    },
    'visibility': 'private',
    'enabled': True,
    'zoneType': {
        'id': 0,
        'code': 'standard',
        'name': 'Morpheus'
    }
}


def module_to_api_params(module_params: dict) -> dict:
    """Convert Module Parameters to the required API Parameters

    Args:
        module_params (dict): The Ansible Module Parameters

    Returns:
        dict: A Dictionary of API Parameters
    """
    api_params = module_params.copy()

    del api_params['state']
    del api_params['remove_resources']
    del api_params['force_remove']

    api_params['zone_type'] = {'code': 'standard'}

    api_params['config'] = {**cloud.CLOUD_OPTIONS_COMMON_CONFIG.copy(), **STD_CLOUD_OPTIONS.copy()}
    for k in api_params['config']:
        api_params['config'][k] = api_params[k]
        del api_params[k]

    return api_params


def run_module():
    argument_spec = {**cloud.CLOUD_OPTIONS_COMMON, **cloud.CLOUD_OPTIONS_COMMON_CONFIG, **STD_CLOUD_OPTIONS}

    mutually_exclusive = [
        ('id', 'name')
    ]

    required_if = [
        ('state', 'absent', ('id', 'name'), True),
        ('id', None, ('name',)),
        ('name', None, ('id',))
    ]

    module = AnsibleModule(
        argument_spec=argument_spec,
        mutually_exclusive=mutually_exclusive,
        required_if=required_if,
        supports_check_mode=True
    )

    cloud.run_cloud_module(
        module=module,
        cloud_type='standard',
        mock_cloud=MOCK_STD_CLOUD,
        param_to_api_func=module_to_api_params
    )


def main():
    run_module()


if __name__ == '__main__':
    main()
