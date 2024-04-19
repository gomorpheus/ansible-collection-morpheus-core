#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: appliance_settings
short_description: Configure Morpheus Appliance Settings
description:
    - Configures Morpheus Appliance Settings
version_added: 0.4.0
author: James Riach (@McGlovin1337)
options:
    appliance_url:
        description:
            - Defines the URL of the Morpheus Appliance.
        type: str
    internal_appliance_url:
        description:
            - Defines the Internal URL of the Morpheus Appliance.
        type: str
    cors_allowed:
        description:
            - Define origins allowed to access the Morpheus API.
        type: str
    registration_enabled:
        description:
            - Enable new users to register a new tenant.
        type: bool
    default_role_id:
        description:
            - Set the default Tenant Role applied to new Tenant Registrations.
        type: int
    default_user_role_id:
        description:
            - Set the default User Role applied the user created from Tenant Registration.
        type: int
    docker_privileged_mode:
        description:
            - Enable or Disable Docker privileged mode.
        type: bool
    password_min_length:
        description:
            - Define the minimum length for passwords.
        type: int
    password_min_upper_case:
        description:
            - Define the minimum number of upper case characters in passwords.
        type: int
    password_min_numbers:
        description:
            - Define the minimum number of numbers in passwords.
        type: int
    password_min_symbols:
        description:
            - Define the minimum number of symbols in passwords.
        type: int
    user_browser_session_timeout:
        description:
            - Define the period of time in minutes to logout an idle user session.
        type: int
    user_browser_session_warning:
        description:
            - Define the period of time in minutes to warn the user of session timeout.
        type: int
    expire_pwd_days:
        description:
            - Expire passwords after this number of days. 0 disables this feature.
        type: int
    disable_after_attempts:
        description:
            - Disable user account after this number of failed login attempts.
        type: int
    disable_after_days_inactive:
        description:
            - Disable user account after this number of days of inactivity.
        type: int
    warn_user_days_before:
        description:
            - Warn user this number of days before account is disabled.
        type: int
    smtp_mail_from:
        description:
            - Set the SMTP Mail From address header
        type: str
    smtp_server:
        description:
            - Set the SMTP Server to relay email through
        type: str
    smtp_port:
        description:
            - Set the SMTP Server Port to connect to
        type: int
    smtp_ssl:
        description:
            - Use SSL to connect to the defined SMTP Server
        type: bool
    smtp_tls:
        description:
            - Use TLS to connect to the defined SMTP Server
        type: bool
    smtp_user:
        description:
            - User to Authenticate with the defined SMTP Server
        type: str
    smtp_password:
        description:
            - Password to Authenticate with the define SMTP Server
        type: str
    proxy_host:
        description:
            - Define a Proxy Server
        type: str
    proxy_port:
        description:
            - Set the Proxy Server port
        type: int
    proxy_user:
        description:
            - User to Authenticate with the defined Proxy Server
        type: str
    proxy_password:
        description:
            - Password to Authenticate with the define Proxy Server
        type: str
    proxy_domain:
        description:
            - Set the Proxy Domain
        type: str
    proxy_workstation:
        description:
            - Set the Proxy Workstation
        type: str
    currency_provider:
        description:
            - Define a Currency Provider
        type: str
    currency_key:
        description:
            - Set the API Key for the defined Currency Provider
        type: str
    enable_all_zone_types:
        description:
            - Enable All Cloud (Zone) Types
        type: bool
    enable_zone_types:
        description:
            - Specify List of Cloud (Zone) Types to Enable
        type: list
        elements: int
    disable_zone_types:
        description:
            - Specify List of Cloud (Zone) Types to Disable
        type: list
        elements: int
    disable_all_zone_types:
        description:
            - Disable All Cloud (Zone) Types
        type: bool
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
- name: Configure SMTP Settings
  morpheus.core.appliance_settings:
    smtp_server: smtp.domain.tld
    smtp_port: 25
    smtp_tls: true

- name: Set Appliance URL
  morpheus.core.appliance_settings:
    appliance_url: cmp.domain.tld
'''

RETURN = r'''
success:
    description:
        - If the API Request was Successful
    returned: always
    type: bool
    sample:
        "success": true
