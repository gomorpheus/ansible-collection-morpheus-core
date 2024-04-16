#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: vcenter_cloud
short_description: Manage a VMware VCenter Cloud
description:
    - Manage VMware VCenter Clouds.
version_added: 0.7.0
author: James Riach (@McGlovin1337)
options:
    api_url:
        description:
            - The VCenter API URL.
        type: str
    api_version:
        description:
            - The VCenter API Version.
        choices:
            - "7.0"
            - "6.7"
            - "6.5"
            - "6.0"
        type: str
    datacenter:
        description:
            - VCenter Datacenter name.
        type: str
    cluster:
        description:
            - VCenter Cluster name.
        type: str
    resource_pool:
        description:
            - VCenter Resource Pool name.
        type: str
    rpc_mode:
        description:
            - Cloud workload interaction method.
            - V(guestexec) = VMWare Tools
            - V(rpc) = SSH/WinRM
        choices:
            - guestexec
            - rpc
        type: str
    disk_storage_type:
        description:
            - The default Virtual Machine Disk type.
        choices:
            - thin
            - thick
            - thick_eager
        type: str
    enable_disk_type_selection:
        description:
            - Enable user to select Virtual Machine Disk type.
        type: bool
    enable_storage_type_selection:
        description:
            - Enable user to select the Storage type.
        type: bool
    enable_network_type_selection:
        description:
            - Enable user to select the Network Interface type.
        type: bool
    enable_vnc:
        description:
            - Enable Hyper-Visor Console.
        type: bool
        aliases:
            - enable_console
    hide_host_selection:
        description:
            - Hide Cloud Host selection.
        type: bool
    import_existing:
        description:
            - Inventory Cloud and Import existing Virtual Machines.
        type: bool
    console_keymap:
        description:
            - Guest console keyboard layout.
        choices:
            - us
            - uk
            - de
            - de-ch
            - es
            - fi
            - fr
            - fr-be
            - fr-ch
            - is
            - it
            - jp
            - nl-be
            - "no"
            - pt
        type: str
        aliases:
            - keyboard_layout
    credential_id:
        description:
            - Specify id of existing credentials to use.
        type: int
    username:
        description:
            - Specify a username to access the cloud.
        type: str
    password:
        description:
            - Specify a password to access the cloud.
        type: str
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
- name: Create new VCenter Cloud
  morpheus.core.vcenter_cloud:
    state: present
    name: VCenter Cloud
    description: A VCenter Cloud
    code: 'vccloud'
    location: 'south'
    visibility: private
    group_id: 50
    account_id: 1
    enabled: true
    agent_mode: cloudinit
    auto_recover_power_state: false
    import_existing: false
    costing_mode: off
    guidance_mode: off
    security_mode: off
    credential_id: 3
    api_url: 'https://vcenter.domain.tld/sdk'
    api_version: '7.0'
    datacenter: 'VCCloud'
    cluster: 'Cluster01'
    resource_pool: 'All'
    rpc_mode: guestexec
    disk_storage_type: thin
    enable_disk_type_selection: true
    enable_storage_type_selection: false
    enable_network_type_selection: true
    enable_vnc: true
    hide_host_selection: true
    console_keymap: uk
    timezone: "Europe/London"

- name: Remove VCenter Cloud
  morpheus.core.vcenter_cloud:
    state: absent
    id: 56
    force_remove: true

