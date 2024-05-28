# Changelog

## v0.7.1
- Added Integration Tests for numerous modules
- Fixed exceptions when running some modules in `check_mode`
- Improved change prediction accuracy when running some modules in `check_mode`
- Add validation for `role` parameter in `tenant` module
- Fix cloud_datastore module exception when `resource_permissions` and/or `tenant_permissions` options were not specified

## v0.7.0
- Added `azure_cloud` module
- Added `cloud_datastore_info` module
- Added `cloud_datastore` module
- Added `cloud_info` module
- Added `cloud_type_info` module
- Added `cypher_info` module
- Added `cypher` module
- Added `group_info` module
- Added `group` module
- Added `integration_info` module
- Added `role_info` module
- Added `standard_cloud` module
- Added `tenant_info` module
- Added `tenant` module
- Added `vcenter_cloud` module

## v0.6.0
- Added `virtual_image_info` module
- Added `virtual_image` module
- Added `key_pair_info` module
- Added `key_pair` module
- Added `ssl_certificate_info` module
- Added `ssl_certificate` module

## v0.5.1
- Added `all_apps` search type for inventory

## v0.5.0
- Added `instance` module
- Added `instance_snapshot_info` module
- Added `instance_snapshot` module

## v0.4.0
- Added `appliance_settings` module
- Added `appliance_maintenance_mode` module
- Added `instance_info` module

## v0.3.0
- Added httpapi connection plugin
- Added `appliance_facts` module

## v0.2.5
- Added AWS assume role support to cloud role

## v0.2.4
- Added `baseRoleId` to `userroles` role

## v0.2.3
- Verbose messages caused a problem with the app search type: [#26](https://github.com/gomorpheus/ansible-collection-morpheus-core/issues/26)

## v0.2.2

- In 5.4.3, Morpheus is requiring authentication for version information from `/api/ping`: [#7](https://github.com/gomorpheus/ansible-collection-morpheus-core/issues/7)
- OS Type is now able to be set via name in `roles/virtualimages`: [#6](https://github.com/gomorpheus/ansible-collection-morpheus-core/issues/6)
- Ansible requires that the FQCN be in the documentation part of the inventory plugin: [#3](https://github.com/gomorpheus/ansible-collection-morpheus-core/issues/3)
- `roles/settings` had the wrong source var: [#2](https://github.com/gomorpheus/ansible-collection-morpheus-core/issues/2)
- Version comparison was using distutils, which has been deprecated.  Switched to packaging. [#10](https://github.com/gomorpheus/ansible-collection-morpheus-core/issues/10)
- Troubleshooting info and verbose messaging added to plugin with `-vv` or higher. [#15](https://github.com/gomorpheus/ansible-collection-morpheus-core/issues/15)
