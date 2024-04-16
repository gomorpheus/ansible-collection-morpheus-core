#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: appliance_facts
short_description: Gather Morpheus Appliance Facts
description:
    - Gathers Morpheus Appliance Facts
version_added: 0.3.0
author: James Riach (@McGlovin1337)
options:
    gather_subset:
        description:
            - "Specify or restrict the facts that are gathered.
              Possible values: V(all), V(database), V(elastic), V(license), V(rabbitmq),
              V(settings), V(system), V(threads).
              The minimum subset is: V(license), V(settings), V(system).
              To specify a specific subset, use V(!all, !min) and then specify the fact(s) required."
        type: list
        elements: str
        default: "all"
    gather_timeout:
        description:
            - Timeout period for collecting individual facts
        type: int
        default: 10
    filter:
        description:
            - Match facts to one of the specified patterns.
        type: list
        elements: str
        default: []
extends_documentation_fragment:
    - action_common_attributes
attributes:
    check_mode:
        support: N/A
        details: Not Required, Module does not make changes.
    diff_mode:
        support: N/A
    platform:
        platforms:
            - httpapi
'''

EXAMPLES = r'''
- name: Gather All Facts
  morpheus.core.appliance_facts:

- name: Gather Minimum Facts
  morpheus.core.appliance_facts:
    gather_subset:
      - "!all"

- name: Gather License Facts
  morpheus.core.appliance_facts:
    gather_subset:
      - "!all"
      - "!min"
      - "license"
