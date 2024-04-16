#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: azure_cloud
short_description: Manage an Azure Cloud
description:
    - Manage Azure Clouds.
version_added: 0.7.0
author: James Riach (@McGlovin1337)
options:
    subscriber_id:
        description:
            - Azure Subscription ID.
        type: str
        aliases:
            - subscription_id
    azure_tenant_id:
        description:
            - Azure Tenant ID.
        type: str
    client_id:
        description:
            - Azure Client ID.
        type: str
    client_secret:
        description:
            - Azure Client Secret.
        type: str
    resource_group:
        description:
            - Azure Resource Group name.
            - Leaving this blank for a new integration scopes the integration to all Resource Groups.
            - Specify V(all) if wanting to change an existing integration to scope to all Resource Groups.
        type: str
    cloud_type:
        description:
            - Azure Cloud type.
        choices:
            - global
            - usgov
            - german
            - china
        type: str
    region_code:
        description:
            - Scoped region of the Cloud integration.
            - Leaving this blank for a new integration scopes the integration to all regions.
            - Specify V(all) if wanting to change an existing integrations scope to all regions.
        type: str
        aliases:
            - region
    account_type:
        description:
            - The Azure Account Type.
        choices:
            - csp
            - ea
            - standard
        type: str
    rpc_mode:
        description:
            - Cloud workload interaction method.
            - V(guestexec) = Azure Run Command
            - V(rpc) = SSH/WinRM
        choices:
            - guestexec
            - rpc
        type: str
    import_existing:
        description:
            - Inventory Cloud and Import existing Virtual Machines.
        type: bool
    azure_costing_mode:
        description:
            - Azure Costing Mode.
            - V(standard) = Pay As You Go
            - V(csp) = CSP
            - V(azure_plan) = CSP (Microsoft Customer Agreement)
        choices:
            - azure_plan
            - csp
            - standard
        type: str
    csp_tenant_id:
        description:
            - The CSP Tenant ID.
        type: str
    csp_client_id:
        description:
            - The CSP Client ID.
        type: str
    csp_client_secret:
        description:
            - The CSP Client Secret.
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
- name: Create Azure Cloud
  morpheus.core.azure_cloud:
    state: present
    name: Azure Cloud
    description: Azure Cloud
    code: AZCloud
    location: UKSouth
    visibility: private
    group_id: 78
    account_id: 1
    enabled: false
    auto_recover_power_state: false
    costing: off
    guidance: off
    security_mode: off
    timezone: Europe/London
    subscription_id: 2638d5ed-0ed1-4a0c-a57f-688a4850aede
    azure_tenant_id: 5308e59d-e8c7-4f62-8a5c-da82262cb7b7
    client_id: 8b25e5fb-03ff-4275-abfb-0ea1fcb392a2
    client_secret: 5ecr3t
    cloud_type: global
    import_existing: false
    azure_costing_mode: standard
    rpc_mode: guestexec
    agent_mode: guestexec

- name: Refresh Cloud
  morpheus.core.azure_cloud:
    state: refresh
    name: Azure Cloud
    refresh_mode: hourly
'''

RETURN = r'''
cloud:
    description:
        - Information related to specified cloud.
    type: dict
    returned: always
    sample:
        "cloud": {
            "account": {
                "id": 1,
                "name": "MasterTenant"
            },
            "account_id": 1,
            "agent_mode": "guestexec",
            "api_proxy": null,
            "auto_recover_power_state": false,
            "code": "AZCloud",
            "config": {
                "account_type": null,
                "appliance_url": null,
                "azure_costing_mode": "standard",
                "client_id": "8b25e5fb-03ff-4275-abfb-0ea1fcb392a2",
                "client_secret": "************",
                "cloud_type": "global",
                "config_cmdb_discovery": false,
                "csp_client_id": null,
                "csp_client_secret": null,
                "csp_tenant_id": null,
                "datacenter_name": null,
                "import_existing": false,
                "resource_group": null,
                "rpc_mode": "guestexec",
                "subscriber_id": "2638d5ed-0ed1-4a0c-a57f-688a4850aede",
                "tenant_id": "5308e59d-e8c7-4f62-8a5c-da82262cb7b7"
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
            "enabled": false,
            "external_id": null,
            "groups": [
                {
                    "account_id": 1,
                    "id": 78,
                    "name": "Azure Clouds"
                }
            ],
            "guidance_mode": "off",
            "id": 57,
            "image_path": null,
            "inventory_level": "off",
            "last_sync": null,
            "last_sync_duration": null,
            "last_updated": "2024-01-01T00:00:01Z",
            "location": "UKSouth",
            "name": "Azure Cloud",
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
                "code": "azure",
                "id": 9,
                "name": "Azure (Public)"
            },
            "zone_type_id": 9
        }
'''

from ansible.module_utils.basic import AnsibleModule
try:
    import module_utils.cloud_module_common as cloud
except ModuleNotFoundError:
    import ansible_collections.morpheus.core.plugins.module_utils.cloud_module_common as cloud


AZURE_CLOUD_OPTIONS = {
    'subscriber_id': {'type': 'str', 'aliases': ['subscription_id']},
    'azure_tenant_id': {'type': 'str'},
    'client_id': {'type': 'str'},
    'client_secret': {'type': 'str', 'no_log': True},
    'resource_group': {'type': 'str'},
    'cloud_type': {'type': 'str', 'choices': ['global', 'usgov', 'german', 'china']},
    'region_code': {'type': 'str', 'aliases': ['region']},
    'account_type': {'type': 'str', 'choices': ['csp', 'ea', 'standard']},
    'rpc_mode': {'type': 'str', 'choices': ['guestexec', 'rpc']},
    'import_existing': {'type': 'bool'},
    'azure_costing_mode': {'type': 'str', 'choices': ['azure_plan', 'csp', 'standard']},
    'csp_tenant_id': {'type': 'str'},
    'csp_client_id': {'type': 'str'},
    'csp_client_secret': {'type': 'str', 'no_log': True}
}

MOCK_AZURE_CLOUD = {
    'id': 'Known After Create',
    'uuid': 'Known After Create',
    'name': '',
    'code': 'azure',
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
        'code': 'azure',
        'name': 'Azure'
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

    api_params['zone_type'] = {'code': 'azure'}
    tenant_id = api_params.pop('azure_tenant_id')

    api_params['config'] = {**cloud.CLOUD_OPTIONS_COMMON_CONFIG.copy(), **AZURE_CLOUD_OPTIONS.copy()}
    del api_params['config']['azure_tenant_id']
    for k in api_params['config']:
        api_params['config'][k] = api_params[k]
        del api_params[k]
    api_params['config']['tenant_id'] = tenant_id

    api_params['credential'] = {
        'type': 'local'
    }

    api_params['region_code'] = api_params['config'].pop('region_code')

    return api_params


def run_module():
    argument_spec = {**cloud.CLOUD_OPTIONS_COMMON, **cloud.CLOUD_OPTIONS_COMMON_CONFIG, **AZURE_CLOUD_OPTIONS}

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
        cloud_type='azure',
        mock_cloud=MOCK_AZURE_CLOUD,
        param_to_api_func=module_to_api_params
    )


def main():
    run_module()


if __name__ == '__main__':
    main()
