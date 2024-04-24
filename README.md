# Ansible Morpheus Collection - Core

- [Ansible Morpheus Collection - Core](#ansible-morpheus-collection---core)
  - [Requirements](#requirements)
  - [Installation](#installation)
    - [Ansible 2.9](#ansible-29)
    - [Ansible \>= 2.10](#ansible--210)
  - [Inventory Plugin Usage](#inventory-plugin-usage)
    - [Inventory Variables](#inventory-variables)
    - [Examples](#examples)
      - [Use in Morpheus](#use-in-morpheus)
      - [Name or Label](#name-or-label)
      - [Tag](#tag)
      - [App](#app)
      - [All Apps](#all-apps)
      - [Cloud](#cloud)
    - [Token Requirement](#token-requirement)
    - [Troubleshooting](#troubleshooting)
  - [httpapi Plugin Usage](#httpapi-plugin-usage)
    - [Parameters](#parameters)
    - [Example Inventory](#example-inventory)
  - [Ansible Roles for Morpheus Setup](#ansible-roles-for-morpheus-setup)
  - [Modules](#modules)
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
|searchtype|yes|Search type for host matching.  Values: `label`, `name`, `app`, `all_apps`, `cloud`, `tag`|
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

#### All Apps

The `all_apps` search type will create a groups for each app and child groups for each app tier.

**Example**

```yaml
plugin: morpheus.core.morpheus_inventory
groups:
  - searchtype: all_apps
```

If you have 2 apps named `AppA` and `AppB` with two tiers each named `Database` and `Web`, You will get the following inventory:

```json
{
  "all": {
    "children": [
      "AppA",
      "AppB"
    ]
  },
  "AppA": {
    "children": [
      "AppA_Database",
      "AppA_Web"
    ]
  },
  "AppA_Database": {
    "hosts": [
      "host1",
      "host2"
    ]
  },
  "AppA_Web": {
    "hosts": [
      "host3",
      "host4"
    ]
  },
  "AppB": {
    "children": [
      "AppB_Database",
      "AppB_Web"
    ]
  }
  ..... and so on.
}
```

If you construct a playbook and workflow in Morpheus to take advantage of this format, you can dynamically target Apps and App Tiers.  An example playbook:

```
- hosts: "{{ morpheus['customOptions']['morph_appname'] }}_{{ morpheus['customOptions']['morph_app_tier'] }}"
  gather_facts: false
  tasks:
    - ping:
```

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

## httpapi Plugin Usage
The httpapi plugin allows one to interact with Morpheus Appliances through Ansible modules by specifying appliances in Ansible Inventories.

### Parameters
The following Parameters are specific to this module. Other standard httpapi parameters apply.

|Parameter|Comments|
|---|---|
|morpheus_user|Specifying a user will login to the api and retrieve an authentication token. <br /> **ANSIBLE_MORPHEUS_USER**|
|morpheus_password|When using morpheus_user for authentication, morpheus_password should also be specified. <br /> **ANSIBLE_MORPHEUS_PASSWORD**|
|morpheus_api_token|Use a pre-defined API Token instead of Username/Password. <br /> **ANSIBLE_MORPHEUS_TOKEN**

### Example Inventory
```yaml
all:
  hosts:
    devcmp.example.tld:
      ansible_morpheus_user: johndoe
      ansible_morpheus_password: password
    testcmp.example.tld:
      ansible_morpheus_token: 12345abc-67de-89fa-12bc-345678defabc
  vars:
    ansible_network_os: morpheus.core.morpheus
    ansible_httpapi_use_ssl: true
```

**Note:** It is not recommended to keep plaintext credentials in files. Where possible use Ansible Vault to encrypt secrets.

## Ansible Roles for Morpheus Setup

These roles are designed for net new Morpheus configurations.  They are _NOT_ designed for removing existing items.

See README files in `roles/` for information regarding the roles in this collection

## Modules
Individual Module Documentation can be found included with the module and can be viewed with ```ansible-doc -t module morpheus.core.module_name```

|Module Name|Description|
|---|---|
|[appliance_facts](docs/appliance_facts_module.rst)|Gathers appliance settings and license facts of the target Morpheus Appliance|
|[appliance_maintenance_mode](docs/appliance_maintenance_mode_module.rst)|Set Morpheus Appliance Maintenance Mode|
|[appliance_settings](docs/appliance_settings_module.rst)|Configure Morpheus Appliance Settings|
|[azure_cloud](docs/azure_cloud_module.rst)|Configure an Azure Cloud|
|[cloud_datastore_info](docs/cloud_datastore_info_module.rst)|Retrieve information about Cloud Datastores|
|[cloud_datastore](docs/cloud_datastore_module.rst)|Manage configurtaion of Cloud Datastores|
|[cloud_info](docs/cloud_info_module.rst)|Retrieve information about Clouds|
|[cloud_type_info](docs/cloud_type_info_module.rst)|Retrieve information about Cloud Types|
|[cypher_info](docs/cypher_info_module.rst)|Retrieve items from Cypher and optionally decrypt|
|[cypher](docs/cypher_module.rst)|Manage items in Cypher|
|[group_info](docs/group_info_module.rst)|Retrieve information about Groups|
|[group](docs/group_module.rst)|Manage Groups|
|[instance_info](docs/instance_info_module.rst)|Retrieve information about Morpheus Instances|
|[instance](docs/instance_module.rst)|Manage state of Morpheus Instances|
|[instance_snapshot_info](docs/instance_snapshot_info_module.rst)|Gather information about Instance Snapshots|
|[instance_snapshot](docs/instance_snapshot_module.rst)|Manage Instance Snapshots|
|[integration_info](docs/integration_info_module.rst)|Retrieve information about Integrations|
|[key_pair_info](docs/key_pair_info_module.rst)|Gather information about Key Pairs|
|[key_pair](docs/key_pair_module.rst)|Create, Generate and Remove Key Pairs|
|[role_info](docs/role_info_module.rst)|Retrieve information about Roles|
|[ssl_certificate_info](docs/ssl_certificate_info_module.rst)|Gather information about SSL Certificates|
|[ssl_certificate](docs/ssl_certificate_module.rst)|Create, Update and Remove SSL Certificates|
|[standard_cloud](docs/standard_cloud_module.rst)|Manage Standard Clouds|
|[tenant_info](docs/tenant_info_module.rst)|Retrieve information about Tenants|
|[tenant](docs/tenant_module.rst)|Manage Tenants|
|[vcenter_cloud](docs/vcenter_cloud_module.rst)|Manage VMWare vCenter Clouds|
|[virtual_image_info](docs/virtual_image_info_module.rst)|Gather information about Virtual Images|
|[virtual_image](docs/virtual_image_module.rst)|Create, Update and Remove Virtual Images and Virtual Image Files|

## Testing
The collection includes ignore files for running `ansible-test sanity` without error.

A number of Integration Tests exist for modules that can be run using `ansible-test`

### WARNING
The Integration Tests require access to a Morpheus Appliance, and they **WILL** make changes. It is **NOT** recommended to run these against a Production environment!

### Integration Test Execution
Enter the directory the collection is installed, e.g.
```shell
cd ~/.ansible/collections/ansible_collections/morpheus/core
```
Edit the file `integration_config.yml` and supply the hostname/address for the `ansible_host` variable as well as either `ansible_morpheus_user` and `ansible_morpheus_password` or `ansible_morpheus_token`.

To view the list of available test targets:
```shell
ansible-test integration --list-targets
```
**NOTE**: Some of the `_info` module tests rely on non `_info` modules creating resources. Therefore it would be recommended to test the non `_info` modules first to confirm they operate as expected. However, you can of course, run all tests in order by not specifying a specific target.

Example Integration Test Execution:
```shell
ansible-test integration group --local -vvv
```

## Support Expectations

Please refer to the [Morpheus Open Source Code Support Policy](https://support.morpheusdata.com/s/article/Morpheus-Open-Source-Code-Support-Policy)