'''

RETURN = r'''
ansible_facts:
    description:
        - Example of returned ansible_facts
    type: dict
    returned: always
    sample:
        "ansible_facts": {
            "gather_subset": [
                "!all",
                "!min",
                "license",
                "settings"
            ],
            "module_setup": true,
            "morpheus_license": {
                "account_name": "MyCompany",
                "amazon_product_codes": null,
                "config": {},
                "date_created": "2022-11-17T10:05:22Z",
                "end_date": "2023-08-31T00:00:00Z",
                "features": {
                    "activity": true,
                    "analytics": true,
                    "approval_services": true,
                    "approvals": true,
                    "apps": true,
                    "archives": true,
                    "automation": true,
                    "automation_services": true,
                    "backup_services": true,
                    "backups": true,
                    "boot": true,
                    "build_services": true,
                    "clouds": true,
                    "cmdb_services": true,
                    "code_service": true,
                    "cypher": true,
                    "dashboard": true,
                    "deployment_services": true,
                    "deployments": true,
                    "discovery": true,
                    "dns_services": true,
                    "groups": true,
                    "guidance": true,
                    "hosts": true,
                    "identity_services": true,
                    "image_builder": true,
                    "instances": true,
                    "ipam_services": true,
                    "key_pairs": true,
                    "library": true,
                    "load_balancer_services": true,
                    "load_balancers": true,
                    "logging": true,
                    "logging_services": true,
                    "migrations": true,
                    "monitoring": true,
                    "monitoring_services": true,
                    "network": true,
                    "plans": true,
                    "pricing": true,
                    "scheduling": true,
                    "security_services": true,
                    "service_discovery_services": true,
                    "ssl_certificates": true,
                    "storage": true,
                    "templates": true,
                    "tenants": true,
                    "trust_services": true,
                    "usage": true,
                    "user_groups": true,
                    "users": true,
                    "virtual_images": true
                },
                "free_trial": false,
                "hard_limit": true,
                "last_updated": "2022-11-17T10:05:22Z",
                "max_instances": 1000,
                "max_memory": 0,
                "max_storage": 0,
                "multi_tenant": true,
                "product_tier": "enterprise",
                "report_status": true,
                "start_date": "2022-08-22T00:00:00Z",
                "support_level": "standard",
                "whitelabel": true,
                "zone_types": null
            },
            "morpheus_settings": {
                "appliance_url": "https://cmp.domain.tld",
                "cors_allowed": null,
                "currency_key": null,
                "currency_provider": null,
                "default_role_id": null,
                "default_user_role_id": null,
                "disable_after_attempts": "5",
                "disable_after_days_inactive": null,
                "docker_privileged_mode": false,
                "enabled_zone_types": [
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
                "expire_pwd_days": null,
                "internal_appliance_url": null,
                "maintenance_mode": false,
                "proxy_domain": null,
                "proxy_host": null,
                "proxy_password": null,
                "proxy_password_hash": null,
                "proxy_port": null,
                "proxy_user": null,
                "proxy_workstation": null,
                "registration_enabled": false,
                "smtp_mail_from": "morpheus@domain.tld",
                "smtp_password": null,
                "smtp_password_hash": null,
                "smtp_port": "25",
                "smtp_server": "smtp.domain.tld",
                "smtp_ssl": false,
                "smtp_tls": true,
                "smtp_user": null,
                "stats_retainment_period": null,
                "warn_user_days_before": null
            }
        }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.facts.namespace import PrefixFactNamespace
from ansible.module_utils.facts import ansible_collector
try:
    import module_utils.morpheus_funcs as mf
    from module_utils.facts.appliance_database import MorpheusDatabaseFactCollector
    from module_utils.facts.appliance_elastic import MorpheusElasticFactCollector
    from module_utils.facts.appliance_license import MorpheusLicenseFactCollector
    from module_utils.facts.appliance_rabbitmq import MorpheusRabbitmqFactCollector
    from module_utils.facts.appliance_settings import MorpheusSettingsFactCollector
    from module_utils.facts.appliance_system import MorpheusSystemFactCollector
    from module_utils.facts.appliance_threads import MorpheusThreadsFactCollector
except ModuleNotFoundError:
    import ansible_collections.morpheus.core.plugins.module_utils.morpheus_funcs as mf
    from ansible_collections.morpheus.core.plugins.module_utils.facts.appliance_database import MorpheusDatabaseFactCollector
    from ansible_collections.morpheus.core.plugins.module_utils.facts.appliance_elastic import MorpheusElasticFactCollector
    from ansible_collections.morpheus.core.plugins.module_utils.facts.appliance_license import MorpheusLicenseFactCollector
    from ansible_collections.morpheus.core.plugins.module_utils.facts.appliance_rabbitmq import MorpheusRabbitmqFactCollector
    from ansible_collections.morpheus.core.plugins.module_utils.facts.appliance_settings import MorpheusSettingsFactCollector
    from ansible_collections.morpheus.core.plugins.module_utils.facts.appliance_system import MorpheusSystemFactCollector
    from ansible_collections.morpheus.core.plugins.module_utils.facts.appliance_threads import MorpheusThreadsFactCollector


def run_module():
    module = AnsibleModule(
        argument_spec=dict(gather_subset=dict(default=["all"], required=False, type='list', elements='str'),
                           gather_timeout=dict(default=10, required=False, type='int'),
                           filter=dict(default=[], required=False, type='list', elements='str'),),
        supports_check_mode=True
    )

    gather_subset = module.params['gather_subset']
    gather_timeout = module.params['gather_timeout']
    filter_spec = module.params['filter']
    minimal_gather_subset = frozenset(['license', 'settings', 'system'])

    collectors = [
        MorpheusDatabaseFactCollector,
        MorpheusElasticFactCollector,
        MorpheusLicenseFactCollector,
        MorpheusRabbitmqFactCollector,
        MorpheusSettingsFactCollector,
        MorpheusSystemFactCollector,
        MorpheusThreadsFactCollector,
    ]

    namespace = PrefixFactNamespace(namespace_name='ansible', prefix='ansible_')

    collector = ansible_collector.get_ansible_collector(all_collector_classes=collectors,
                                                        namespace=namespace,
                                                        filter_spec=filter_spec,
                                                        gather_subset=gather_subset,
                                                        gather_timeout=gather_timeout,
                                                        minimal_gather_subset=minimal_gather_subset)

    fact_results = collector.collect(module=module)

    module.exit_json(ansible_facts=mf.dict_keys_to_snake_case(fact_results))


def main():
    run_module()


if __name__ == '__main__':
    main()