appliance_settings:
    description:
        - The current Morpheus Appliance Settings
    returned: success
    type: dict
    sample:
        "appliance_settings": {
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
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
try:
    import module_utils.morpheus_funcs as mf
    from module_utils.morpheusapi import MorpheusApi
except ModuleNotFoundError:
    import ansible_collections.morpheus.core.plugins.module_utils.morpheus_funcs as mf
    from ansible_collections.morpheus.core.plugins.module_utils.morpheusapi import MorpheusApi


def run_module():
    argument_spec = {
        'appliance_url': {'type': 'str'},
        'internal_appliance_url': {'type': 'str'},
        'cors_allowed': {'type': 'str'},
        'registration_enabled': {'type': 'bool'},
        'default_role_id': {'type': 'int'},
        'default_user_role_id': {'type': 'int'},
        'docker_privileged_mode': {'type': 'bool'},
        'password_min_length': {'type': 'int', 'no_log': False},
        'password_min_upper_case': {'type': 'int', 'no_log': False},
        'password_min_numbers': {'type': 'int', 'no_log': False},
        'password_min_symbols': {'type': 'int', 'no_log': False},
        'user_browser_session_timeout': {'type': 'int'},
        'user_browser_session_warning': {'type': 'int'},
        'expire_pwd_days': {'type': 'int'},
        'disable_after_attempts': {'type': 'int'},
        'disable_after_days_inactive': {'type': 'int'},
        'warn_user_days_before': {'type': 'int'},
        'smtp_mail_from': {'type': 'str'},
        'smtp_server': {'type': 'str'},
        'smtp_port': {'type': 'int'},
        'smtp_ssl': {'type': 'bool'},
        'smtp_tls': {'type': 'bool'},
        'smtp_user': {'type': 'str'},
        'smtp_password': {'type': 'str', 'no_log': True},
        'proxy_host': {'type': 'str'},
        'proxy_port': {'type': 'int'},
        'proxy_user': {'type': 'str'},
        'proxy_password': {'type': 'str', 'no_log': True},
        'proxy_domain': {'type': 'str'},
        'proxy_workstation': {'type': 'str'},
        'currency_provider': {'type': 'str'},
        'currency_key': {'type': 'str', 'no_log': True},
        'enable_all_zone_types': {'type': 'bool'},
        'enable_zone_types': {'type': 'list', 'elements': 'int'},
        'disable_zone_types': {'type': 'list', 'elements': 'int'},
        'disable_all_zone_types': {'type': 'bool'}
    }

    mutually_exclusive = [
        ('enable_all_zone_types', 'enable_zone_types'),
        ('enable_all_zone_types', 'disable_zone_types'),
        ('enable_all_zone_types', 'disable_all_zone_types'),
        ('disable_all_zone_types', 'enable_zone_types'),
        ('disable_all_zone_types', 'disable_zone_types')
    ]

    required_by = {
        'currency_provider': 'currency_key'
    }

    result = {
        'changed': False
    }

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        mutually_exclusive=mutually_exclusive,
        required_by=required_by
    )

    connection = Connection(module._socket_path)
    morpheus_api = MorpheusApi(connection)

    original_settings = morpheus_api.get_appliance_settings()
    current_settings = mf.dict_keys_to_snake_case(original_settings)

    # Check if a param was used that we can't verify a change for
    unverifiable = False
    for k, v in module.params.items():
        if v is None:
            continue

        if k not in current_settings:
            unverifiable = True
            break

    if module.check_mode:
        diff = []
        for k, v in module.params.items():
            if v is not None:
                try:
                    if current_settings[k] != v:
                        diff_item = {
                            'after': '{0} = {1}\n'.format(k, v),
                            'before': '{0} = {1}\n'.format(k, current_settings[k])
                        }
                        diff.append(diff_item)
                except KeyError:
                    continue
            if module._diff:
                result['diff'] = diff

        result['changed'] = True if unverifiable or len(diff) > 0 else False

        module.exit_json(**result)

    response = morpheus_api.set_appliance_settings(module.params)

    try:
        result['success'] = response['success']
    except KeyError:
        result['success'] = False

    updated_settings = morpheus_api.get_appliance_settings()

    changed, diff = mf.dict_diff(updated_settings, original_settings)
    result['changed'] = True if changed or unverifiable else False
    if module._diff:
        result['diff'] = diff

    if result['success']:
        result['appliance_settings'] = mf.dict_keys_to_snake_case(updated_settings)

    if not result['success']:
        module.fail_json('API Request Failed', **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
