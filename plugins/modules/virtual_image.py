#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: virtual_image
short_description: Manage Morpheus Virtual Images
description:
    - Manage Morpheus Virtual Images.
version_added: 0.6.0
author: James Riach (@McGlovin1337)
options:
    state:
        description:
            - Create, update or remove a Virtual Image.
            - If O(state=absent) and O(filename) is specified then remove the specified file.
        default: present
        choices:
            - absent
            - present
        type: str
    virtual_image_id:
        description:
            - Specify Virtual Image by Id.
        type: int
    name:
        description:
            - Set the Name of the Virtual Image
        type: str
    filename:
        description:
            - Name of uploaded file.
        type: str
    file_url:
        description:
            - URL of file to upload.
        type: str
    labels:
        description:
            - Provide a list of labels to apply to Virtual Image.
        type: list
        elements: str
    image_type:
        description:
            - Set the Image Type code, e.g. vmware
        type: str
    storage_provider_id:
        description:
            - Specify the Storage Provider by Id.
        type: int
    is_cloud_init:
        description:
            - Specify if Cloud Init is enabled.
        type: bool
    user_data:
        description:
            - Cloud Init user data.
        type: str
    install_agent:
        description:
            - Specify if Morpheus Agent should be installed.
        type: bool
    username:
        description:
            - Specify the Username for the Virtual Image.
        type: str
    password:
        description:
            - Specify the Password for the Virtual Image.
        type: str
    ssh_key:
        description:
            - Specify an SSH Key for the Virtual Image.
        type: str
    os_type:
        description:
            - Specify the OS Type code or name.
        type: str
    visibility:
        description:
            - If the Virtual Image should be private or public.
        choices:
            - private
            - public
        type: str
    accounts:
        description:
            - List of Tenants by Id Virtual Image is available to.
        type: list
        elements: int
    is_auto_join_domain:
        description:
            - Whether to Auto Join Domain.
        type: bool
    virtio_supported:
        description:
            - Are Virtio Drivers installed.
        type: bool
    vm_tools_installed:
        description:
            - Are VMware Tools installed.
        type: bool
    trial_version:
        description:
            - Is the Virtual Image a Trial Version.
        type: bool
    is_sysprep:
        description:
            - Specify if Sysprep is Enabled.
        type: bool
    azure_config:
        description:
            - For Azure Virtual Images, specify further options.
        type: dict
        suboptions:
            publisher:
                description:
                    - Name of Publisher in the Azure Marketplace.
                type: str
            offer:
                description:
                    - Name of Offer in the Azure Marketplace.
                type: str
            sku:
                description:
                    - Name of SKU in the Azure Marketplace.
                type: str
            version:
                description:
                    - Name of Version in the Azure Marketplace.
                type: str
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
                type: str
            value:
                description:
                    - The Tag value.
                type: str
extends_documentation_fragment:
    - action_common_attributes
attributes:
    check_mode:
        support: full
    diff_mode:
        support: full
    platform:
        platforms:
            - httpapi
'''

EXAMPLES = r'''
- name: Create Virtual Image and upload File
  morpheus.core.virtual_image:
    state: present
    name: My VMware Image
    image_type: vmware
    is_cloud_init: true
    install_agent: true
    username: root
    password: Password123
    os_type: redhat 8 64bit
    visibility: public
    accounts:
        - 1
    vm_tools_installed: true
    filename: rhel8x64.ova
    file_url: https://my.domain.tld/rhel8x64.ova

- name: Remove Virtual Image by Name
  morpheus.core.virtual_image:
    state: absent
    name: Win2016

- name: Remove Virtual Image by Id
  morpheus.core.virtual_image:
    state: absent
    virtual_image_id: 700

- name: Remove Virtual Image File
  morpheus.core.virtual_image:
    virtual_image_id: 750
    filename: windows_template.ova
    state: absent
