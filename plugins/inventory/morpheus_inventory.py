# morpheus_inventory.py

from __future__ import (absolute_import, division, print_function)
import requests
import os
import yaml
import sys
from builtins import str
from packaging import version
from ansible.plugins.inventory import BaseInventoryPlugin
from ansible.errors import AnsibleParserError

__metaclass__ = type

DOCUMENTATION = r'''
    name: morpheus_inventory
    plugin_type: inventory
    short_description: Returns Ansible inventory from Morpheus
    description: Returns Ansible inventory from Morpheus
    options:
        plugin:
            description: Morpheus Inventory
            required: true
            choices: ['morpheus_inventory', 'morpheus.core.morpheus_inventory']
        groups:
            description: whatever
            required: true
        searchtype:
            description: Search type
            required: false
        searchstring:
            description: Search term
            required: false
        morpheus_url:
            description: Morpheus URL
            required: false
        morpheus_api_key:
            description: Morpheus API Key - Can be a vault encrypted string
            required: false
'''


class InventoryModule(BaseInventoryPlugin):
    NAME = 'morpheus_inventory'

    def __init__(self):
        self.morpheus_env = False
        self.morpheus_url = ""
        self.morpheus_api = ""
        self.morpheus_token = ""
        self.morpheus_opt_args = {
            'token': "",
            'sslverify': True
        }
        self.morpheus_version = None
        self.morpheus_oldmetadata = False
        self.morpheus_simulate = False
        self.morpheus_simulate_agent = False
        self.extravars = None
        self.workspace = ""
        self.groups = None

    def _set_version_from_morpheus(self):

        headers = {'Authorization': "BEARER %s" % self.morpheus_token,
                   "Content-Type": "application/json"}
        method = "get"
        verify = self.morpheus_opt_args['sslverify']
        versionapi = self.morpheus_api + "/ping"
        v = getattr(requests, method)(versionapi, headers=headers, verify=verify)
        returned_v = v.json()
        self.morpheus_version = returned_v['buildVersion']

    def _set_morpheus_oldmetadata(self):
        if version.parse(self.morpheus_version) < version.parse("4.2.5"):
            self.morpheus_oldmetadata = True
        if (version.parse(self.morpheus_version) >= version.parse("5.0")) and (version.parse(self.morpheus_version) < version.parse("5.2.1")):
            self.morpheus_oldmetadata = True

    def _get_data_from_morpheus(self, searchtype, searchstring=None):
        headers = {'Authorization': "BEARER %s" % self.morpheus_token,
                   "Content-Type": "application/json"}
        method = "get"
        verify = self.morpheus_opt_args['sslverify']

        if searchtype in ["label", "name", "tag"]:
            path = "/instances?max=-1"
        elif searchtype == "app":
            path = "/apps?max=-1"
        elif searchtype == "cloud":
            cloudid = None
            if searchstring is None:
                raise AnsibleParserError("Searchtype cloud must have a searchstring")
            # Python 2 fix
            cloud_is_numeric = True
            if sys.version_info[0] == 2:
                if str(searchstring).isnumeric() is not True:
                    cloud_is_numeric = False
            if sys.version_info[0] == 3:
                if str(searchstring).isnumeric() is not True:
                    cloud_is_numeric = False

            if not cloud_is_numeric:
                cloudurl = self.morpheus_api + "/zones?max=-1"
                cloudr = getattr(requests, method)(cloudurl, headers=headers, verify=verify)
                cloudoutput = cloudr.json()
                if 'error' in cloudoutput.keys():
                    raise AnsibleParserError("Error in Morpheus API call: %s" % cloudoutput['error'])
                for c in cloudoutput['zones']:
                    if c['code'] == searchstring:
                        cloudid = c['id']
                        break
                if cloudid is None:
                    raise AnsibleParserError("Could not find a cloud with code: %s" % searchstring)
            else:
                cloudid = searchstring
            path = "/instances?zoneId=%s&max=-1" % cloudid
        url = self.morpheus_api + path
        r = getattr(requests, method)(url, headers=headers, verify=verify)
        if 'error' in r.json().keys():
            raise AnsibleParserError("Error in Morpheus API call: %s" % r.json()['error'])
        return r.json()

    def _get_containers_from_morpheus(self, instanceid):
        headers = {'Authorization': "BEARER %s" % self.morpheus_token,
                   "Content-Type": "application/json"}

        path = "/instances/%s/containers?max=-1" % instanceid
        url = self.morpheus_api + path
        method = "get"
        verify = self.morpheus_opt_args['sslverify']
        r = getattr(requests, method)(url, headers=headers, verify=verify)
        return r.json()

    def _set_morpheus_connection_vars(self, hostname, ip, containerid, noagent=False, platform=None):
        if noagent == "null" or noagent is False:
            agent = True
        else:
            agent = False
        self.inventory.set_variable(hostname, 'ansible_host', ip)
        self.inventory.set_variable(hostname, 'ansible_user', 'morpheus-node')
        self.inventory.set_variable(hostname, 'ansible_ssh_private_key_file', self.morpheusprivatekeyfile)
        self.inventory.set_variable(hostname, 'ansible_morpheus_container_id', containerid)
        if agent:
            if platform == "windows":
                self.inventory.set_variable(hostname, 'ansible_connection', 'morpheus_win')
            else:
                self.inventory.set_variable(hostname, 'ansible_connection', 'morpheus')

    def _add_morpheus_instance_cloud_bytag(self, instance):
        if self.morpheus_oldmetadata:
            for tag in instance['metadata']:
                if str(tag['name']).startswith("Morpheus "):
                    continue
                group = "%s_%s" % (tag['name'], tag['value'])
                self.inventory.add_group(group)
                self._add_morpheus_instance(group, instance)
        else:
            for tag in instance['tags']:
                group = "%s_%s" % (tag['name'], tag['value'])
                self.inventory.add_group(group)
                self._add_morpheus_instance(group, instance)

    def _get_server_details(self, serverid):
        headers = {'Authorization': "BEARER %s" % self.morpheus_token,
                   "Content-Type": "application/json"}
        method = "get"
        verify = self.morpheus_opt_args['sslverify']
        path = "/servers/%s" % serverid
        url = self.morpheus_api + path
        r = getattr(requests, method)(url, headers=headers, verify=verify)
        resultdict = r.json()

        return resultdict['server']

    def _add_morpheus_container(self, group, containerid, container, platform_query=False):
        server = self._get_server_details(container['server']['id'])
        platform = server['serverOs']['category']
        if platform_query:
            if platform is None:
                group = "platform_undetected"
            else:
                group = platform
            self.inventory.add_group(group)
        container_hostname = container['externalHostname']
        self.inventory.add_host(
            host=container_hostname,
            group=group
        )
        if self.morpheus_env or self.morpheus_simulate:
            if server['agentInstalled'] is True or self.morpheus_simulate_agent:
                noagent = False
            else:
                noagent = True
            if self.morpheus_simulate:
                self.morpheusprivatekeyfile = "/tmp/mock.key"
            self._set_morpheus_connection_vars(container_hostname,
                                               container['ip'], containerid,
                                               noagent, platform)
        else:
            self.inventory.set_variable(container_hostname,
                                        'ansible_host',
                                        container['ip'])

    def _add_morpheus_instance(self, group, instance):
        platform_query = False
        if group == "platform_query":
            platform_query = True

        if len(instance['containers']) > 1:
            containerdata = self._get_containers_from_morpheus(instance['id'])
            for containerid in instance['containers']:
                for container in containerdata['containers']:
                    if containerid == container['id']:
                        self._add_morpheus_container(group, containerid, container, platform_query)
        else:
            containerdata = self._get_containers_from_morpheus(instance['id'])
            containerid = containerdata['containers'][0]['id']
            self._add_morpheus_container(group, containerid, containerdata['containers'][0], platform_query)

    def _filter_morpheus_output(self, rawresponse, group, searchtype, searchstring):
        if self.morpheus_env:
            try:
                for file in os.listdir(self.workspace):
                    if file.startswith("private-"):
                        self.morpheusprivatekeyfile = self.workspace + file
            except Exception as e:
                e = e
                raise AnsibleParserError("Cannot find morpheus private key in workspace directory")
        if searchtype == "label":
            for instance in rawresponse['instances']:
                if version.parse(self.morpheus_version) > version.parse("5.0"):
                    for label in instance['labels']:
                        if str(searchstring).lower() == str(label).lower():
                            self._add_morpheus_instance(group, instance)
                else:
                    for tag in instance['tags']:
                        if str(searchstring).lower() == str(tag).lower():
                            self._add_morpheus_instance(group, instance)
        elif searchtype == "name":
            for instance in rawresponse['instances']:
                if searchstring in instance['name']:
                    self._add_morpheus_instance(group, instance)
        elif searchtype == "app":
            for app in rawresponse['apps']:
                if searchstring['appname'].lower() == app['name'].lower() and \
                        app['appStatus'] in ['running', 'completed']:
                    for apptier in app['appTiers']:
                        if searchstring['apptier'] in apptier['tier']['name']:
                            for instance in apptier['appInstances']:
                                self._add_morpheus_instance(group, instance['instance'])
        elif searchtype == "cloud":
            for instance in rawresponse['instances']:
                self._add_morpheus_instance_cloud_bytag(instance)
                self._add_morpheus_instance("platform_query", instance)
        elif searchtype == "tag":
            for instance in rawresponse['instances']:
                for tag in instance['tags']:
                    if searchstring['tagName'] == tag['name'] and searchstring['tagValue'] == tag['value']:
                        self._add_morpheus_instance(group, instance)

    def verify_file(self, path):
        '''Return true/false if this is possibly a valid file for this plugin to
        consume
        '''
        valid = True
        if super(InventoryModule, self).verify_file(path):
            if path.endswith(('morpheusinv.yaml', 'morpheusinv.yml')):
                valid = True
        return valid

    def parse(self, inventory, loader, path, cache):
        '''Return dynamic inventory from source '''
        super(InventoryModule, self).parse(inventory, loader, path, cache)

        if os.environ['PWD'].startswith('/var/opt/morpheus'):
            self.morpheus_env = True
        config_data = self._read_config_data(path)

        try:
            self.groups = config_data['groups']
            if self.morpheus_env:
                self.workspace = str(os.environ['ANSIBLE_LOOKUP_PLUGINS'])[:-51]
                for file in os.listdir(self.workspace):
                    if file.startswith("extraVars-"):
                        morpheusextravarsfile = self.workspace + file
                with open(morpheusextravarsfile, 'r') as stream:
                    self.extravars = yaml.safe_load(stream)
                self.morpheus_url = self.extravars['morpheus']['morpheus']['applianceUrl']
                self.morpheus_token = config_data['morpheus_api_key']
            else:
                self.morpheus_url = config_data['morpheus_url']
                self.morpheus_token = config_data['morpheus_api_key']

            self.morpheus_api = self.morpheus_url + "/api"
            if 'morpheus_client_id' in config_data:
                self.morpheus_opt_args['client_id'] = config_data['morpheus_client_id']
            if 'morpheus_ssl_verify' in config_data:
                if config_data['morpheus_ssl_verify']:
                    self.morpheus_opt_args['sslverify'] = True
                elif config_data['morpheus_ssl_verify'] is False:
                    self.morpheus_opt_args['sslverify'] = False
                else:
                    raise AnsibleParserError('morpheus_ssl_verify must be set to "True" or "False"')
            if 'morpheus_simulate' in config_data:
                self.morpheus_simulate = config_data['morpheus_simulate']
            if 'morpheus_simulate_agent' in config_data:
                self.morpheus_simulate_agent = config_data['morpheus_simulate_agent']

        except Exception as e:
            raise AnsibleParserError("Options missing: %s" % e)

        self._set_version_from_morpheus()
        self._set_morpheus_oldmetadata()

        for group in self.groups:
            if group['searchtype'] == 'cloud':
                rawoutput = self._get_data_from_morpheus(searchtype=group['searchtype'], searchstring=group['searchstring'])
                self._filter_morpheus_output(rawoutput, None, group['searchtype'], group['searchstring'])
            else:
                self.inventory.add_group(group['name'])
                rawoutput = self._get_data_from_morpheus(searchtype=group['searchtype'])
                self._filter_morpheus_output(rawoutput, group['name'], group['searchtype'], group['searchstring'])
