#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: virtual_image
short_description: Manage Morpheus Virtual Images
description:
    - Manage Morpheus Virtual Images.
version_added: 0.x.x
author: James Riach
options:
    state:
        description:
            - Create, update or remove a Virtual Image.
        default: present
        choices:
            - absent
            - present
        type: string
    virtual_image_id:
        description:
            - Specify Virtual Image by Id.
        type: int
    name:
        description:
            - Set the Name of the Virtual Image
        type: string
    labels:
        description:
            - Provide a list of labels to apply to Virtual Image.
        type: list
        elements: string
    image_type:
        description:
            - Set the Image Type code, e.g. vmware
        type: string
    storage_provider_id:
        description:
            - Specify the Storage Provider by Id.
        type: int
    is_cloud_init:
        description:
            - Specify if Cloud Init is enabled.
        default: false
        type: bool
    user_data:
        description:
            - Cloud Init user data.
        type: string
    install_agent:
        description:
            - Specify if Morpheus Agent should be installed.
        default: true
        type: bool
    username:
        description:
            - Specify the Username for the Virtual Image.
        type: string
    password:
        description:
            - Specify the Password for the Virtual Image.
        type: string
    ssh_key:
        description:
            - Specify an SSH Key for the Virtual Image.
        type: string
    os_type:
        description:
            - Specify the OS Type code or name.
        type: string
    visibility:
        description:
            - If the Virtual Image should be private or public.
        default: private
        choices:
            - private
            - public
        type: string
    accounts:
        description:
            - List of Tenants by Id Virtual Image is available to.
        type: list
        elements: int
    is_auto_join_domain:
        description:
            - Whether to Auto Join Domain.
        default: false
        type: bool
    virtio_supported:
        description:
            - Are Virtio Drivers installed.
        default: false
        type: bool
    vm_tools_installed:
        description:
            - Are VMware Tools installed.
        default: false
        type: bool
    trial_version:
        description:
            - Is the Virtual Image a Trial Version.
        default: false
        type: bool
    is_sysprep:
        description:
            - Specify if Sysprep is Enabled.
        default: false
        type: bool
    azure_config:
        description:
            - For Azure Virtual Images, specify further options.
        type: dict
        suboptions:
            publisher:
                description:
                    - Name of Publisher in the Azure Marketplace.
                type: string
            offer:
                description:
                    - Name of Offer in the Azure Marketplace.
                type: string
            sku:
                description:
                    - Name of SKU in the Azure Marketplace.
                type: string
            version:
                description:
                    - Name of Version in the Azure Marketplace.
                type: string
    config:
        description:
            - Dictionary of Virtual Image configuration.
        type: dict
    tags:
        description:
            - List of Tags to apply.
        type: list
        elements: dict
        suboptions:
            name:
                description:
                    - The Tag name.
                type: string
            value:
                description:
                    - The Tag value.
                type: string
'''

EXAMPLES = r'''
'''

RETURN = r'''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection

try:
    import module_utils.morpheus_funcs as mf
    from module_utils.morpheusapi import MorpheusApi
except ModuleNotFoundError:
    import ansible_collections.morpheus.core.plugins.module_utils.morpheus_funcs as mf
    from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import MorpheusApi


def run_module():
    argument_spec = {
        'state': {'type': 'str', 'choices': ['absent', 'present'], 'default': 'present'},
        'virtual_image_id': {'type': 'int'},
        'name': {'type': 'str'},
        'labels': {'type': 'list', 'elements': 'str'},
        'image_type': {'type': 'str'},
        'storage_provider_id': {'type': 'int'},
        'is_cloud_init': {'type': 'bool', 'default': 'false'},
        'user_data': {'type': 'str'},
        'install_agent': {'type': 'bool', 'default': 'true'},
        'username': {'type': 'str'},
        'password': {'type': 'str', 'no_log': 'true'},
        'ssh_key': {'type': 'str', 'no_log': 'true'},
        'os_type': {'type': 'str'},
        'visibility': {'type': 'str', 'choices': ['private', 'public'], 'default': 'private'},
        'accounts': {'type': 'list', 'elements': 'int'},
        'is_auto_join_domain': {'type': 'bool', 'default': 'false'},
        'virtio_supported': {'type': 'bool', 'default': 'false'},
        'vm_tools_installed': {'type': 'bool', 'default': 'false'},
        'trial_version': {'type': 'bool', 'default': 'false'},
        'is_sysprep': {'type': 'bool', 'default': 'false'},
        'azure_config': {
            'type': 'dict',
            'options': {
                'publisher': {'type': 'str'},
                'offer': {'type': 'str'},
                'sku': {'type': 'str'},
                'version': {'type': 'str'}
            }
        },
        'config': {'type': 'dict'},
        'tags': {
            'type': 'list',
            'elements': 'dict',
            'options': {
                'name': {'type': 'str'},
                'value': {'type': 'str'}
            }
        }
    }

    result = {
        'changed': False,
        'virtual_image': None
    }

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False
    )

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    api_params = module.params.copy()

    api_params['ssh_username'] = api_params.pop('username')
    api_params['ssh_password'] = api_params.pop('password')
    if api_params['azure_config'] is not None:
        if api_params['config'] is None:
            api_params['config'] = {}
        api_params['config'].update(api_params.pop('azure_config'))
    del api_params['state']

    virtual_image = []

    if module.params['virtual_image_id'] is not None:
        virtual_image = [morpheus_api.get_virtual_images(api_params)]

    if module.params['name'] is not None and len(virtual_image) == 0:
        virtual_image = morpheus_api.get_virtual_images({'virtual_image_id': None, 'name': api_params['name']})

    if module.params['state'] == 'absent' and len(virtual_image) > 0:
        response = morpheus_api.delete_virtual_image(virtual_image[0]['id'])
        success, msg = mf.success_response(response)
        result['changed'] = success
        result['msg'] = msg
        module.exit_json(**result)

    if module.params['state'] == 'present':
        api_params['virtual_image_id'] = virtual_image[0]['id'] if len(virtual_image) > 0 else None
        action = morpheus_api.create_virtual_image \
            if len(virtual_image) == 0 else \
            morpheus_api.update_virtual_image
        response = action(api_params)
        result['virtual_image'] = mf.dict_keys_to_snake_case(response)
        result['changed'] = result['virtual_image'] is not None
        module.exit_json(**result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
