from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import copy
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from functools import partial
from typing import Callable
try:
    import morpheus_funcs as mf
    from morpheusapi import ApiPath, MorpheusApi
except ModuleNotFoundError:
    import ansible_collections.morpheus.core.plugins.module_utils.morpheus_funcs as mf
    from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import ApiPath, MorpheusApi


CLOUD_OPTIONS_COMMON = {
    'state': {'type': 'str', 'choices': ['absent', 'present', 'refresh'], 'default': 'present'},
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
    'timezone': {'type': 'str'},
    'logo': {'type': 'str'},
    'dark_logo': {'type': 'str'},
    'remove_resources': {'type': 'bool', 'default': 'false'},
    'force_remove': {'type': 'bool', 'default': 'false'},
    'refresh_mode': {'type': 'str', 'choices': ['costing', 'costing_rebuild', 'daily', 'hourly'], 'default': 'hourly'},
    'refresh_period': {'type': 'int'}
}

CLOUD_OPTIONS_COMMON_CREDS = CLOUD_OPTIONS_COMMON.copy()
CLOUD_OPTIONS_COMMON_CREDS.update(
    {
        'credential_id': {'type': 'int'}
    }
)

CLOUD_OPTIONS_COMMON_CONFIG = {
    'appliance_url': {'type': 'str'},
    'datacenter_name': {'type': 'str'}
}

CLOUD_OPTIONS_COMMON_CONFIG_CREDS = CLOUD_OPTIONS_COMMON_CONFIG.copy()
CLOUD_OPTIONS_COMMON_CONFIG_CREDS.update(
    {
        'username': {'type': 'str'},
        'password': {'type': 'str', 'no_log': True}
    }
)


def create_update_cloud(
        module: AnsibleModule,
        morpheus_api: MorpheusApi,
        param_convertor: Callable,
        existing_cloud: dict,
        mock_cloud: dict = None) -> dict:
    """Create a new Morpheus Cloud, or update an existing one.

    Args:
        module (AnsibleModule): An instantiated AnsibleModule Class
        morpheus_api (MorpheusApi): An instantiated MorpheusApi Class
        param_convertor (Callable): The Cloud Module specific Function for converting\\
        module parameters to the required API Parameters.
        existing_cloud (dict): Dictionary Details of an existing cloud.
        mock_cloud (dict, optional): The Cloud Module specific Mock response (used when running in check mode).

    Returns:
        dict: Result Dictionary
    """
    api_params = param_convertor(module.params)

    logo = api_params.pop('logo')
    dark_logo = api_params.pop('dark_logo')

    if api_params['agent_mode'] == 'cloudinit':
        api_params['agent_mode'] = 'cloudInit'

    if 'id' in existing_cloud and api_params['id'] is None:
        api_params['id'] = existing_cloud['id']

    action = {
        0: partial(morpheus_api.common_create, path=ApiPath.CLOUDS, api_params=api_params),
        1: partial(morpheus_api.common_set, path=ApiPath.CLOUDS, item_id=api_params.pop('id'), api_params=api_params),
        2: partial(
            parse_check_mode,
            state=module.params['state'],
            api_params=api_params,
            existing_cloud=existing_cloud,
            mock_cloud=mock_cloud)
    }.get('id' in existing_cloud if not module.check_mode else 2)

    action_result = action()
    action_result = mf.dict_keys_to_snake_case(action_result)

    changed, diff = mf.dict_diff(action_result, existing_cloud, ignore_keys={'last_updated'})

    result = {
        'changed': changed and 'id' in action_result,
        'cloud': action_result
    }

    if logo is not None or dark_logo is not None:
        logo_update_response = morpheus_api.update_cloud_logo({
            'id': action_result['id'],
            'logo': logo,
            'dark_logo': dark_logo
        })
        result['logo_update'] = logo_update_response
        success, msg = mf.success_response(logo_update_response)
        result['changed'] = success
        result['failed'] = not success

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
                    'after': 'Create new Cloud\n',
                    'before_header': 'Non-existent Cloud',
                    'before': 'Non-existent Cloud\n'
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
    existing_cloud = morpheus_api.common_get(ApiPath.CLOUDS, {'id': module_params['id']}) \
        if module_params['id'] is not None \
        else morpheus_api.common_get(ApiPath.CLOUDS, {'id': None, 'name': module_params['name']})

    if not isinstance(existing_cloud, list):
        existing_cloud = [existing_cloud]

    existing_cloud = [mf.dict_keys_to_snake_case(cloud) for cloud in existing_cloud]

    return existing_cloud


