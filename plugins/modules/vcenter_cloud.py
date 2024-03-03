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
    import module_utils.morpheus_funcs as mf
    from module_utils.morpheusapi import MorpheusApi
    from module_utils.morpheus_const import CLOUD_OPTIONS_COMMON, CLOUD_OPTIONS_COMMON_CONFIG
except ModuleNotFoundError:
    import ansible_collections.morpheus.core.plugins.module_utils.morpheus_funcs as mf
    from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import MorpheusApi
    from ansible_collections.morpheus.core.plugins.module_utils.morpheus_const import CLOUD_OPTIONS_COMMON, CLOUD_OPTIONS_COMMON_CONFIG


VCENTER_CLOUD_OPTIONS = {
    'api_url': {'type': 'str'},
    'api_version': {'type': 'str'},
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


def create_update_cloud(module: AnsibleModule, morpheus_api: MorpheusApi, existing_cloud: dict) -> dict:
    """Create a new Morpheus Cloud, or update an existing one.

    Args:
        module (AnsibleModule): An instantiated AnsibleModule Class
        morpheus_api (MorpheusApi): An instantiated MorpheusApi Class
        existing_cloud (dict): Dictionary Details of an existing cloud

    Returns:
        dict: Result Dictionary
    """
    api_params = module_to_api_params(module.params)

    if 'id' in existing_cloud and api_params['id'] is None:
        api_params['id'] = existing_cloud['id']

    action = {
        0: partial(morpheus_api.create_cloud, api_params),
        1: partial(morpheus_api.update_cloud, api_params),
        2: partial(parse_check_mode, state=module.params['state'], api_params=api_params, existing_cloud=existing_cloud)
    }.get('id' in existing_cloud if not module.check_mode else 2)

    action_result = action()
    action_result = mf.dict_keys_to_snake_case(action_result)

    changed, diff = mf.dict_diff(action_result, existing_cloud)

    result = {
        'changed': changed and 'id' in action_result,
        'action': 'id' in existing_cloud,
        'cloud': action_result
    }

    if module._diff:
        diffs = []

        if result['changed']:
            if 'id' in existing_cloud:
                diffs.append({
                    'after_header': '{0} ({1})'.format(action_result['name'], action_result['id']),
                    'after': '\n'.join([d['after'] for d in diff]),
                    'before_header': '{0} ({1})'.format(existing_cloud['name'], existing_cloud['id']),
                    'before': '\n'.join([d['before'] for d in diff])
                })
            else:
                diffs.append({
                    'after_header': '{0} ({1})'.format(action_result['name'], action_result['id']),
                    'after': 'Create new VCenter Cloud\n',
                    'before_header': 'Non-existent VCenter Cloud',
                    'before': 'Non-existent VCenter Cloud\n'
                })

        result['diff'] = diffs

    return result


def get_cloud(module_params: dict, morpheus_api: MorpheusApi) -> list:
    """Returns a list of matching Clouds/Zones

    Args:
        module_params (dict): The specified Module Parameters
        morpheus_api (MorpheusApi): MorpheusApi Instance

    Returns:
        list: List of Clouds/Zones
    """
    existing_cloud = morpheus_api.get_clouds({'id': module_params['id']}) \
        if module_params['id'] is not None \
        else morpheus_api.get_clouds({'id': None, 'name': module_params['name']})

    if not isinstance(existing_cloud, list):
        existing_cloud = [existing_cloud]

    existing_cloud = [mf.dict_keys_to_snake_case(cloud) for cloud in existing_cloud]

    return existing_cloud


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


def parse_check_mode(state: str, api_params: dict = None, existing_cloud: dict = None) -> dict:
    """Function for running the module in check mode

    Args:
        state (str): The module desired state
        api_params (dict, optional): The API Parameters that would be used,\
              derived from the module parameters. Defaults to None.
        existing_cloud (dict, optional): Dictionary Details of an existing cloud. Defaults to None.

    Returns:
        dict: Result Dictionary
    """
    if state == 'absent':
        return {'success': True, 'msg': ''}

    if 'id' not in existing_cloud:
        existing_cloud = MOCK_VCENTER_CLOUD

    api_params = mf.dict_keys_to_camel_case(api_params)

    for k, v in api_params.items():
        if k in existing_cloud:
            existing_cloud[k] = v

    return existing_cloud


def remove_cloud(module: AnsibleModule, morpheus_api: MorpheusApi) -> dict:
    """Function to remove a cloud

    Args:
        module (AnsibleModule): An instantiated AnsibleModule Class
        morpheus_api (MorpheusApi): An instantiated MorpheusApi Class

    Returns:
        dict: Result Dictionary
    """
    response = morpheus_api.delete_cloud(
        module.params['id'],
        {
            'remove_resources': module.params['remove_resources'],
            'force': module.params['force_removal']
        }
        ) \
        if not module.check_mode else parse_check_mode(
            state='absent',
            api_params=module_to_api_params(module.params)
        )

    success, msg = mf.success_response(response)

    return {
        'changed': success,
        'failed': not success,
        'msg': msg
    }


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

    existing_cloud = get_cloud(module.params, morpheus_api)

    if len(existing_cloud) > 1:
        module.fail_json(
            msg='Number of matching Clouds exceeded 1, got {0}'.format(len(existing_cloud))
        )

    if len(existing_cloud) == 1 and existing_cloud[0]['zone_type']['code'] != 'vmware':
        module.fail_json(
            msg='Specified Cloud is not VSphere'
        )

    action = {
        'absent': remove_cloud,
        'present': partial(create_update_cloud, existing_cloud=existing_cloud[0])
    }.get(module.params['state'])

    action_result = action(module, morpheus_api)

    result.update(action_result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
