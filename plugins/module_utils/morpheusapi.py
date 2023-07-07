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

APPLIANCE_SETTINGS_PATH = '/api/appliance-settings'
HEALTH_PATH = '/api/health'
LICENSE_PATH = '/api/license'


class MorpheusApi():
    def __init__(self, connection) -> None:
        self.connection = connection

    def get_appliance_settings(self):
        response = self.connection.send_request(path=APPLIANCE_SETTINGS_PATH)
        return response['contents']

    def get_appliance_license(self):
        response = self.connection.send_request(path=LICENSE_PATH)
        return response['contents']

    def get_appliance_health(self):
        response = self.connection.send_request(path=HEALTH_PATH)
        return response['contents']
