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

import urllib.parse
from enum import Enum
try:
    import morpheus_funcs as mf
except ModuleNotFoundError:
    import ansible_collections.morpheus.core.plugins.module_utils.morpheus_funcs as mf


class ApiPath(Enum):
    APPLIANCE_SETTINGS_PATH = {
        'path': '/api/appliance-settings',
        'dict': 'applianceSettings'
    }
    CLOUDS = {
        'path': '/api/zones',
        'dict': 'zone',
        'list': 'zones'
    }
    CLOUD_DATASTORES = {
        'path': '/api/zones/{0}/data-stores',
        'dict': 'datastore',
        'list': 'datastores'
    }
    CLOUD_TYPES = {
        'path': '/api/zone-types',
        'dict': 'zoneType',
        'list': 'zoneTypes'
    }
    GROUPS_PATH = {
        'path': '/api/groups',
        'dict': 'group',
        'list': 'groups'
    }
    HEALTH_PATH = {
        'path': '/api/health',
        'dict': 'health'
    }
    INSTANCES_PATH = {
        'path': '/api/instances',
        'dict': 'instance',
        'list': 'instances',
        'action_paths': {
            'backup': '/backup',
            'eject': '/eject'
        }
    }
    INTEGRATIONS_PATH = {
        'path': '/api/integrations',
        'dict': 'integration',
        'list': 'integrations'
    }
    KEY_PAIR_PATH = {
        'path': '/api/key-pairs',
        'dict': 'keyPair',
        'list': 'keyPairs'
    }
    LICENSE_PATH = {
        'path': '/api/license',
        'dict': 'license'
    }
    MAINTENANCE_MODE_PATH = {
        'path': '/api/appliance-settings/maintenance',
    }
    ROLES_PATH = {
        'path': '/api/roles',
        'dict': 'role',
        'list': 'roles'
    }
    SNAPSHOTS_PATH = {
        'path': '/api/snapshots',
        'dict': 'snapshot',
        'list': 'snapshots'
    }
    SSL_CERTIFICATES_PATH = {
        'path': '/api/certificates',
        'dict': 'certificate',
        'list': 'certificates'
    }
    TENANTS_PATH = {
        'path': '/api/accounts',
        'dict': 'account',
        'list': 'accounts'
    }
    VIRTUAL_IMAGES_PATH = {
        'path': '/api/virtual-images',
        'dict': 'virtualImage',
        'list': 'virtualImages'
    }


