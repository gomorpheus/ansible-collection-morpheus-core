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


def class_to_dict(input_class: object) -> dict:
    class_dict = input_class.__dict__
    return {
        k: v for k, v in class_dict.items()
        if not k.startswith('_')
    }


def dict_diff(dict_after: dict, dict_before: dict) -> tuple:
    """Compare two dictionaries for differences

    Args:
        dict_after (dict): First Dictionary to Compare
        dict_before (dict): Second Dictionary to Compare

    Returns:
        tuple: A tuple, (True, [diffrences]) if there are differences, otherwise (False, [])
    """
    diff_list = []

    for k, val_a in dict_after.items():
        diff = {
            'after': '{0} = {1}\n'.format(k, val_a),
            'before': 'Unknown\n'
        }

        val_b = None
        try:
            val_b = dict_before[k]
        except KeyError:
            diff_list.append(diff)
            continue

        diff['before'] = '{0} = {1}\n'.format(k, val_b)

        if type(val_a) != type(val_b):
            diff_list.append(diff)
            continue

        if isinstance(val_a, list) and isinstance(val_b, list):
            if len(val_a) != len(val_b):
                diff_list.append(diff)
                continue

            try:
                list_a = sorted(val_a)
                list_b = sorted(val_b)

                if list_a != list_b:
                    diff_list.append(diff)
                    continue
            except TypeError:
                matched_idx = []
                for list_a_item in val_a:
                    for idx_b, list_b_item in enumerate(val_b):
                        if idx_b in matched_idx:
                            continue
                        if isinstance(list_a_item, dict) and isinstance(list_b_item, dict):
                            if dict_compare_equality(list_a_item, list_b_item):
                                matched_idx.append(idx_b)
                if len(matched_idx) != len(val_b):
                    diff_list.append(diff)
                    continue

        if isinstance(val_a, dict) and isinstance(val_b, dict):
            _, sub_diff_list = dict_diff(val_a, val_b)
            diff_list += sub_diff_list

        if val_a != val_b:
            diff_list.append(diff)
            continue

    if len(diff_list) > 0:
        return True, diff_list

    return False, diff_list


def dict_compare_equality(dict_a: dict, dict_b: dict) -> bool:
    """Compare two dictionaries for equality

    Args:
        dict_a (dict): First Dictionary to Compare
        dict_b (dict): Second Dictionary to Compare

    Returns:
        bool: True if both Dictionaries are the same, otherwise False
    """
    if len(dict_a) != len(dict_b):
        return False

    for k, val_a in dict_a.items():
        val_b = None
        try:
            val_b = dict_b[k]
        except KeyError:
            return False

        if type(val_a) != type(val_b):
            return False

        if isinstance(val_a, dict) and isinstance(val_b, dict):
            if not dict_compare_equality(val_a, val_b):
                return False

        if isinstance(val_a, list) and isinstance(val_b, list):
            if len(val_a) != len(val_b):
                return False

            try:
                list_a = sorted(val_a)
                list_b = sorted(val_b)

                if list_a != list_b:
                    return False
            except TypeError:
                matched_idx = []
                for list_a_item in val_a:
                    for idx_b, list_b_item in enumerate(val_b):
                        if idx_b in matched_idx:
                            continue
                        if isinstance(list_a_item, dict) and isinstance(list_b_item, dict):
                            if dict_compare_equality(list_a_item, list_b_item):
                                matched_idx.append(idx_b)
                if len(matched_idx) != len(val_b):
                    return False

        if val_a != val_b:
            return False

    return True


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
        params['all_labels'] = None

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


def success_response(response: dict) -> tuple:
    """Return the value of the response success Key with a corresponding msg

    Args:
        response (dict): The response dictionary to lookup

    Returns:
        tuple: (bool, msg)
    """
    success = False
    msg = ''

    try:
        success = response['success']
    except KeyError:
        success = False

    try:
        msg = response['msg']
    except KeyError:
        if not success:
            msg = 'Unknown Failure'

    return success, msg
