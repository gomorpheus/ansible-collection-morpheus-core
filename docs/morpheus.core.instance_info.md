# morpheus.core.instance_info
Retrieve information about Morpheus Instances

## Parameters

|Parameter|Choices/Defaults|Comments|
|---|---|---|
|id||Specify the id of an instance|
|name||Filter instances by name|
|regex_name|Choices:<br/> <ul><li>true</li><li>false &larr;(default)</li></ul>|Treat the name parameter as a regular expression|
|detail|Choices:<br/> <ul><li>minimal &larr;(default)</li><li>full</li><li>extra</li><li>summary</li></ul>|Specify the level of detail returned for matching instances|
|instance_type||Filter by the instance type code|
|agent_installed|Choices:<br/> <ul><li>true</li><li>false</li></ul>|Filter by if agent is installed or not|
|status||Filter by instance status, e.g. running|
|environment||Filter instances by environment|
|deleted|Choices:<br/> <ul><li>exclude &larr;(default)</li><li>include</li><li>only</li></ul>|Include, Exclude or Only show deleted instances or those pending removal|
|labels||Filter instances by matching labels|
|match_all_labels|Choices:<br/> <ul><li>true</li><li>false &larr;(default)</li></ul>|Match **ALL** specified labels|
|tags||Filter instances by matching tags|

## Attributes

|Attribute|Support|Comments|
|---|---|---|
|check_mode|Full|Can run in ```check_mode``` and predict changed status without performing any modifications|

## Examples

```yaml
- name: Get Info for a Specific Instance by id
  morpheus.core.instance_info:
    id: 200

- name: Get a short summary of instances
  morpheus.core.instance_info:
    detail: summary

- name: Get Extra Info for a Specific Instance by id
  morpheus.core.instance_info:
    id: 200
    detail: extra

- name: Get Info for all Instances with any of the specified labels
  morpheus.core.instance_info:
    labels:
      - foo
      - bar
      - prod

- name: Get Info of all Running Instances
  morpheus.core.instance_info:
    status: running
```

## Return Values

|Key|Returned|Description|
|---|---|---|
|morpheus_instances|always|List of Morpheus Instances with Info|

## Status

### Authors
James Riach (@McGlovin1337)