#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: vcenter_cloud
short_description: Manage a VMware VCenter Cloud
description:
    - Manage VMware VCenter Clouds.
version_added: 0.x.x
author: James Riach
options:
    api_url:
        description:
            - The VCenter API URL.
        type: string
    api_version:
        description:
            - The VCenter API Version.
        choices:
            - 7.0
            - 6.7
            - 6.5
            - 6.0
        type: string
    datacenter:
        description:
            - VCenter Datacenter name.
        type: string
    cluster:
        description:
            - VCenter Cluster name.
        type: string
    resource_pool:
        description:
            - VCenter Resource Pool name.
        type: string
    rpc_mode:
        description:
            - Cloud workload interaction method.
            - V(guestexec) = VMWare Tools
            - V(rpc) = SSH/WinRM
        choices:
            - guestexec
            - rpc
        type: string
    disk_storage_type:
        description:
            - The default Virtual Machine Disk type.
        choices:
            - thin
            - thick
            - thick_eager
        type: string
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
            - no
            - pt
        type: string
        aliases:
            - keyboard_layout
extends_documentation_fragment:
    - morpheus.core.cloud_options_common
'''

EXAMPLES = r'''
'''

RETURN = r'''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from functools import partial
try:
    import module_utils.cloud_module_common as cloud
    from module_utils.morpheusapi import MorpheusApi
    from module_utils.morpheus_const import CLOUD_OPTIONS_COMMON, CLOUD_OPTIONS_COMMON_CONFIG
except ModuleNotFoundError:
    import ansible_collections.morpheus.core.plugins.module_utils.cloud_module_common as cloud
    from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import MorpheusApi
    from ansible_collections.morpheus.core.plugins.module_utils.morpheus_const import CLOUD_OPTIONS_COMMON, CLOUD_OPTIONS_COMMON_CONFIG


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
    'console_keymap': {
        'type': 'str',
        'choices': [
            'us',
            'uk',
            'de',
            'de-ch',
            'es',
            'fi',
            'fr',
            'fr-be',
            'fr-ch',
            'is',
            'it',
            'jp',
            'nl-be',
            'no',
            'pt'
        ],
        'aliases': ['keyboard_layout']
    }
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

    api_params['config'] = {**CLOUD_OPTIONS_COMMON_CONFIG.copy(), **VCENTER_CLOUD_OPTIONS.copy()}
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
    argument_spec = {**CLOUD_OPTIONS_COMMON, **CLOUD_OPTIONS_COMMON_CONFIG, **VCENTER_CLOUD_OPTIONS}

    mutually_exclusive = [
        ('id', 'name'),
        ('credential_id', 'username'),
        ('credential_id', 'password')
    ]

    required_if = [
        ('state', 'absent', ('id', 'name'), True),
        ('id', None, ('name')),
        ('name', None, ('id'))
    ]

    result = {
        'changed': False,
        'cloud': {}
    }

    module = AnsibleModule(
        argument_spec=argument_spec,
        mutually_exclusive=mutually_exclusive,
        required_if=required_if,
        supports_check_mode=True
    )

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    existing_cloud = cloud.get_cloud(module.params, morpheus_api)

    if len(existing_cloud) > 1:
        module.fail_json(
            msg='Number of matching Clouds exceeded 1, got {0}'.format(len(existing_cloud))
        )

    if len(existing_cloud) == 1 and existing_cloud[0]['zone_type']['code'] != 'vmware':
        module.fail_json(
            msg='Specified Cloud is not VSphere'
        )

    if len(existing_cloud) == 0 and (module.params['state'] == 'absent' or module.params['id'] is not None):
        module.fail_json(
            msg='Specified Cloud not found'
        )

    action = {
        'absent': cloud.remove_cloud,
        'present': partial(
            cloud.create_update_cloud,
            existing_cloud=existing_cloud[0] if len(existing_cloud) > 0 else {},
            mock_cloud=MOCK_VCENTER_CLOUD
            )
    }.get(module.params['state'])

    action_result = action(
        module=module,
        morpheus_api=morpheus_api,
        param_convertor=module_to_api_params
    )

    result.update(action_result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
