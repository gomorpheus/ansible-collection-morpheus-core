from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
name: morpheus_funcs
short_description: Shared Morpheus Module Functions
description:
    - Shared Functions for Morpheus Ansible Modules
version_added: 0.5.0
author: James Riach
'''

import re
try:
    from morpheusapi import MorpheusApi
except ModuleNotFoundError:
    from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import MorpheusApi


def class_to_dict(input_class: object) -> dict:
    class_dict = input_class.__dict__
    return {
        k: v for k, v in class_dict.items()
        if not k.startswith('_')
    }


def dict_diff(dict_after: dict, dict_before: dict, ignore_keys: set = None) -> tuple:
    """Compare two dictionaries for differences

    Args:
        dict_after (dict): First Dictionary to Compare
        dict_before (dict): Second Dictionary to Compare
        ignore_keys (set): Set of Dictionary Keys to ignore comparison

    Returns:
        tuple: A tuple, (True, [diffrences]) if there are differences, otherwise (False, [])
    """
    diff_list = []

    if ignore_keys is None:
        ignore_keys = set()

    for k, val_a in dict_after.items():
        if k in ignore_keys:
            continue

        diff = {
            'after': '{0} = {1}\n'.format(k, val_a),
            'before': 'Unknown\n'
        }

        val_b = None
        if k in dict_before:
            val_b = dict_before[k]
        else:
            diff_list.append(diff)
            continue

        diff['before'] = '{0} = {1}\n'.format(k, val_b)

        if type(val_a) is not type(val_b):
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
            is_diff, sub_diff_list = dict_diff(val_a, val_b)
            diff_list += sub_diff_list

        if val_a != val_b:
            diff_list.append(diff)
            continue

    if len(diff_list) > 0:
        return True, diff_list

    return False, diff_list


def dict_compare_equality(dict_a: dict, dict_b: dict, ignore_keys: set = None) -> bool:
    """Compare two dictionaries for equality

    Args:
        dict_a (dict): First Dictionary to Compare
        dict_b (dict): Second Dictionary to Compare
        ignore_keys (set): Set of Dictionary Keys to ignore comparison

    Returns:
        bool: True if both Dictionaries are the same, otherwise False
    """
    if ignore_keys is None:
        ignore_keys = set()

    if len(dict_a) != len(dict_b):
        return False

    for k, val_a in dict_a.items():
        if k in ignore_keys:
            continue

        val_b = None
        if k in dict_b:
            val_b = dict_b[k]
        else:
            return False

        if type(val_a) is not type(val_b):
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


def dict_filter(dictionary: dict, filter_keys: list) -> dict:
    """Return a filtered dictionary based on a list of keys to retain

    Args:
        dictionary (dict): The original dictionary to filter
        filter_keys (list): A list of keys to retain.
          To filter subkeys use a list or tuple in the format of ['key', ['subkeyA', 'subkeyB']]

    Returns:
        dict: A dictionary with only the keys specified in filter_keys
    """
    subkey_filters = {k: v for k, v in enumerate(filter_keys) if isinstance(v, (list, set, tuple))}

    if len(subkey_filters) > 0:
        for k, v in subkey_filters.items():
            filter_keys[k] = v[0]

    filtered_dict = {k: v for k, v in dictionary.items() if k in filter_keys}

    if len(subkey_filters) > 0:
        for k, v in subkey_filters.items():
            try:
                if isinstance(filtered_dict[v[0]], (list, set, tuple)):
                    for idx, itm in enumerate(filtered_dict[v[0]]):
                        filtered_dict[v[0]][idx] = dict_filter(filtered_dict[v[0]][idx], v[1])
                    continue
                filtered_dict[v[0]] = dict_filter(filtered_dict[v[0]], v[1])
            except KeyError:
                continue

    return filtered_dict


def dict_keys_to_camel_case(dictionary: dict, recursive: bool = True) -> dict:
    """Convert keys of a dictionary to camelCase format

    Args:
        dictionary (dict): The dictionary to convert
        recursive (bool, optional): Recursively convert subkeys. Defaults to True.

    Returns:
        dict: Dictionary with keys in camelCase
    """
    camel_dict = {}

    for k in dictionary.keys():
        camel_case_key = ''.join(c.capitalize() for c in k.lower().split('_'))
        lower_camel_case_key = camel_case_key[0].lower() + camel_case_key[1:]
        camel_dict[lower_camel_case_key] = dictionary[k]

        if recursive and isinstance(camel_dict[lower_camel_case_key], dict):
            if isinstance(camel_dict[lower_camel_case_key], list):
                camel_dict[lower_camel_case_key] = [dict_keys_to_camel_case(item) if isinstance(item, dict) else item
                                                    for item in camel_dict[lower_camel_case_key]]
                continue
            if isinstance(camel_dict[lower_camel_case_key], set):
                camel_dict[lower_camel_case_key] = {dict_keys_to_camel_case(item) if isinstance(item, dict) else item
                                                    for item in camel_dict[lower_camel_case_key]}
                continue
            if isinstance(camel_dict[lower_camel_case_key], tuple):
                camel_dict[lower_camel_case_key] = (dict_keys_to_camel_case(item) if isinstance(item, dict) else item
                                                    for item in camel_dict[lower_camel_case_key])
                continue
            if isinstance(camel_dict[lower_camel_case_key], dict):
                camel_dict[lower_camel_case_key] = dict_keys_to_camel_case(camel_dict[lower_camel_case_key])
                continue

    return camel_dict


def dict_keys_to_snake_case(dictionary: dict, recursive: bool = True) -> dict:
    """Convert keys of a dictionary to snake_case format

    Args:
        dictionary (dict): The dictionary to convert
        recursive (bool, optional): Recursively convert subkeys. Defaults to True.

    Returns:
        dict: Dictionary with keys in snake_case format
    """
    snake_dict = {}

    for k in dictionary.keys():
        new_key_name = re.sub('((?<=[a-z0-9])[A-Z]|(?!^)(?<!_)[A-Z](?=[a-z]))', r'_\1', k).lower()
        snake_dict[new_key_name] = dictionary[k]

        if recursive:
            if isinstance(snake_dict[new_key_name], list):
                snake_dict[new_key_name] = [dict_keys_to_snake_case(item) if isinstance(item, dict) else item
                                            for item in snake_dict[new_key_name]]
                continue
            if isinstance(snake_dict[new_key_name], set):
                snake_dict[new_key_name] = {dict_keys_to_snake_case(item) if isinstance(item, dict) else item
                                            for item in snake_dict[new_key_name]}
                continue
            if isinstance(snake_dict[new_key_name], tuple):
                snake_dict[new_key_name] = (dict_keys_to_snake_case(item) if isinstance(item, dict) else item
                                            for item in snake_dict[new_key_name])
                continue
            if isinstance(snake_dict[new_key_name], dict):
                snake_dict[new_key_name] = dict_keys_to_snake_case(snake_dict[new_key_name])
                continue

    return snake_dict


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
    success = response['success'] if 'success' in response else False
    msg = response['msg'] if 'msg' in response else ''

    if not success and msg == '':
        msg = 'Unknown Failure'

    return success, msg
