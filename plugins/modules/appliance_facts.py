#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: appliance_facts
short_description: Gather Morpheus Appliance Facts
description:
    - Gathers Morpheus Appliance Facts
version_added: 0.3.0
author: James Riach
'''

EXAMPLES = r'''
- name: Gather All Facts
  morpheus.core.appliance_facts:

- name: Gather License Facts
  morpheus.core.appliance_facts:
    gather_subset:
      - license
'''

RETURN = r'''
ansible_facts:
    description: Example of returned ansible_facts
    returned: always
    sample:
    "ansible_facts": {
            "gather_subset": [
                "all"
            ],
            "license": {
                "accountName": "MyCompany",
                "amazonProductCodes": null,
                "config": {},
                "dateCreated": "2022-11-17T10:05:22Z",
                "endDate": "2023-08-31T00:00:00Z",
                "features": {
                    "activity": true,
                    "analytics": true,
                    "approvalServices": true,
                    "approvals": true,
                    "apps": true,
                    "archives": true,
                    "automation": true,
                    "automationServices": true,
                    "backupServices": true,
                    "backups": true,
                    "boot": true,
                    "buildServices": true,
                    "clouds": true,
                    "cmdbServices": true,
                    "codeService": true,
                    "cypher": true,
                    "dashboard": true,
                    "deploymentServices": true,
                    "deployments": true,
                    "discovery": true,
                    "dnsServices": true,
                    "groups": true,
                    "guidance": true,
                    "hosts": true,
                    "identityServices": true,
                    "imageBuilder": true,
                    "instances": true,
                    "ipamServices": true,
                    "keyPairs": true,
                    "library": true,
                    "loadBalancerServices": true,
                    "loadBalancers": true,
                    "logging": true,
                    "loggingServices": true,
                    "migrations": true,
                    "monitoring": true,
                    "monitoringServices": true,
                    "network": true,
                    "plans": true,
                    "pricing": true,
                    "scheduling": true,
                    "securityServices": true,
                    "serviceDiscoveryServices": true,
                    "sslCertificates": true,
                    "storage": true,
                    "templates": true,
                    "tenants": true,
                    "trustServices": true,
                    "usage": true,
                    "userGroups": true,
                    "users": true,
                    "virtualImages": true
                },
                "freeTrial": false,
                "hardLimit": true,
                "lastUpdated": "2022-11-17T10:05:22Z",
                "maxInstances": 1000,
                "maxMemory": 0,
                "maxStorage": 0,
                "multiTenant": true,
                "productTier": "enterprise",
                "reportStatus": true,
                "startDate": "2022-08-22T00:00:00Z",
                "supportLevel": "standard",
                "whitelabel": true,
                "zoneTypes": null
            },
            "module_setup": true,
            "settings": {
                "applianceUrl": "https://cmp.domain.tld",
                "corsAllowed": null,
                "currencyKey": null,
                "currencyProvider": null,
                "defaultRoleId": null,
                "defaultUserRoleId": null,
                "disableAfterAttempts": "5",
                "disableAfterDaysInactive": null,
                "dockerPrivilegedMode": false,
                "enabledZoneTypes": [
                    {
                        "id": 4,
                        "name": "Amazon"
                    },
                    {
                        "id": 9,
                        "name": "Azure (Public)"
                    },
                    {
                        "id": 11,
                        "name": "DigitalOcean"
                    },
                    {
                        "id": 3,
                        "name": "Morpheus"
                    },
                    {
                        "id": 18,
                        "name": "Oracle Public Cloud"
                    },
                    {
                        "id": 40,
                        "name": "PowerVC"
                    },
                    {
                        "id": 17,
                        "name": "UpCloud"
                    },
                    {
                        "id": 38,
                        "name": "VMware Fusion"
                    },
                    {
                        "id": 28,
                        "name": "VMware vCenter"
                    },
                    {
                        "id": 34,
                        "name": "vCloud Director"
                    }
                ],
                "expirePwdDays": null,
                "internalApplianceUrl": null,
                "maintenanceMode": false,
                "proxyDomain": null,
                "proxyHost": null,
                "proxyPassword": null,
                "proxyPasswordHash": null,
                "proxyPort": null,
                "proxyUser": null,
                "proxyWorkstation": null,
                "registrationEnabled": false,
                "smtpMailFrom": "morpheus@domain.tld",
                "smtpPassword": null,
                "smtpPasswordHash": null,
                "smtpPort": "25",
                "smtpSSL": false,
                "smtpServer": "smtp.domain.tld",
                "smtpTLS": true,
                "smtpUser": null,
                "statsRetainmentPeriod": null,
                "warnUserDaysBefore": null
            }
        }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.facts.namespace import PrefixFactNamespace
from ansible.module_utils.facts import ansible_collector
from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import MorpheusApi
from ansible_collections.morpheus.core.plugins.module_utils.facts.appliance_license import MorpheusLicenseFactCollector
from ansible_collections.morpheus.core.plugins.module_utils.facts.appliance_settings import MorpheusSettingsFactCollector


def run_module():
    module = AnsibleModule(
        argument_spec=dict(gather_subset=dict(default=["all"], required=False, type='list'),
                           gather_timeout=dict(default=10, required=False, type='int'),
                           filter=dict(default="*", required=False),),
        supports_check_mode=True
    )

    gather_subset = module.params['gather_subset']
    gather_timeout = module.params['gather_timeout']
    filter_spec = module.params['filter']
    minimal_gather_subset = frozenset()

    collectors = [
        MorpheusLicenseFactCollector,
        MorpheusSettingsFactCollector,
    ]

    namespace = PrefixFactNamespace(namespace_name='ansible', prefix='ansible_')

    collector = ansible_collector.get_ansible_collector(all_collector_classes=collectors,
                                                        namespace=namespace,
                                                        filter_spec=filter_spec,
                                                        gather_subset=gather_subset,
                                                        gather_timeout=gather_timeout,
                                                        minimal_gather_subset=minimal_gather_subset)

    fact_results = collector.collect(module=module)

    module.exit_json(ansible_facts=fact_results)


def main():
    run_module()


if __name__ == '__main__':
    main()