def parse_check_mode(
        state: str,
        mock_cloud: dict,
        api_params: dict = None,
        existing_cloud: dict = None) -> dict:
    """Function for running the module in check mode

    Args:
        state (str): The module desired state
        mock_cloud (dict): The Cloud Module specific Mock response.
        api_params (dict, optional): The API Parameters that would be used,\\
        derived from the module parameters. Defaults to None.
        existing_cloud (dict, optional): Dictionary Details of an existing cloud. Defaults to None.

    Returns:
        dict: Result Dictionary
    """
    if state == 'absent':
        return {'success': True, 'msg': ''}

    updated_cloud = copy.deepcopy(existing_cloud)

    if 'id' not in existing_cloud:
        updated_cloud = mf.dict_keys_to_snake_case(mock_cloud)

    if api_params['zone_type']['code'] == updated_cloud['zone_type']['code']:
        api_params['zone_type'] = updated_cloud['zone_type']

    for k, v in api_params.items():
        if k in existing_cloud and k != 'config' and v is not None:
            updated_cloud[k] = v

    for k, v in api_params['config'].items():
        if v is not None:
            updated_cloud['config'][k] = v

    return updated_cloud


def refresh_cloud(
        module: AnsibleModule,
        morpheus_api: MorpheusApi,
        existing_cloud: dict) -> dict:
    """Refresh a Cloud Instance

    Args:
        module (AnsibleModule): An Instantiated AnsibleModule Class
        morpheus_api (MorpheusApi): An Instantiated MorpheusApi Class
        existing_cloud (dict): An existing cloud dictionary

    Returns:
        dict: Result Dictionary
    """
    if 'id' not in existing_cloud:
        module.fail_json(
            msg='Cloud not found'
        )

    mode = module.params['refresh_mode'] if module.params['refresh_mode'] != 'costing_rebuild' else 'costing'
    rebuild = 'true' if module.params['refresh_mode'] == 'costing_rebuild' else None
    period = str(module.params['refresh_period']) if module.params['refresh_period'] is not None else None

    api_params = {
        'id': existing_cloud['id'],
        'mode': mode
    }

    if rebuild is not None:
        api_params.update({'rebuild': rebuild})

    if period is not None:
        api_params.update({'period': period})

    response = morpheus_api.refresh_cloud(api_params)

    success, msg = mf.success_response(response)

    return {
        'changed': success,
        'failed': not success,
        'msg': msg
    }


def remove_cloud(
        module: AnsibleModule,
        morpheus_api: MorpheusApi,
        existing_cloud: dict) -> dict:
    """Function to remove a cloud

    Args:
        module (AnsibleModule): An instantiated AnsibleModule Class
        morpheus_api (MorpheusApi): An instantiated MorpheusApi Class
        existing_cloud (dict): Dictionary information of cloud to remove

    Returns:
        dict: Result Dictionary
    """
    if 'id' not in existing_cloud:
        module.fail_json(
            msg='Cloud not found'
        )

    response = morpheus_api.common_delete(
        path=ApiPath.CLOUDS,
        item_id=existing_cloud['id'],
        api_params={
            'remove_resources': module.params['remove_resources'],
            'force': module.params['force_remove']
        }) \
        if not module.check_mode else parse_check_mode(
            state='absent',
            mock_cloud=None)

    success, msg = mf.success_response(response)

    return {
        'changed': success,
        'failed': not success,
        'msg': msg
    }


def run_cloud_module(
        module: AnsibleModule,
        cloud_type: str,
        mock_cloud: dict,
        param_to_api_func: Callable) -> dict:
    """Execute the module

    Args:
        module (AnsibleModule): An instantiated AnsibleModule Class
        cloud_type (str): The type of cloud to be configured
        mock_cloud (dict): A Mock Cloud dictionary for the given cloud type used in check_mode
        param_to_api_func (Callable): A Function to convert module parameters to api parameters

    Returns:
        dict: Module Result Dictionary
    """

    result = {
        'changed': False,
        'cloud': {}
    }

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    existing_cloud = get_cloud(module.params, morpheus_api)

    if len(existing_cloud) > 1:
        module.fail_json(
            msg='Number of matching Clouds exceeded 1, got {0}'.format(len(existing_cloud))
        )

    if len(existing_cloud) == 1 and existing_cloud[0]['zone_type']['code'] != cloud_type:
        module.fail_json(
            msg='Specified Cloud is not correct type'
        )

    if len(existing_cloud) == 0 and (module.params['state'] in ['absent', 'refresh'] or module.params['id'] is not None):
        module.fail_json(
            msg='Specified Cloud not found'
        )

    action = {
        'absent': remove_cloud,
        'present': partial(
            create_update_cloud,
            mock_cloud=mock_cloud,
            param_convertor=param_to_api_func),
        'refresh': refresh_cloud
    }.get(module.params['state'])

    action_result = action(
        module=module,
        morpheus_api=morpheus_api,
        existing_cloud=existing_cloud[0] if len(existing_cloud) > 0 else {})

    result.update(action_result)

    module.exit_json(**result)
