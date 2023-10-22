# morpheus.core.virtual_image
Create, Update and Delete Virtual Images and Virtual Image Files

## Parameters

|Parameter|Choices/Defaults|Comments|
|---|---|---|
|state|Choices:<br/> <ul><li>absent</li><li>present &larr;(default)</li></ul>|State/Action to apply to the Virtual Image or File<br/> If `state=absent` and `filename` is specified, then only the file associated with the image will be removed.|
|virtual_image_id||The id of the Virtual Image|
|name||The name of the Virtual Image|
|filename||The name of a Virtual Image File|
|file_path||Path to a local file to upload.<br/> Note, that files should be small (a few MB), otherwise it is likely the module will OOM and crash attempting to base64 encode the file.|
|file_url||URL Link to a File that Morpheus can download|
|labels||A list of labels to apply|
|image_type||Set the Image Type code, e.g. `vmware`|
|storage_provider_id||Specify the Storage Provider by Id|
|is_cloud_init|Choices<br/> <ul><li>true</li><li>false</li></ul>|Is Cloud Init enabled|
|user_data||Cloud Init user provided bash script|
|install_agent|Choices<br/> <ul><li>true</li><li>false</li></ul>|Install the Morpheus Agent?|
|username||Specify Virtual Image Username|
|password||Specify Virtual Image Password|
|ssh_key||Specify an SSH Key for the Virtual Image|
|os_type||Specify the OS Type Code or Name, e.g. windows.server.2022|
|visibility|Choices<br/> <ul><li>private</li><li>public</li></ul>|If Virtual Image is private or public|
|accounts||List of Tenants by Id for which this Virtual Image is available|
|is_auto_join_domain|Choices<br/> <ul><li>true</li><li>false</li></ul>|Whether to Auto Join Domain|
|virtio_supported|Choices<br/> <ul><li>true</li><li>false</li></ul>|Are Virtio Drivers installed?|
|vm_tools_installed|Choices<br/> <ul><li>true</li><li>false</li></ul>|Are VMware Tools installed?|
|trial_version|Choices<br/> <ul><li>true</li><li>false</li></ul>|Is Virtual Image a Trial Version|
|is_sysprep|Choices<br/> <ul><li>true</li><li>false</li></ul>|Is sysprep enabled?|
|azure_config||Options for Azure Virtual Images|
|publisher<br/> (azure_config)||Name of Publisher in the Azure Marketplace|
|offer<br/> (azure_config)||Name of Offer in the Azure Marketplace|
|sku<br/> (azure_config)||Name of SKU in the Azure Marketplace|
|version<br/> (azure_config)||Name of Version in the Azure Marketplace|
|config||Dictionary of Virtual Image configuration|
|tags||List of Tags to apply|
|name<br/> (tags)||Tag Name|
|value<br/> (tags)||Tag Value|

## Attributes

|Attribute|Support|Comments|
|---|---|---|
|check_mode|Full|Can run in ```check_mode``` and predict changed status without performing any modifications|
|diff_mode|Full|Will return what has changed (or needs changing when run with ```check_mode```)|

## Examples

```yaml
- name: Create Virtual Image and upload File
  morpheus.core.virtual_image:
    state: present
    name: My VMware Image
    image_type: vmware
    is_cloud_init: true
    install_agent: true
    username: root
    password: Password123
    os_type: redhat 8 64bit
    visibility: public
    accounts:
        - 1
    vm_tools_installed: true
    filename: rhel8x64.ova
    file_url: https://my.domain.tld/rhel8x64.ova

- name: Remove Virtual Image by Name
  morpheus.core.virtual_image:
    state: absent
    name: Win2016

- name: Remove Virtual Image by Id
  morpheus.core.virtual_image:
    state: absent
    virtual_image_id: 700

- name: Remove Virtual Image File
  morpheus.core.virtual_image:
    virtual_image_id: 750
    filename: windows_template.ova
    state: absent
```

## Return Values

|Key|Returned|Description|
|---|---|---|
|virtual_image|always|Information about the Virtual Image|

## Status

### Authors
James Riach (@McGlovin1337)
