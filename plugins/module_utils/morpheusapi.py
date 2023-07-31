from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
name: morpheusapi
short_description: Morpheus Api Helper Class
description:
    - Ansible Module Utility for interfacing with the Morpheus API
version_added: 0.3.0
author: James Riach
'''

import re
import urllib.parse


APPLIANCE_SETTINGS_PATH = '/api/appliance-settings'
HEALTH_PATH = '/api/health'
INSTANCES_PATH = '/api/instances'
LICENSE_PATH = '/api/license'
MAINTENANCE_MODE_PATH = '{}/maintenance'.format(APPLIANCE_SETTINGS_PATH)


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
            'after': '{0} = {1}'.format(k, val_a),
            'before': 'Unknown'
        }

        val_b = None
        try:
            val_b = dict_before[k]
        except KeyError:
            diff_list.append(diff)
            continue

        diff['before'] = '{0} = {1}'.format(k, val_b)

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
        for _, v in subkey_filters.items():
            try:
                if isinstance(filtered_dict[v[0]], (list, set, tuple)):
                    for idx, _ in enumerate(filtered_dict[v[0]]):
                        filtered_dict[v[0]][idx] = dict_filter(filtered_dict[v[0]][idx], v[1])
                    continue
                filtered_dict[v[0]] = dict_filter(filtered_dict[v[0]], v[1])
            except KeyError:
                continue

    return filtered_dict


def success_response(response: dict) -> bool:
    try:
        return response['success']
    except KeyError:
        return False


class MorpheusApi():
    def __init__(self, connection) -> None:
        self.connection = connection

    def _return_reponse_key(self, response: dict, key: str):
        if key is None or key == '':
            try:
                return response['contents']
            except KeyError:
                return response

        try:
            return response['contents'][key]
        except KeyError:
            try:
                return response['contents']
            except KeyError:
                return response

    def _build_url(self, path: str, params: list[tuple] = None):
        url_parts = list(urllib.parse.urlparse(path))
        if params is not None:
            url_parts[4] = urllib.parse.urlencode(params)
        return urllib.parse.urlunparse(url_parts)

    def _url_params(self, params: dict):
        args = []

        for k, v in params.items():
            if v is None:
                continue
            if isinstance(v, list):
                for item in v:
                    args.append((k, item))
                continue
            if isinstance(v, bool):
                v = str(v).lower()
            args.append((k, v))

        return args

    def get_appliance_settings(self):
        response = self.connection.send_request(path=APPLIANCE_SETTINGS_PATH)
        return self._return_reponse_key(response, 'applianceSettings')

    def set_appliance_settings(self, api_params: dict):
        payload = dict_keys_to_camel_case(
            {k: v for k, v in api_params.items() if v is not None}
        )
        body = {'applianceSettings': payload}

        response = self.connection.send_request(
            data=body,
            path=APPLIANCE_SETTINGS_PATH,
            method='PUT'
        )
        return self._return_reponse_key(response, '')

    def get_appliance_license(self):
        response = self.connection.send_request(path=LICENSE_PATH)
        return self._return_reponse_key(response, 'license')

    def get_appliance_health(self):
        response = self.connection.send_request(path=HEALTH_PATH)
        return self._return_reponse_key(response, 'health')

    def set_appliance_maintenance_mode(self, enabled: bool):
        params = self._url_params({'enabled': enabled})
        path = self._build_url(MAINTENANCE_MODE_PATH, params)
        response = self.connection.send_request(path=path, method='POST')
        return self._return_reponse_key(response, '')

    def get_instances(self, api_params: dict):
        if api_params['id'] is not None:
            path = '{0}/{1}'.format(INSTANCES_PATH, api_params['id'])
            args = [('details', str(api_params['details']).lower())]
            path = self._build_url(path, args)
            response = self.connection.send_request(path=path)
            return self._return_reponse_key(response, 'instance')

        params = dict_keys_to_camel_case(api_params)
        url_params = self._url_params(params)

        path = self._build_url(INSTANCES_PATH, url_params)

        response = self.connection.send_request(path=path)
        return self._return_reponse_key(response, 'instances')
