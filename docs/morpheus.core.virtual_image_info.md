# morpheus.core.virtual_image_info
Retrieve information about Morpheus Virtual Images

## Parameters

|Parameter|Choices/Defaults|Comments|
|---|---|---|
|virtual_image_id||Return info for specic Virtual Image by Id|
|name||Return info for Virtual Image by Name|
|regex_name|Choices:<br/> <ul><li>true</li><li>false &larr;(default)</li></ul>|Treat name parameter as a Regular Expression|
|filter_type|Choices:<br/> <ul><li>all &larr;(default)</li><li>synced</li><li>system</li><li>user</li></ul>|Filter Virtual Images by type|
|image_type||Filter by image type code, e.g. vmware, ami|
|labels||Filter by matching labels|
|match_all_labels|Choices:<br/> <ul><li>true</li><li>false &larr;(default)</li></ul>|If true, match all specified labels|
|detail|Choices:<br/> <ul><li>full</li><li>summary &larr;(default)</li></ul>|Level of detail returned about Virtual Images|

## Attributes

|Attribute|Support|Comments|
|---|---|---|
|check_mode|Full|Can run in ```check_mode``` and predict changed status without performing any modifications|

## Examples

```yaml
- name: Get Virtual Image by Id
  morpheus.core.virtual_image_info:
    virtual_image_id: 500

- name: Get Virtual Image by Name
  morpheus.core.virtual_image_info:
    name: redhat_image

- name: Get Virtual Images by Regex Match
  morpheus.core.virtual_image_info:
    name: ^.*$
    regex_name: true

- name: Get Synced VMware Virtual Images
  morpheus.core.virtual_image_info:
    filter_type: synced
    image_type: vmware

- name: Get User Virtual Images
  morpheus.core.virtual_image_info:
    filter_type: user
```

## Return Values

|Key|Returned|Description|
|---|---|---|
|virtual_images|always|List of Virtual Images|

## Status

### Authors
James Riach (@McGlovin1337)