from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.facts.collector import BaseFactCollector
from ansible.module_utils.connection import Connection
from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import MorpheusApi


class MorpheusThreadsFactCollector(BaseFactCollector):
    name = 'threads'
    _fact_ids = set()

    def collect(self, module=None, collected_facts=None):
        facts = {}

        connection = Connection(module._socket_path)
        morph_api = MorpheusApi(connection)

        appliance_health = morph_api.get_appliance_health()

        facts['threads'] = appliance_health['health']['threads']

        return facts