class MorpheusApi():
    def __init__(self, connection) -> None:
        self.connection = connection

    def _build_url(self, path: str, params: list[tuple] = None):
        url_parts = list(urllib.parse.urlparse(path))
        if params is not None:
            url_parts[4] = urllib.parse.urlencode(params)
        return urllib.parse.urlunparse(url_parts)

    def _get_object(self, api_path: str, api_params: dict, max_param: bool = False):
        params = mf.dict_keys_to_camel_case(api_params)
        if max_param:
            params['max'] = -1
        url_params = self._url_params(params)
        path = self._build_url(api_path, url_params)

        return self.connection.send_request(path=path)

    def _get_object_by_id(self, api_path: str, obj_id: int, url_params: dict = None):
        path = '{0}/{1}'.format(api_path, obj_id)

        if url_params is not None:
            url_params = self._url_params(url_params)
            path = self._build_url(path, url_params)

        return self.connection.send_request(path=path)

    def _payload_from_params(self, params: dict):
        payload = mf.dict_keys_to_camel_case(
            {k: v for k, v in params.items() if v is not None}
        )

        return payload

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

    def create_key_pair(self, api_params: dict):
        payload = self._payload_from_params(api_params)
        body = {'keyPair': payload}

        path = ApiPath.KEY_PAIR_PATH.value['path']

        if len(body['keyPair']) == 1 and bool(api_params['name']):
            path = '{0}/generate'.format(ApiPath.KEY_PAIR_PATH.value['path'])

        response = self.connection.send_request(
            data=body,
            path=path,
            method='POST'
        )
        return self._return_reponse_key(response, '')

    def common_create(self, path: ApiPath, api_params: dict):
        payload = self._payload_from_params(api_params)
        body = {path.value['dict']: payload}

        response = self.connection.send_request(
            data=body,
            path=path.value['path'],
            method='POST'
        )
        return self._return_reponse_key(response, path.value['dict'])

    def common_delete(self, path: ApiPath, item_id: int, api_params: dict = None):
        path = '{0}/{1}'.format(path.value['path'], item_id)

        if api_params is not None:
            params = mf.dict_keys_to_camel_case(api_params)
            url_params = self._url_params(params)
            path = self._build_url(path, url_params)

        response = self.connection.send_request(
            path=path,
            method='DELETE'
        )
        return self._return_reponse_key(response, '')

    def common_get(self, path: ApiPath, api_params: dict):
        if api_params['id'] is not None:
            response = self._get_object_by_id(path.value['path'], api_params['id'])
            return self._return_reponse_key(response, path.value['dict'])

        response = self._get_object(path.value['path'], api_params, True)
        return self._return_reponse_key(response, path.value['list'])

    def common_set(self, path: ApiPath, item_id: int, api_params: dict):
        api_path = '{0}/{1}'.format(path.value['path'], item_id)

        payload = self._payload_from_params(api_params)
        body = {path.value['dict']: payload}

        response = self.connection.send_request(
            data=body,
            path=api_path,
            method='PUT'
        )
        return self._return_reponse_key(response, path.value['dict'])

    def delete_all_instance_snapshots(self, instance_id: int):
        path = '{0}/{1}/delete-all-snapshots'.format(ApiPath.INSTANCES_PATH.value['path'], instance_id)
        response = self.connection.send_request(path=path, method='DELETE')
        return self._return_reponse_key(response, '')

    def delete_virtual_image_file(self, api_params: dict):
        path = '{0}/{1}/files'.format(ApiPath.VIRTUAL_IMAGES_PATH.value['path'], api_params['virtual_image_id'])

        url_params = self._url_params({'filename': api_params['filename']})
        path = self._build_url(path, url_params)

        response = self.connection.send_request(path=path, method='DELETE')

        return self._return_reponse_key(response, '')

    def get_appliance_health(self):
        response = self.connection.send_request(path=ApiPath.HEALTH_PATH.value['path'])
        return self._return_reponse_key(response, 'health')

    def get_appliance_license(self):
        response = self.connection.send_request(path=ApiPath.LICENSE_PATH.value['path'])
        return self._return_reponse_key(response, 'license')

    def get_appliance_settings(self):
        response = self.connection.send_request(path=ApiPath.APPLIANCE_SETTINGS_PATH.value['path'])
        return self._return_reponse_key(response, 'applianceSettings')

    def get_cloud_datastores(self, api_params: dict):
        zone_id = api_params.pop('zone_id')

        if api_params['id'] is not None:
            response = self._get_object_by_id(ApiPath.CLOUD_DATASTORES.value['path'].format(zone_id), api_params['id'])
            return self._return_reponse_key(response, 'datastore')

        response = self._get_object(ApiPath.CLOUD_DATASTORES.value['path'].format(zone_id), api_params, True)
        return self._return_reponse_key(response, 'datastores')

    def get_instances(self, api_params: dict):
        if api_params['id'] is not None:
            path = '{0}/{1}'.format(ApiPath.INSTANCES_PATH.value['path'], api_params['id'])
            try:
                detail = str(api_params['details']).lower()
            except KeyError:
                detail = 'false'
            params = self._url_params({
                'details': detail
            })
            path = self._build_url(path, params)
            response = self.connection.send_request(path=path)
            return self._return_reponse_key(response, 'instance')

        params = mf.dict_keys_to_camel_case(api_params)
        params['max'] = -1
        url_params = self._url_params(params)

        path = self._build_url(ApiPath.INSTANCES_PATH.value['path'], url_params)

        response = self.connection.send_request(path=path)
        return self._return_reponse_key(response, 'instances')

    def get_instance_snapshots(self, instance_id: int):
        path = '{0}/{1}/snapshots'.format(ApiPath.INSTANCES_PATH.value['path'], instance_id)
        response = self.connection.send_request(path=path)
        return self._return_reponse_key(response, 'snapshots')

    def get_integrations(self, api_params: dict):
        if api_params['id'] is not None:
            response = self._get_object_by_id(ApiPath.INTEGRATIONS_PATH.value['path'], api_params['id'])
            return self._return_reponse_key(response, 'integration')

        # max = -1 doesnt' seem to work on this endpoint
        api_params['max'] = 10000
        response = self._get_object(ApiPath.INTEGRATIONS_PATH.value['path'], api_params)
        return self._return_reponse_key(response, 'integrations')

    def get_virtual_images(self, api_params: dict):
        params = mf.dict_keys_to_camel_case(api_params)
        params['max'] = -1

        if params['virtualImageId'] is not None:
            path = '{0}/{1}'.format(ApiPath.VIRTUAL_IMAGES_PATH.value['path'], params['virtualImageId'])
            response = self.connection.send_request(path=path)
            return self._return_reponse_key(response, 'virtualImage')

        url_params = self._url_params(params)
        path = self._build_url(ApiPath.VIRTUAL_IMAGES_PATH.value['path'], url_params)

        response = self.connection.send_request(path=path)
        return self._return_reponse_key(response, 'virtualImages')

    def instance_action(self, action: str, item_id: int):
        path = '{0}/{1}/{2}'.format(ApiPath.INSTANCES_PATH.value['path'], item_id, action)
        response = self.connection.send_request(path=path, method='PUT')
        return self._return_reponse_key(response, '' if action in ['lock', 'unlock'] else 'results')

    def refresh_cloud(self, api_params: dict):
        path = '{0}/{1}/refresh'.format(ApiPath.CLOUDS.value['path'], api_params.pop('id'))
        body = self._payload_from_params(api_params)

        response = self.connection.send_request(
            data=body,
            path=path,
            method='POST'
        )

        return self._return_reponse_key(response, '')

    def set_appliance_maintenance_mode(self, enabled: bool):
        params = self._url_params({'enabled': enabled})
        path = self._build_url(ApiPath.MAINTENANCE_MODE_PATH.value['path'], params)
        response = self.connection.send_request(path=path, method='POST')
        return self._return_reponse_key(response, '')

    def set_appliance_settings(self, api_params: dict):
        payload = self._payload_from_params(api_params)
        body = {'applianceSettings': payload}

        response = self.connection.send_request(
            data=body,
            path=ApiPath.APPLIANCE_SETTINGS_PATH.value['path'],
            method='PUT'
        )
        return self._return_reponse_key(response, '')

    def set_cloud_datastore(self, api_params: dict):
        path = '{0}/{1}'.format(ApiPath.CLOUD_DATASTORES.value['path'].format(api_params.pop('zone_id')), api_params.pop('id'))
        payload = self._payload_from_params(api_params)
        body = {'datastore': payload}

        response = self.connection.send_request(
            data=body,
            path=path,
            method='PUT'
        )

        return self._return_reponse_key(response, 'datastore')

    def snapshot_instance(self, api_params: dict):
        path = '{0}/{1}/snapshot'.format(ApiPath.INSTANCES_PATH.value['path'], api_params.pop('id'))
        payload = self._payload_from_params(api_params)
        body = {'snapshot': payload}

        response = self.connection.send_request(
            data=body,
            path=path,
            method='PUT'
        )

        return self._return_reponse_key(response, '')

    def snapshot_revert(self, instance_id: int, snapshot_id: int):
        path = '{0}/{1}/revert-snapshot/{2}'.format(ApiPath.INSTANCES_PATH.value['path'], instance_id, snapshot_id)
        response = self.connection.send_request(path=path, method='PUT')
        return self._return_reponse_key(response, '')

    def update_cloud_logo(self, api_params: dict):
        path = '{0}/{1}/update-logo'.format(ApiPath.CLOUDS.value['path'], api_params['id'])

        file_data = []

        if api_params['logo'] is not None:
            file_data.append(
                {
                    'name': 'logo',
                    'file_path': api_params['logo']
                }
            )

        if api_params['dark_logo'] is not None:
            file_data.append(
                {
                    'name': 'darkLogo',
                    'file_path': api_params['dark_logo']
                }
            )

        response = self.connection.multipart_upload(
            uri_path=path,
            file_data=file_data
        )

        return self._return_reponse_key(response, '')

    def update_group_zones(self, api_params: dict):
        path = '{0}/{1}/update-zones'.format(ApiPath.GROUPS_PATH.value['path'], api_params.pop('id'))

        payload = self._payload_from_params(api_params)
        body = {'group': payload}

        response = self.connection.send_request(
            data=body,
            path=path,
            method='PUT'
        )
        return self._return_reponse_key(response, '')

    def upload_virtual_image_file(self, api_params: dict):
        path = '{0}/{1}/upload'.format(ApiPath.VIRTUAL_IMAGES_PATH.value['path'], api_params.pop('virtual_image_id'))

        payload = mf.dict_keys_to_camel_case(
            api_params
        )

        response = {}

        if payload['url'] is not None:
            url_params = self._url_params(api_params)
            path = self._build_url(path, url_params)
            response = self.connection.send_request(
                path=path,
                method='POST'
            )

        return self._return_reponse_key(response, '')
