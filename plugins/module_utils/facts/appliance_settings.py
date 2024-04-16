from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.facts.collector import BaseFactCollector
from ansible.module_utils.connection import Connection
try:
    from module_utils.morpheusapi import MorpheusApi
except ModuleNotFoundError:
    from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import MorpheusApi


class MorpheusSettingsFactCollector(BaseFactCollector):
    name = 'settings'
    _fact_ids = set()

    def collect(self, module=None, collected_facts=None):
        facts = {}

        connection = Connection(module._socket_path)
        morph_api = MorpheusApi(connection)

        appliance_settings = morph_api.get_appliance_settings()

        facts['morpheus_settings'] = appliance_settings

        return facts