'''

RETURN = r'''
virtual_image:
    description:
        - Information about the Virtual Image.
    type: dict
    returned: always
    sample:
        "virtual_image": {
            "accounts": [
                {
                    "id": 1,
                    "name": "TenantA"
                }
            ],
            "config": {
                "disk_ids": []
            },
            "console_keymap": null,
            "date_created": "2023-10-06T23:15:39Z",
            "description": null,
            "external_id": null,
            "fips_enabled": false,
            "guest_console_password": null,
            "guest_console_password_hash": null,
            "guest_console_port": null,
            "guest_console_type": null,
            "guest_console_username": null,
            "id": 700,
            "image_type": "vmware",
            "install_agent": true,
            "is_auto_join_domain": false,
            "is_cloud_init": false,
            "is_force_customization": false,
            "is_sysprep": true,
            "labels": [],
            "last_updated": "2023-10-08T21:15:26Z",
            "linked_clone": false,
            "locations": [],
            "min_disk": null,
            "min_disk_gb": null,
            "min_ram": null,
            "min_ram_gb": null,
            "name": "Windows 2022 Template",
            "network_interfaces": [],
            "os_type": {
                "bit_count": 64,
                "category": "windows",
                "code": "windows.server.2022",
                "description": null,
                "id": 27,
                "name": "windows server 2022",
                "os_family": "windows",
                "os_version": "2022",
                "platform": "windows",
                "vendor": "microsoft"
            },
            "owner_id": 1,
            "raw_size": null,
            "raw_size_gb": null,
            "ssh_key": null,
            "ssh_password": "************",
            "ssh_password_hash": "936a185caaa266bb9cbe981e9e05cb78cd732b0b3280eb944412bb6f8f8f07af",
            "ssh_username": "Administrator",
            "status": "Active",
            "storage_controllers": [],
            "storage_provider": null,
            "system_image": false,
            "tags": [
                {
                    "id": 150,
                    "name": "Bleh",
                    "value": "Blah"
                },
                {
                    "id": 149,
                    "name": "Foo",
                    "value": "Bar"
                }
            ],
            "tenant": {
                "id": 1,
                "name": "TenantA"
            },
            "trial_version": false,
            "uefi": false,
            "user_data": null,
            "user_defined": false,
            "user_uploaded": true,
            "virtio_supported": false,
            "visibility": "public",
            "vm_tools_installed": true,
            "volumes": []
        }
