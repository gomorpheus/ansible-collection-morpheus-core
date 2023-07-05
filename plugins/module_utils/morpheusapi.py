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


APPLIANCE_SETTINGS_PATH = '/api/appliance-settings'
HEALTH_PATH = '/api/health'
LICENSE_PATH = '/api/license'
MAINTENANCE_MODE_PATH = '{}/maintenance'.format(APPLIANCE_SETTINGS_PATH)


def dict_diff(dict_after: dict, dict_before: dict) -> tuple:
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
    snake_dict = {}

    for k in dictionary.keys():
        new_key_name = re.sub('((?<=[a-z0-9])[A-Z]|(?!^)(?<!_)[A-Z](?=[a-z]))', r'_\1', k).lower()
        snake_dict[new_key_name] = dictionary[k]

        if recursive and isinstance(snake_dict[new_key_name], dict):
            snake_dict[new_key_name] = dict_keys_to_snake_case(snake_dict[new_key_name])

    return snake_dict


def dict_keys_to_camel_case(dictionary: dict, recursive: bool = True) -> dict:
    camel_dict = {}

    for k in dictionary.keys():
        camel_case_key = ''.join(c.capitalize() for c in k.lower().split('_'))
        lower_camel_case_key = camel_case_key[0].lower() + camel_case_key[1:]
        camel_dict[lower_camel_case_key] = dictionary[k]

        if recursive and isinstance(camel_dict[lower_camel_case_key], dict):
            camel_dict[lower_camel_case_key] = dict_keys_to_camel_case(camel_dict[lower_camel_case_key])

    return camel_dict


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

    def get_appliance_settings(self):
        response = self.connection.send_request(path=APPLIANCE_SETTINGS_PATH)
        return self._return_reponse_key(response, 'applianceSettings')

    def set_appliance_settings(self, module_params: dict):
        payload = dict_keys_to_camel_case(
            {k: v for k, v in module_params.items() if v is not None}
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
        path = '{0}?enabled={1}'.format(MAINTENANCE_MODE_PATH, enabled)
        response = self.connection.send_request(path=path, method='POST')
        return self._return_reponse_key(response, '')
