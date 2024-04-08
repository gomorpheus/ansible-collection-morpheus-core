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


def param_filter(module: AnsibleModule, remove_params: list[str] = []) -> dict:
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


def response_filter(module: AnsibleModule, response: dict, response_filter: dict = None) -> list[dict]:
    if not isinstance(response, list):
        response = [response]

    if module.params['name'] is not None and module.params['regex_name']:
        response = [response_item for response_item in response if re.match(module.params['name'], response_item['name'])]

    if response_filter is not None and module.params['detail'] in response_filter:
        response = [mf.dict_filter(response_item, list(response_filter[module.params['detail']])) for response_item in response]

    return response
