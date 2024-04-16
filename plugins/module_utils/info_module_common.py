from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import re
from ansible.module_utils.basic import AnsibleModule
try:
    import morpheus_funcs as mf
except ModuleNotFoundError:
    import ansible_collections.morpheus.core.plugins.module_utils.morpheus_funcs as mf


COMMON_ARG_SPEC = {
    'id': {'type': 'int'},
    'name': {'type': 'str'},
    'regex_name': {'type': 'bool', 'default': 'false'}
}

COMMON_MUTUALLY_EXCLUSIVE = [
    ('id', 'name'),
    ('id', 'regex_name')
]


def param_filter(module: AnsibleModule, remove_params: list[str] = None) -> dict:
    """Removes and converts common module parameters to usable API Parameters.

    Args:
        module (AnsibleModule): An instantiated AnsibleModule Class.
        remove_params (list[str], optional): A list of additional module parameters to remove. Defaults to None.

    Returns:
        dict: A dictionary of API Parameters.
    """
    if remove_params is None:
        remove_params = []

    api_params = module.params.copy()

    if all(param in api_params for param in ['labels', 'match_all_labels']):
        api_params['all_labels'] = api_params.pop('labels') if api_params['match_all_labels'] else None

    removals = set(
        [
            'detail',
            'match_all_labels',
            'regex_name'
        ] + remove_params)

    for param in removals:
        if param in api_params:
            del api_params[param]

    if module.params['regex_name']:
        api_params['name'] = None

    return api_params


def response_filter(module: AnsibleModule, response: dict | list, filter_items: dict = None) -> list[dict]:
    """Filters a response based on the supplied dictionary keys.

    Args:
        module (AnsibleModule): An instantiated AnsibleModule Class.
        response (dict | list): The API Response to filter.
        filter_items (dict, optional): Dictionary of keys to filter. Defaults to None.

    Returns:
        list[dict]: A list of filtered API Responses
    """
    if not isinstance(response, list):
        response = [response]

    if module.params['name'] is not None and module.params['regex_name']:
        response = [response_item for response_item in response if re.match(module.params['name'], response_item['name'])]

    if filter_items is not None and module.params['detail'] in filter_items:
        response = [mf.dict_filter(response_item, list(filter_items[module.params['detail']])) for response_item in response]

    return response