- name: Refresh and Rebuild Cloud Costing
  morpheus.core.vcenter_cloud:
    state: refresh
    name: VCenter Cloud
    refresh_mode: costing_rebuild
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
            "agent_mode": "cloudinit",
            "api_proxy": null,
            "auto_recover_power_state": false,
            "code": "vccloud",
            "config": {
                "api_url": "https://vcenter.domain.tld/sdk",
                "api_version": "7.0",
                "appliance_url": null,
                "cluster": "Cluster01",
                "config_cmdb_discovery": false,
                "datacenter": "VCCloud",
                "datacenter_name": null,
                "disk_storage_type": "thin",
                "enable_disk_type_selection": true,
                "enable_network_type_selection": true,
                "enable_storage_type_selection": false,
                "enable_vnc": true,
                "hide_host_selection": true,
                "import_existing": false,
                "resource_pool": "All",
                "rpc_mode": "guestexec"
            },
            "console_keymap": "uk",
            "container_mode": "docker",
            "cost_last_sync": null,
            "cost_last_sync_duration": null,
            "cost_status": "ok",
            "cost_status_date": null,
            "cost_status_message": null,
            "costing_mode": "off",
            "credential": {
                "id": 3,
                "name": "VCenter Creds",
                "type": "username-password"
            },
            "dark_image_path": null,
            "date_created": "2024-01-01T00:00:01Z",
            "domain_name": "localdomain",
            "enabled": false,
            "external_id": null,
            "groups": [
                {
                    "account_id": 1,
                    "id": 50,
                    "name": "VCGroup"
                }
            ],
            "guidance_mode": "manual",
            "id": 56,
            "image_path": null,
            "inventory_level": "off",
            "last_sync": null,
            "last_sync_duration": null,
            "last_updated": "2024-01-01T00:00:01Z",
            "location": "south",
            "name": "VCenter Cloud",
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
                "code": "vmware",
                "id": 28,
                "name": "VMware vCenter"
            },
            "zone_type_id": 28
        }
'''

from ansible.module_utils.basic import AnsibleModule
try:
    import module_utils.cloud_module_common as cloud
    from module_utils.morpheus_const import KEYMAP_OPTIONS
except ModuleNotFoundError:
    import ansible_collections.morpheus.core.plugins.module_utils.cloud_module_common as cloud
    from ansible_collections.morpheus.core.plugins.module_utils.morpheus_const import KEYMAP_OPTIONS


VCENTER_CLOUD_OPTIONS = {
    'api_url': {'type': 'str'},
    'api_version': {'type': 'str', 'choices': ['7.0', '6.7', '6.5', '6.0']},
    'datacenter': {'type': 'str'},
    'cluster': {'type': 'str'},
    'resource_pool': {'type': 'str'},
    'rpc_mode': {'type': 'str', 'choices': ['guestexec', 'rpc']},
    'disk_storage_type': {'type': 'str', 'choices': ['thin', 'thick', 'thick_eager']},
    'enable_disk_type_selection': {'type': 'bool'},
    'enable_storage_type_selection': {'type': 'bool'},
    'enable_network_type_selection': {'type': 'bool'},
    'enable_vnc': {'type': 'bool', 'aliases': ['enable_console']},
    'hide_host_selection': {'type': 'bool'},
    'import_existing': {'type': 'bool'},
    'console_keymap': {'type': 'str', 'choices': KEYMAP_OPTIONS, 'aliases': ['keyboard_layout']}
}

MOCK_VCENTER_CLOUD = {
    'id': 'Known After Create',
    'uuid': 'Known After Create',
    'name': '',
    'code': 'vmware',
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
        'code': 'vmware',
        'name': 'VMware vCenter'
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

    api_params['zone_type'] = {'code': 'vmware'}

    api_params['config'] = {**cloud.CLOUD_OPTIONS_COMMON_CONFIG_CREDS.copy(), **VCENTER_CLOUD_OPTIONS.copy()}
    for k in api_params['config']:
        api_params['config'][k] = api_params[k]
        del api_params[k]

    api_params['credential'] = {
        'type': 'username-password' if api_params['credential_id'] is not None else 'local'
    }

    if api_params['credential_id'] is not None:
        api_params['credential']['id'] = api_params.pop('credential_id')
        del api_params['config']['username']
        del api_params['config']['password']

    api_params['console_keymap'] = api_params['config'].pop('console_keymap')

    return api_params


def run_module():
    argument_spec = {**cloud.CLOUD_OPTIONS_COMMON_CREDS, **cloud.CLOUD_OPTIONS_COMMON_CONFIG_CREDS, **VCENTER_CLOUD_OPTIONS}

    mutually_exclusive = [
        ('id', 'name'),
        ('credential_id', 'username'),
        ('credential_id', 'password')
    ]

    required_if = [
        ('state', 'absent', ('id', 'name'), True),
        ('state', 'refresh', ('id', 'name'), True),
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
        cloud_type='vmware',
        mock_cloud=MOCK_VCENTER_CLOUD,
        param_to_api_func=module_to_api_params
    )


def main():
    run_module()


if __name__ == '__main__':
    main()
