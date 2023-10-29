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

import binascii
import base64
import urllib.parse
try:
    import morpheus_funcs as mf
except ModuleNotFoundError:
    import ansible_collections.morpheus.core.plugins.module_utils.morpheus_funcs as mf


APPLIANCE_SETTINGS_PATH = '/api/appliance-settings'
HEALTH_PATH = '/api/health'
INSTANCES_PATH = '/api/instances'
KEY_PAIR_PATH = '/api/key-pairs'
LICENSE_PATH = '/api/license'
MAINTENANCE_MODE_PATH = '{}/maintenance'.format(APPLIANCE_SETTINGS_PATH)
SNAPSHOTS_PATH = '/api/snapshots'
SSL_CERTIFICATES_PATH = '/api/certificates'
VIRTUAL_IMAGES_PATH = '/api/virtual-images'


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

    def _payload_from_params(self, params: dict):
        payload = mf.dict_keys_to_camel_case(
            {k: v for k, v in params.items() if v is not None}
        )

        return payload

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

        path = KEY_PAIR_PATH

        if len(body['keyPair']) == 1 and bool(api_params['name']):
            path = '{0}/generate'.format(KEY_PAIR_PATH)

        response = self.connection.send_request(
            data=body,
            path=path,
            method='POST'
        )
        return self._return_reponse_key(response, '')

    def create_ssl_certificate(self, api_params: dict):
        payload = self._payload_from_params(api_params)
        body = {'certificate': payload}

        response = self.connection.send_request(
            data=body,
            path=SSL_CERTIFICATES_PATH,
            method='POST'
        )
        return self._return_reponse_key(response, 'certificate')

    def create_virtual_image(self, api_params: dict):
        payload = self._payload_from_params(api_params)
        body = {'virtualImage': payload}

        response = self.connection.send_request(
            data=body,
            path=VIRTUAL_IMAGES_PATH,
            method='POST'
        )
        return self._return_reponse_key(response, 'virtualImage')

    def get_appliance_settings(self):
        response = self.connection.send_request(path=APPLIANCE_SETTINGS_PATH)
        return self._return_reponse_key(response, 'applianceSettings')

    def set_appliance_settings(self, api_params: dict):
        payload = self._payload_from_params(api_params)
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

    def get_instance_snapshots(self, instance_id: int):
        path = '{0}/{1}/snapshots'.format(INSTANCES_PATH, instance_id)
        response = self.connection.send_request(path=path)
        return self._return_reponse_key(response, 'snapshots')

    def set_appliance_maintenance_mode(self, enabled: bool):
        params = self._url_params({'enabled': enabled})
        path = self._build_url(MAINTENANCE_MODE_PATH, params)
        response = self.connection.send_request(path=path, method='POST')
        return self._return_reponse_key(response, '')

    def get_instances(self, api_params: dict):
        if api_params['id'] is not None:
            path = '{0}/{1}'.format(INSTANCES_PATH, api_params['id'])
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
        url_params = self._url_params(params)

        path = self._build_url(INSTANCES_PATH, url_params)

        response = self.connection.send_request(path=path)
        return self._return_reponse_key(response, 'instances')

    def get_key_pairs(self, api_params: dict):
        params = mf.dict_keys_to_camel_case(api_params)

        if params['id'] is not None:
            path = '{0}/{1}'.format(KEY_PAIR_PATH, params['id'])
            response = self.connection.send_request(path=path)
            return self._return_reponse_key(response, 'keyPair')

        url_params = self._url_params(params)
        path = self._build_url(KEY_PAIR_PATH, url_params)

        response = self.connection.send_request(path=path)
        return self._return_reponse_key(response, 'keyPairs')

    def get_ssl_certificates(self, api_params: dict):
        params = mf.dict_keys_to_camel_case(api_params)

        if params['id'] is not None:
            path = '{0}/{1}'.format(SSL_CERTIFICATES_PATH, params['id'])
            response = self.connection.send_request(path=path)
            return self._return_reponse_key(response, 'certificate')

        url_params = self._url_params(params)
        path = self._build_url(SSL_CERTIFICATES_PATH, url_params)

        response = self.connection.send_request(path=path)
        return self._return_reponse_key(response, 'certificates')

    def get_virtual_images(self, api_params: dict):
        params = mf.dict_keys_to_camel_case(api_params)
        params['max'] = -1

        if params['virtualImageId'] is not None:
            path = '{0}/{1}'.format(VIRTUAL_IMAGES_PATH, params['virtualImageId'])
            response = self.connection.send_request(path=path)
            return self._return_reponse_key(response, 'virtualImage')

        url_params = self._url_params(params)
        path = self._build_url(VIRTUAL_IMAGES_PATH, url_params)

        response = self.connection.send_request(path=path)
        return self._return_reponse_key(response, 'virtualImages')

    def backup_instance(self, instance_id: int):
        path = '{0}/{1}/backup'.format(INSTANCES_PATH, instance_id)
        response = self.connection.send_request(path=path, method='PUT')
        return self._return_reponse_key(response, 'results')

    def delete_all_instance_snapshots(self, instance_id: int):
        path = '{0}/{1}/delete-all-snapshots'.format(INSTANCES_PATH, instance_id)
        response = self.connection.send_request(path=path, method='DELETE')
        return self._return_reponse_key(response, '')

    def delete_instance(self, instance_id: int, api_params: dict):
        path = '{0}/{1}'.format(INSTANCES_PATH, instance_id)
        params = mf.dict_keys_to_camel_case(api_params)
        url_params = self._url_params(params)
        path = self._build_url(path, url_params)
        response = self.connection.send_request(path=path, method='DELETE')
        return self._return_reponse_key(response, 'results')

    def delete_key_pair(self, key_pair_id: int):
        path = '{0}/{1}'.format(KEY_PAIR_PATH, key_pair_id)
        response = self.connection.send_request(path=path, method='DELETE')
        return self._return_reponse_key(response, '')

    def delete_snapshot(self, snapshot_id: int):
        path = '{0}/{1}'.format(SNAPSHOTS_PATH, snapshot_id)
        response = self.connection.send_request(path=path, method='DELETE')
        return self._return_reponse_key(response, '')

    def delete_ssl_certificate(self, cert_id: int):
        path = '{0}/{1}'.format(SSL_CERTIFICATES_PATH, cert_id)
        response = self.connection.send_request(path=path, method='DELETE')
        return self._return_reponse_key(response, '')

    def delete_virtual_image(self, virtual_image_id: int):
        path = '{0}/{1}'.format(VIRTUAL_IMAGES_PATH, virtual_image_id)

        response = self.connection.send_request(path=path, method='DELETE')

        return self._return_reponse_key(response, '')

    def delete_virtual_image_file(self, api_params: dict):
        path = '{0}/{1}/files'.format(VIRTUAL_IMAGES_PATH, api_params['virtual_image_id'])

        url_params = self._url_params({'filename': api_params['filename']})
        path = self._build_url(path, url_params)

        response = self.connection.send_request(path=path, method='DELETE')

        return self._return_reponse_key(response, '')

    def eject_instance(self, instance_id: int):
        path = '{0}/{1}/eject'.format(INSTANCES_PATH, instance_id)
        response = self.connection.send_request(path=path, method='PUT')
        return self._return_reponse_key(response, 'results')

    def lock_instance(self, instance_id: int):
        path = '{0}/{1}/lock'.format(INSTANCES_PATH, instance_id)
        response = self.connection.send_request(path=path, method='PUT')
        return self._return_reponse_key(response, '')

    def restart_instance(self, instance_id: int):
        path = '{0}/{1}/restart'.format(INSTANCES_PATH, instance_id)
        response = self.connection.send_request(path=path, method='PUT')
        return self._return_reponse_key(response, 'results')

    def snapshot_instance(self, api_params: dict):
        path = '{0}/{1}/snapshot'.format(INSTANCES_PATH, api_params.pop('id'))
        payload = self._payload_from_params(api_params)
        body = {'snapshot': payload}

        response = self.connection.send_request(
            data=body,
            path=path,
            method='PUT'
        )

        return self._return_reponse_key(response, '')

    def snapshot_revert(self, instance_id: int, snapshot_id: int):
        path = '{0}/{1}/revert-snapshot/{2}'.format(INSTANCES_PATH, instance_id, snapshot_id)
        response = self.connection.send_request(path=path, method='PUT')
        return self._return_reponse_key(response, '')

    def start_instance(self, instance_id: int):
        path = '{0}/{1}/start'.format(INSTANCES_PATH, instance_id)
        response = self.connection.send_request(path=path, method='PUT')
        return self._return_reponse_key(response, 'results')

    def stop_instance(self, instance_id: int):
        path = '{0}/{1}/stop'.format(INSTANCES_PATH, instance_id)
        response = self.connection.send_request(path=path, method='PUT')
        return self._return_reponse_key(response, 'results')

    def suspend_instance(self, instance_id: int):
        path = '{0}/{1}/suspend'.format(INSTANCES_PATH, instance_id)
        response = self.connection.send_request(path=path, method='PUT')
        return self._return_reponse_key(response, 'results')

    def update_ssl_certificate(self, api_params: dict):
        path = '{0}/{1}'.format(SSL_CERTIFICATES_PATH, api_params.pop('id'))

        payload = self._payload_from_params(api_params)
        body = {'certificate': payload}

        response = self.connection.send_request(
            data=body,
            path=path,
            method='PUT'
        )
        return self._return_reponse_key(response, 'certificate')

    def update_virtual_image(self, api_params: dict):
        path = '{0}/{1}'.format(VIRTUAL_IMAGES_PATH, api_params.pop('virtual_image_id'))

        payload = self._payload_from_params(api_params)
        body = {'virtualImage': payload}

        response = self.connection.send_request(
            data=body,
            path=path,
            method='PUT'
        )
        return self._return_reponse_key(response, 'virtualImage')

    def upload_virtual_image_file(self, api_params: dict):
        path = '{0}/{1}/upload'.format(VIRTUAL_IMAGES_PATH, api_params.pop('virtual_image_id'))

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/octet-stream'
        }

        orig_headers = self.connection.headers
        self.connection.headers = headers

        payload = mf.dict_keys_to_camel_case(
            api_params
        )

        response = {}

        if payload['url'] is not None:
            del payload['file']
            url_params = self._url_params(api_params)
            path = self._build_url(path, url_params)
            response = self.connection.send_request(
                path=path,
                method='POST'
            )
        elif payload['file'] is not None:
            del payload['url']
            with open(payload['file'], 'rb') as vi_file:
                file_name = vi_file.name
                b64_file = base64.b64encode(vi_file.read())
                b64_ascii = binascii.a2b_base64(b64_file)

            body = 'data:application/octet-stream;name={0};base64,{1}'.format(file_name, b64_ascii)

            url_params = self._url_params(payload)
            path = self._build_url(path, url_params)

            response = self.connection.send_request(
                path=path,
                data=body,
                method='POST'
            )

        self.connection.headers = orig_headers
        return self._return_reponse_key(response, '')

    def unlock_instance(self, instance_id: int):
        path = '{0}/{1}/unlock'.format(INSTANCES_PATH, instance_id)
        response = self.connection.send_request(path=path, method='PUT')
        return self._return_reponse_key(response, '')