'''

from copy import deepcopy
from hashlib import sha256
from functools import partial
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection

try:
    import module_utils.morpheus_funcs as mf
    from module_utils.morpheusapi import ApiPath, MorpheusApi
except ModuleNotFoundError:
    import ansible_collections.morpheus.core.plugins.module_utils.morpheus_funcs as mf
    from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import ApiPath, MorpheusApi


def create_update_vi(module: AnsibleModule, morpheus_api: MorpheusApi) -> dict:
    """Create or Update a Virtual Image

    Args:
        module (AnsibleModule): Instance of AnsibleModule
        morpheus_api (MorpheusApi): Instance of MorpheusApi

    Returns:
        dict: Returns a result dictionary
    """
    vi_response = {}
    upload_response = False
    diffs = []

    virtual_image = get_vi(module.params, morpheus_api)

    if len(virtual_image) > 1:
        module.fail_json(
            msg='Number of matching Virtual Images exceeded 1, got {0}'.format(len(virtual_image))
        )

    if module.params['password'] is not None and 'ssh_password_hash' in virtual_image:
        pass_hash = sha256(module.params['password'].encode()).hexdigest()

        if pass_hash.decode() == virtual_image['ssh_password_hash']:
            module.params['password'] = None

    api_params, file_params = module_to_api_params(module.params)

    try:
        api_params['virtual_image_id'] = virtual_image[0]['id']
    except (KeyError, IndexError):
        api_params['virtual_image_id'] = None
        virtual_image = []

    action = {
        0: partial(morpheus_api.common_create, path=ApiPath.VIRTUAL_IMAGES_PATH, api_params=api_params),
        1: partial(morpheus_api.common_set, path=ApiPath.VIRTUAL_IMAGES_PATH, item_id=api_params.pop('virtual_image_id'), api_params=api_params),
        3: partial(parse_check_mode, state=module.params['state'], api_params=api_params, virtual_images=virtual_image)
    }.get(len(virtual_image) if not module.check_mode else 3)

    vi_action = action()
    vi_response = mf.dict_keys_to_snake_case(vi_action)

    try:
        vi_id = vi_response['id']
        if module._diff:
            vi_changed, diff = mf.dict_diff(vi_response, virtual_image[0], {'last_updated', 'ssh_password'})
            diffs.append({
                'after_header': '{0} ({1})'.format(vi_response['name'], vi_response['id']),
                'after': '\n'.join([d['after'] for d in diff]),
                'before_header': '{0}, ({1})'.format(virtual_image[0]['name'], virtual_image[0]['id']),
                'before': '\n'.join([d['before'] for d in diff])
            })
        else:
            vi_changed = not mf.dict_compare_equality(virtual_image[0], vi_response, {'last_updated', 'ssh_password'})
    except KeyError:
        vi_id = None
        vi_changed = False
    except IndexError:
        vi_changed = True
        if module._diff:
            diffs.append({
                'after_header': '{0} ({1})'.format(vi_response['name'], vi_response['id']),
                'after': 'Created Virtual Image\n',
                'before_header': '{0}, ({1})'.format(vi_response['name'], vi_response['id']),
                'before': 'Non-Existent Virtual Image\n'
            })

    if file_params['filename'] is not None and vi_id is not None:
        file_params['virtual_image_id'] = vi_id
        upload_action = {
            'False': partial(morpheus_api.upload_virtual_image_file, api_params=file_params),
            'True': partial(parse_check_mode, state=module.params['state'], file_params=file_params, virtual_images=virtual_image)
        }.get(str(module.check_mode))
        exec_upload_action = upload_action()
        upload_response = mf.success_response(exec_upload_action)[0]

    result = {
        'changed': vi_changed is True or upload_response is True,
        'virtual_image': vi_response
    }

    if module._diff:
        result['diff'] = diffs

    return result


def get_vi(module_params: dict, morpheus_api: MorpheusApi) -> list:
    """Retrieve Virtual Images

    Args:
        module_params (dict): Ansible Module Parameters
        morpheus_api (MorpheusApi): Instance of Morpheus Api

    Returns:
        list: List of Virtual Images
    """
    virtual_image = []

    api_params, file_params = module_to_api_params(module_params)

    if module_params['virtual_image_id'] is not None:
        virtual_image = [morpheus_api.get_virtual_images(api_params)]

        if 'id' not in virtual_image[0]:
            virtual_image = []

    if module_params['name'] is not None and len(virtual_image) == 0:
        virtual_image = morpheus_api.get_virtual_images({'virtual_image_id': None, 'name': api_params['name']})

    virtual_image = [mf.dict_keys_to_snake_case(vi) for vi in virtual_image]

    return virtual_image


def module_to_api_params(module_params: dict) -> tuple:
    """Convert Ansible Module Parameters to Morpheus API Parameters

    Args:
        module_params (dict): Ansible Module Parameters

    Returns:
        tuple: General API Params for interacting with Virtual Images,
        and API Parameters for Virtual Image files
    """
    api_params = module_params.copy()

    api_params['ssh_username'] = api_params.pop('username')
    api_params['ssh_password'] = api_params.pop('password')
    if api_params['azure_config'] is not None:
        if api_params['config'] is None:
            api_params['config'] = {}
        api_params['config'].update(api_params.pop('azure_config'))
    del api_params['state']

    file_params = {
        'virtual_image_id': api_params['virtual_image_id'] if api_params['virtual_image_id'] is not None else 0,
        'filename': api_params.pop('filename'),
        'url': api_params.pop('file_url')
    }

    return api_params, file_params


def parse_check_mode(
        state: str, virtual_images: list,
        api_params: dict = None, file_params: dict = None
) -> dict:
    """Parse the module parameters in check_mode

    Args:
        state (str): The requested state
        virtual_images (list): List of Virtual Images
        api_params (dict, optional): Virtual Image API Parameters. Defaults to None.
        file_params (dict, optional): Virtual Image File API Parameters. Defaults to None.

    Returns:
        dict: Result Dictionary
    """
    images = deepcopy(virtual_images)
    result = {}

    if state == 'absent' and (len(images) == 0 or 'id' not in images[0]):
        result = {
            'success': False,
            'msg': 'Virtual Image not found'
        }

        result = {'success': True}

    if api_params is not None and len(result) == 0:
        if 'virtual_image_id' in api_params:
            api_params['id'] = api_params.pop('virtual_image_id')

        if 'accounts' in api_params:
            api_params['accounts'] = [{'id': aid} for aid in api_params['accounts']]

        if 'azure_config' in api_params:
            try:
                api_params['config'].update(api_params.pop('azure_config'))
            except AttributeError:
                api_params['config'] = api_params.pop('azure_config')

        virtual_image = images[0] if len(images) > 0 else {}

        virtual_image.update({k: v for k, v in api_params.items() if v is not None})

        if 'id' not in virtual_image:
            virtual_image['id'] = -1

        result = virtual_image

    if file_params is not None and len(result) == 0 and (len(images) == 0 or 'id' not in images[0]):
        result = {
            'success': False,
            'msg': 'Virtual Image not found'
        }
    else:
        result = {
            'success': True,
        }

    return result


def remove_vi(module: AnsibleModule, morpheus_api: MorpheusApi) -> dict:
    """Remove a Virtual Image or Virtual Image File

    Args:
        module (AnsibleModule): Instance of AnsibleModule
        morpheus_api (MorpheusApi): Instance of MorpheusAPI

    Returns:
        dict: Result Dictionary
    """
    virtual_image = get_vi(module.params, morpheus_api)

    if len(virtual_image) > 1:
        module.fail_json(
            msg='Number of matching Virtual Images exceeded 1, got {0}'.format(len(virtual_image))
        )

    if len(virtual_image) == 0 or 'id' not in virtual_image[0]:
        module.fail_json(
            msg='No Virtual Images matched query parameters'
        )

    api_params, file_params = module_to_api_params(module.params)
    file_params['virtual_image_id'] = virtual_image[0]['id']

    action = {
        0: partial(morpheus_api.common_delete, path=ApiPath.VIRTUAL_IMAGES_PATH, item_id=virtual_image[0]['id']),
        1: partial(morpheus_api.delete_virtual_image_file, file_params),
        2: partial(parse_check_mode, state=module.params['state'], virtual_images=virtual_image)
    }.get(int(module.params['filename'] is not None) if not module.check_mode else 2)

    response = action()

    success, msg = mf.success_response(response)

    result = {
        'changed': success,
        'msg': msg,
        'virtual_image': virtual_image[0]
    }

    if module._diff:
        prepared_action = 'Remove file {0} from Virtual Image \'{1}\'\n'.format(module.params['filename'], virtual_image[0]['name']) \
            if module.params['filename'] is not None \
            else 'Remove Virtual Image \'{0}\' ({1})\n'.format(virtual_image[0]['name'], virtual_image[0]['id'])
        result['diff'] = [{
            'prepared': prepared_action
        }]

    return result


def run_module():
    argument_spec = {
        'state': {'type': 'str', 'choices': ['absent', 'present'], 'default': 'present'},
        'virtual_image_id': {'type': 'int'},
        'name': {'type': 'str'},
        'filename': {'type': 'str'},
        'file_url': {'type': 'str'},
        'labels': {'type': 'list', 'elements': 'str'},
        'image_type': {'type': 'str'},
        'storage_provider_id': {'type': 'int'},
        'is_cloud_init': {'type': 'bool'},
        'user_data': {'type': 'str'},
        'install_agent': {'type': 'bool'},
        'username': {'type': 'str'},
        'password': {'type': 'str', 'no_log': True},
        'ssh_key': {'type': 'str', 'no_log': True},
        'os_type': {'type': 'str'},
        'visibility': {'type': 'str', 'choices': ['private', 'public']},
        'accounts': {'type': 'list', 'elements': 'int'},
        'is_auto_join_domain': {'type': 'bool'},
        'virtio_supported': {'type': 'bool'},
        'vm_tools_installed': {'type': 'bool'},
        'trial_version': {'type': 'bool'},
        'is_sysprep': {'type': 'bool'},
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
        'virtual_image': {}
    }

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True
    )

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    action = {
        'absent': remove_vi,
        'present': create_update_vi
    }.get(module.params['state'])

    action_result = action(module, morpheus_api)

    result.update(action_result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
