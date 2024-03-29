#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: virtual_image_info
short_description: Gather Virtual Image information
description:
    - Gathers information about Virtual Images.
version_added: 0.6.0
author: James Riach
options:
    virtual_image_id:
        description:
            - Return info for specic Virtual Image by Id
        type: int
    name:
        description:
            - Return info for Virtual Image by Name
        type: string
    regex_name:
        description:
            - Treat name parameter as a Regular Expression
        default: false
        type: bool
    filter_type:
        description:
            - Filter Virtual Images by type
        default: all
        choices:
            - all
            - synced
            - system
            - user
        type: string
    image_type:
        description:
            - Filter by image type code, e.g. vmware, ami
        type: string
    labels:
        description:
            - Filter by matching labels
        type: list
        elements: string
    match_all_labels:
        description:
            - If true, match all specified labels
        default: false
        type: bool
    detail:
        description:
            - Level of detail returned about Virtual Images
        default: summary
        choices:
            - full
            - summary
        type: string
'''

EXAMPLES = r'''
- name: Get Virtual Image by Id
  morpheus.core.virtual_image_info:
    virtual_image_id: 500

- name: Get Virtual Image by Name
  morpheus.core.virtual_image_info:
    name: redhat_image

- name: Get Virtual Images by Regex Match
  morpheus.core.virtual_image_info:
    name: ^.*$
    regex_name: true

- name: Get Synced VMware Virtual Images
  morpheus.core.virtual_image_info:
    filter_type: synced
    image_type: vmware

- name: Get User Virtual Images
  morpheus.core.virtual_image_info:
    filter_type: user
'''

RETURN = r'''
virtual_images:
    description:
        - List of Virtual Images
    returned: always
    sample:
        "virtual_images": [
            {
                "date_created": "2023-01-01T00:00:00Z",
                "description": null,
                "id": 500,
                "image_type": "vmdk",
                "install_agent": false,
                "is_cloud_init": false,
                "is_force_customization": false,
                "labels": [],
                "locations": [],
                "min_disk_gb": null,
                "min_ram_gb": 4,
                "name": "My User Image",
                "os_type": {
                    "bit_count": 64,
                    "category": "suse",
                    "code": "suse.11.64",
                    "description": null,
                    "id": 92,
                    "name": "suse enterprise 11 64-bit",
                    "os_family": "suse",
                    "os_version": "11",
                    "platform": "linux",
                    "vendor": "suse"
                },
                "raw_size_gb": null,
                "ssh_username": null,
                "status": "queued",
                "vm_tools_installed": true,
                "volumes": []
            }
        ]
'''

import re
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection

try:
    import module_utils.morpheus_funcs as mf
    from module_utils.morpheusapi import MorpheusApi
except ModuleNotFoundError:
    import ansible_collections.morpheus.core.plugins.module_utils.morpheus_funcs as mf
    from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import MorpheusApi


API_FILTER_KEYS = {
    'summary': (
        'id',
        'name',
        'description',
        'imageType',
        'osType',
        'minRamGB',
        'minDiskGB',
        'rawSizeGB',
        'vmToolsInstalled',
        ('volumes', ['name', 'resizeable', 'rootVolume', 'size']),
        'labels',
        ('locations', ['cloud', 'id', 'imageName']),
        'status',
        'sshUsername',
        'installAgent',
        'isCloudInit',
        'isForceCustomization',
        'dateCreated'
    )
}


def run_module():
    argument_spec = {
        'virtual_image_id': {'type': 'int'},
        'name': {'type': 'str'},
        'regex_name': {'type': 'bool', 'default': 'false'},
        'filter_type': {'type': 'str', 'choices': ['all', 'synced', 'system', 'user'], 'default': 'all'},
        'image_type': {'type': 'str'},
        'labels': {'type': 'list', 'elements': 'str'},
        'match_all_labels': {'type': 'bool', 'default': 'false'},
        'detail': {'type': 'str', 'choices': ['full', 'summary'], 'default': 'summary'}
    }

    mutually_exclusive = {
        ('virtual_image_id', 'name'),
        ('virtual_image_id', 'regex_name'),
        ('virtual_image_id', 'filter_type'),
        ('virtual_image_id', 'image_type'),
        ('virtual_image_id', 'labels'),
        ('virtual_image_id', 'match_all_labels')
    }

    result = {
        'changed': False,
        'virtual_images': []
    }

    module = AnsibleModule(
        argument_spec=argument_spec,
        mutually_exclusive=mutually_exclusive,
        supports_check_mode=True
    )

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    api_params = module.params.copy()

    if module.params['regex_name']:
        api_params['name'] = None
    api_params['all_labels'] = api_params.pop('labels') if module.params['match_all_labels'] else None

    for k in ['detail', 'match_all_labels', 'regex_name']:
        del api_params[k]

    response = morpheus_api.get_virtual_images(api_params)

    if not isinstance(response, list):
        response = [response]

    if module.params['name'] is not None and module.params['regex_name']:
        response = [image for image in response if re.match(module.params['name'], image['name'])]

    if module.params['detail'] != 'full':
        filter_keys = API_FILTER_KEYS[module.params['detail']]

        filtered_info = [mf.dict_filter(image, list(filter_keys)) for image in response]
        result['virtual_images'] = [mf.dict_keys_to_snake_case(image) for image in filtered_info]

        module.exit_json(**result)

    result['virtual_images'] = [mf.dict_keys_to_snake_case(response_item) for response_item in response]

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
