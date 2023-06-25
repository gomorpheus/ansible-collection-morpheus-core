from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.basic import to_text
from ansible.errors import AnsibleConnectionFailure, AnsibleOptionsError, AnsibleAuthenticationFailure
from ansible.module_utils.six.moves.urllib.error import HTTPError
from ansible.plugins.httpapi import HttpApiBase
from ansible.module_utils.connection import ConnectionError
import json
import re

DOCUMENTATION = r'''
---
author: James Riach
httpapi : morpheus
short_description: Httpapi Plugin for Morpheus
description:
  - Httpapi plugin to connect to and manage morpheus appliances through the morpheus api
version_added: "0.3.0"
options:
    morpheus_user:
        type: str
        env:
           - name: ANSIBLE_MORPHEUS_USER
        vars:
           - name: ansible_morpheus_user
    morpheus_password:
        type: str
        env:
           - name: ANSIBLE_MORPHEUS_PASSWORD
        vars:
           - name: ansible_morpheus_password
    morpheus_api_token:
        type: str
        env:
            - name: ANSIBLE_MORPHEUS_TOKEN
        vars:
            - name: ansible_morpheus_token
'''

LOGIN_PATH = '/oauth/token?client_id=morph-api&grant_type=password&scope=write'
WHOAMI_PATH = '/api/whoami'

BASE_HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}


class HttpApi(HttpApiBase):
    def __init__(self, connection):
        super(HttpApi, self).__init__(connection)
        self.headers = BASE_HEADERS
        self.access_token = None
        self.refresh_token = None
        self.token_timeout = None

    def handle_httperror(self, exc):
        # Handle 5xx errors
        err_5xx = r'^5\d{2}$'

        handled_error = re.search(err_5xx, str(exc.code))
        if handled_error:
            raise AnsibleConnectionFailure('Could not connect to {0}: {1}'.format(self.connection._url, exc.reason))

        # Handle 401 errors
        if exc.code == 401:
            raise AnsibleAuthenticationFailure('Authentication Failure')

        return False

    def login(self, username, password):
        # The specification of ansible_user results in Ansible attempting a HTTP Basic Auth attempt,
        # this is incompatible with the morpheus login endpoint, therefore we raise an exception
        if username and password:
            raise AnsibleOptionsError('Cannot use ansible_user or ansible_password, refer to plugin documentation')

        api_token = self.get_option('morpheus_api_token')

        if api_token:
            self.access_token = api_token
            self.headers['Authorization'] = 'Bearer {0}'.format(self.access_token)

            # Call the whoami endpoint as a means of checking token validity
            response = self.send_request(path=WHOAMI_PATH)
            return

        username = self.get_option('morpheus_user')
        password = self.get_option('morpheus_password')

        if username and password:
            payload = 'username={0}&password={1}'.format(username, password)
            headers = {
                'Accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            response = self.send_request(payload, path=LOGIN_PATH, method='POST', headers=headers)

            try:
                self.access_token = response['contents']['access_token']
                self.refresh_token = response['contents']['refresh_token']
                self.token_timeout = response['contents']['expires_in']
                self.headers['Authorization'] = 'Bearer {0}'.format(self.access_token)
            except KeyError:
                raise AnsibleAuthenticationFailure('Failed to retrieve an access_token: %s' % response)
            return

        raise AnsibleAuthenticationFailure('Username and Password or API Token required for login')

    def send_request(self, data=None, **kwargs) -> dict:
        path = kwargs.pop('path', None)
        method = kwargs.pop('method', 'GET')
        headers = kwargs.pop('headers', self.headers)

        if headers['Content-Type'] != 'application/x-www-form-urlencoded':
            data = json.dumps(data) if data is not None else None

        try:
            response, response_data = self.connection.send(path, data, method=method, headers=headers, **kwargs)
        except HTTPError as exc:
            try:
                exc_data = self._response_to_json(exc.read())
            except ConnectionError:
                exc_data = exc.read()

            return dict(code=exc.code, contents=exc_data, path=path)

        response_value = self._get_response_value(response_data)
        return dict(code=response.getcode(), contents=self._response_to_json(response_value))

    def _get_response_value(self, response_data):
        return to_text(response_data.getvalue())

    def _response_to_json(self, response_text):
        try:
            return json.loads(response_text) if response_text else {}
        except ValueError:
            raise ConnectionError('Invalid JSON response: %s' % response_text)
