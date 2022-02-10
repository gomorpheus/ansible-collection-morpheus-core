# Changelog

## v0.2.2

- In 5.4.3, Morpheus is requiring authentication for version information from `/api/ping`: [#7](https://github.com/gomorpheus/ansible-collection-morpheus-core/issues/7)
- OS Type is now able to be set via name in `roles/virtualimages`: [#6](https://github.com/gomorpheus/ansible-collection-morpheus-core/issues/6)
- Ansible requires that the FQCN be in the documentation part of the inventory plugin: [#3](https://github.com/gomorpheus/ansible-collection-morpheus-core/issues/3)
- `roles/settings` had the wrong source var: [#2](https://github.com/gomorpheus/ansible-collection-morpheus-core/issues/2)
- Version comparison was using distutils, which has been deprecated.  Switched to packaging. [#10](https://github.com/gomorpheus/ansible-collection-morpheus-core/issues/10)
- Troubleshooting info and verbose messaging added to plugin with `-vv` or higher. [#15](https://github.com/gomorpheus/ansible-collection-morpheus-core/issues/15)