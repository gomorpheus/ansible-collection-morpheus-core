from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
name: morpheus_funcs
short_description: Shared Morpheus Module Functions
description:
    - Shared Functions for Morpheus Ansible Modules
version_added: 0.x.x
author: James Riach
'''

import re
try:
    from morpheusapi import MorpheusApi, dict_filter
except ModuleNotFoundError:
    from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import MorpheusApi, dict_filter


def instance_filter(morpheus_api: MorpheusApi, module_params: dict, key_filter: list = None) -> list:
    """Filters Morpheus Instances returned from the Morpheus API according to supplied module parameters.
        Module Parameters that are not valid API Parameters are stripped prior to calling get_instances() method.

    Args:
        morpheus_api (MorpheusApi): Instance of the MorpheusApi Class
        module_params (dict): Module Parameters used to make the API request and filter results
        key_filter (list, optional): An optional list of dictionary keys to filter the results. Defaults to None.

    Returns:
        list: A list of instances and associated info
    """
    params = module_params.copy()
    if module_params['regex_name']:
        params['name'] = None

    try:
        params['details'] = 'extra' in module_params['detail']
    except KeyError:
        params['details'] = False

    try:
        params['show_deleted'] = 'include' in module_params['deleted']
    except KeyError:
        params['show_deleted'] = False

    try:
        params['deleted'] = 'only' in module_params['deleted']
    except KeyError:
        params['deleted'] = False

    try:
        params['all_labels'] = params.pop('labels') if module_params['match_all_labels'] else None
    except KeyError:
        params['all_labels'] = False

    # this could be extended to support further API parameters if needed
    valid_params = [
        'id',
        'name',
        'instance_type',
        'agent_installed',
        'status',
        'environment',
        'show_deleted',
        'deleted',
        'labels',
        'all_labels',
        'tags',
        'details'
    ]

    api_params = {}
    for param in valid_params:
        try:
            api_params[param] = params[param]
        except KeyError:
            continue

    response = morpheus_api.get_instances(api_params)
    if not isinstance(response, list):
        response = [response]

    try:
        if module_params['name'] is not None and module_params['regex_name']:
            response = [inst for inst in response if re.match(module_params['name'], inst['name'])]
    except KeyError:
        pass

    if len(response) > 1:
        try:
            match_name = module_params['match_name']
        except KeyError:
            match_name = 'none'

        return {
            'none': [],
            'first': [response[0]] if key_filter is None else [dict_filter(response[0], key_filter)],
            'last': [response[-1]] if key_filter is None else [dict_filter(response[-1], key_filter)],
            'all': [instance if key_filter is None else dict_filter(instance, key_filter) for instance in response]
        }.get(match_name)

    return [dict_filter(instance, key_filter) if key_filter is not None else instance for instance in response]
