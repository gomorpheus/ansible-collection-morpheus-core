from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
from functools import partial
from typing import Callable
try:
    import morpheus_funcs as mf
    from morpheusapi import MorpheusApi
    from morpheus_const import CLOUD_OPTIONS_COMMON, CLOUD_OPTIONS_COMMON_CONFIG
except ModuleNotFoundError:
    import ansible_collections.morpheus.core.plugins.module_utils.morpheus_funcs as mf
    from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import MorpheusApi
    from ansible_collections.morpheus.core.plugins.module_utils.morpheus_const import CLOUD_OPTIONS_COMMON, CLOUD_OPTIONS_COMMON_CONFIG


def create_update_cloud(
        module: AnsibleModule,
        morpheus_api: MorpheusApi,
        param_convertor: Callable,
        existing_cloud: dict,
        mock_cloud: dict = None
        ) -> dict:
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

    if 'id' in existing_cloud and api_params['id'] is None:
        api_params['id'] = existing_cloud['id']

    action = {
        0: partial(morpheus_api.create_cloud, api_params),
        1: partial(morpheus_api.update_cloud, api_params),
        2: partial(
            parse_check_mode,
            state=module.params['state'],
            api_params=api_params,
            existing_cloud=existing_cloud,
            mock_cloud=mock_cloud
            )
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
    existing_cloud = morpheus_api.get_clouds({'id': module_params['id']}) \
        if module_params['id'] is not None \
        else morpheus_api.get_clouds({'id': None, 'name': module_params['name']})

    if not isinstance(existing_cloud, list):
        existing_cloud = [existing_cloud]

    existing_cloud = [mf.dict_keys_to_snake_case(cloud) for cloud in existing_cloud]

    return existing_cloud


def parse_check_mode(
        state: str,
        mock_cloud: dict,
        api_params: dict = None,
        existing_cloud: dict = None
        ) -> dict:
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

    if 'id' not in existing_cloud:
        existing_cloud = mock_cloud

    api_params = mf.dict_keys_to_camel_case(api_params)

    for k, v in api_params.items():
        if k in existing_cloud:
            existing_cloud[k] = v

    return existing_cloud


def remove_cloud(
        module: AnsibleModule,
        morpheus_api: MorpheusApi,
        param_convertor: Callable
        ) -> dict:
    """Function to remove a cloud

    Args:
        module (AnsibleModule): An instantiated AnsibleModule Class
        morpheus_api (MorpheusApi): An instantiated MorpheusApi Class
        param_convertor (Callable): The Cloud Module specific Function for converting\\
        module parameters to the required API Parameters.

    Returns:
        dict: Result Dictionary
    """
    response = morpheus_api.delete_cloud(
        module.params['id'],
        {
            'remove_resources': module.params['remove_resources'],
            'force': module.params['force_remove']
        }
        ) \
        if not module.check_mode else parse_check_mode(
            state='absent',
            mock_cloud=None,
            api_params=param_convertor(module.params)
        )

    success, msg = mf.success_response(response)

    return {
        'changed': success,
        'failed': not success,
        'msg': msg
    }
