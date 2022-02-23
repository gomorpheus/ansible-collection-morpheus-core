# Ansible Morpheus Collection - Core

- [Ansible Morpheus Collection - Core](#ansible-morpheus-collection---core)
  - [Requirements](#requirements)
  - [Installation](#installation)
    - [Ansible 2.9](#ansible-29)
    - [Ansible >= 2.10](#ansible--210)
  - [Inventory Plugin Usage](#inventory-plugin-usage)
    - [Inventory Variables](#inventory-variables)
    - [Examples](#examples)
      - [Use in Morpheus](#use-in-morpheus)
      - [Name or Label](#name-or-label)
      - [Tag](#tag)
      - [App](#app)
      - [Cloud](#cloud)
    - [Token Requirement](#token-requirement)
    - [Troubleshooting](#troubleshooting)
  - [Ansible Roles for Morpheus Setup](#ansible-roles-for-morpheus-setup)
  - [Support Expectations](#support-expectations)

## Requirements

- Ansible >= 2.9 or ansible-core >= 2.11
- requests
- packaging
- future (required for python 2.7)

## Installation

Ansible made many changes in versions past 2.9, but the collection installation methods should work for every version.

If you wish to install from Ansible galaxy, use the following: `ansible-galaxy collection install morpheus.core`

### Ansible 2.9

---
**NOTE**

Ansible 2.9 doesn't recognize the collection's inventory plugins once the collection is installed.  Follow these instructions to use the inventory plugin in Ansible 2.9.

This has been tested both with the EPEL and pip installed versions of Ansible, so this method should be fairly portable.

---

If it doesn't exist, create the directory `/usr/share/ansible/plugins/inventory`
```
mkdir -p /usr/share/ansible/plugins/inventory
```

Install the collection.  By default, the collection will be installed at `~/.ansible/collections/ansible_collections/morpheus/core`  

```
ansible-galaxy collection install morpheus.core
```

Copy or symlink the `plugins/inventory/morpheus_inventory.py` file to the `/usr/share/ansible/plugins/inventory` directory.
```
cp ~/.ansible/collections/ansible_collections/morpheus/core/plugins/inventory/morpheus_inventory.py /usr/share/ansible/plugins/inventory/
```

Run `ansible-doc` to confirm installation
```
ansible-doc -t inventory -l | grep morpheus
```

When using this module with Ansible 2.9, you will refer to the module in your YAML file as:
```
plugin: morpheus_inventory
```

### Ansible >= 2.10

Install the collection through Ansible
```
ansible-galaxy collection install morpheus.core
```

Run `ansible-doc` to confirm installation
```
ansible-doc -t inventory -l | grep morpheus
```

When using this module as a collection with Ansible >= 2.10, refer to the module in your YAML file as:
```
plugin: morpheus.core.morpheus_inventory
```

## Inventory Plugin Usage

Within Morpheus, the dynamic inventory plugin will query the API and return a set of targets based on your search and organaizational criteria.

### Inventory Variables

|Name|Required|Description|
|---|---|---|
|plugin|yes|Use `morpheus_inventory` to activate the plugin|
|groups|yes||List used for group definition|
|name|yes|Required except for `cloud` search types|
|searchtype|yes|Search type for host matching.  Values: `label`, `name`, `app`, `cloud`, `tag`|
|searchstring|yes|Search string - the `app` and `tag` types uses this as a list, otherwise it is a string|
|morpheus_url|yes|Morpheus URL|
|morpheus_api_key|yes|Required for Morpheus versions <= 5.0.0|
|morpheus_ssl_verify|no|Option to disable ssl verification, defaults to True|

---
**NOTES**

Morpheus versions <= 5.0.0 require an API token in the inventory file to provide access to the Morpheus API.  Look in the Examples section for an example using Ansible Vault.

Morpheus versions >= 5.0.0 can use an ephemeral API token if run as a Morpheus task.  This has only been tested against 5.4.3, but should work all the way back to 5.0.0.

### Examples

#### Use in Morpheus

Create an Ansible Task in Morpheus and specify the playbook you wish to run.  Set the `Execute Target` to `Local`.

In `Command Options` specify `-i <relative path>/morpheusinv.yml`

This will process `morpheusinv.yml` as a dynamic inventory using the specified plugin.

**NOTES**

This plugin requires the Morpheus agent on target hosts due to credential storage methods in Morpheus.

#### Name or Label

Name searches are a simple text match. If your string is in the name anywhere, it will match.  Label must match exactly, but is case insensitive.

**Example:**

```yaml
plugin: morpheus_inventory
groups:
  - name: morphtest
    searchtype: label
    searchstring: whateverlabel
morpheus_url: <your morpheus URL>
morpheus_api_key: <your API key>
```

This will create a group `morphtest` and add any instances that have the label `whateverlabel` applied in Morpheus.

#### Tag

The tag search requires a tag name and value to be specified to add instances to a specified group.

**Example:**

```yaml
plugin: morpheus_inventory
groups:
  - name: dockerhosts
    searchtype: tag
    searchstring:
      tagName: servertype
      tagValue: docker
  - name: morpheus_ui
    searchtype: tag
    searchstring:
      tagName: application
      tagValue: morpheus
morpheus_url: <your morpheus URL>
morpheus_api_key: <your API key>
```

This will create 2 groups.  Instances tagged with a `servertype` tag with a value of `docker` will be put into the `dockerhosts` group.
Instances tagged with an `application` tag with a value of `morpheus` will be put into the `morpheus_ui` group.

#### App

The App search type will create a group named `name` out of the instances in the `apptier` tier of app `appname`.

**Example:**

```yaml
plugin: morpheus_inventory
groups:
  - name: ui
    searchtype: app
    searchstring:
      appname: 2tier
      apptier: UI
  - name: db
    searchtype: app
    searchstring:
      appname: 2tier
      apptier: Database
morpheus_url: <your morpheus URL>
morpheus_api_key: <your API key>
```

This will create two groups: `ui` and `db`.
`ui` will contain instances from the `UI` tier of the `2tier` application that was deployed in Morpheus from a blueprint.
`db` will contain instances from the `Database` tier of the `2tier` application.

#### Cloud

Cloud types will match the searchstring against the cloud `code` or `id` and generate groups based on remote tags as `<key>_<value>`.  It will also generate groups based on `platform` as seen by the Morpheus agent.  Unknown or agent-less VMs will appear under the `platform_undetected` group.

**Example:**

```yaml
plugin: morpheus_inventory
groups: 
  - searchtype: cloud
    searchstring: vmware
morpheus_url: <your morpheus URL>
morpheus_api_key: <your API key>
```

### Token Requirement

Since the inventory file will need to be stored in a git repository, it is not advised to store it in plain text.

We suggest encrypting the API token with Ansible Vault with the vault password stored in a file on the Morpheus UI server(s).

Acquire a token by going in your Morpheus user settings and clicking the API Access button.
Any entry will be sufficient.  Regenerate an Access Token and copy it.

On your Morpheus server, create a directory under `/var/opt/morpheus/morpheus-ui` to store the Ansible vault password.
Restrict permissions on this directory to the Morpheus user that runs Ansible: `morpheus-local`
```bash
install -o morpheus-local -g morpheus-local -m 0770 -d /var/opt/morpheus/morpheus-ui/ansiblevault
```

In your task, specify `--vault-password-file /var/opt/morpheus/morpheus-ui/ansiblevault/<file>` in order to use the password.

Information on encrypting strings and variables for ansible is located [HERE](https://docs.ansible.com/ansible/latest/user_guide/vault.html)

### Troubleshooting

By using `-vv` or higher whether using `ansible-inventory` or using the inventory in a playbook, the plugin will output extra information for use in troubleshooting.  Output will be prefixed by: `morpheus_inventory: `

## Ansible Roles for Morpheus Setup

These roles are designed for net new Morpheus configurations.  They are _NOT_ designed for removing existing items.

See README files in `roles/` for information regarding the roles in this collection

## Support Expectations

Please refer to the [Morpheus Open Source Code Support Policy](https://support.morpheusdata.com/s/article/Morpheus-Open-Source-Code-Support-Policy)