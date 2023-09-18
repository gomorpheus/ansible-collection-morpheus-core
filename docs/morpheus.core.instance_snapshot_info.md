# morpheus.core.instance_snapshot_info
Gather Morpheus Instance Snapshot information

## Parameters

|Parameter|Choices/Defaults|Comments|
|---|---|---|
|id||Specify the id of an instance|
|name||Filter instances by name|
|regex_name|Choices:<br/> <ul><li>true</li><li>false &larr;(default)</li></ul>|Treat the name parameter as a regular expression|
|environment||Filter instances by environment|
|labels||Filter instances by matching labels|
|match_all_labels|Choices:<br/> <ul><li>true</li><li>false &larr;(default)</li></ul>|Match **ALL** specified labels|
|tags||Filter instances by matching tags|

## Attributes

|Attribute|Support|Comments|
|---|---|---|
|check_mode|Full|Can run in ```check_mode``` and predict changed status without performing any modifications|

## Examples

```yaml
- name: Get Snapshots for specific instance
  morpheus.core.instance_snapshot_info:
    id: 200

- name: Get Snapshots for instances matching regex pattern
  morpheus.core.instance_snapshot_info:
    name: ^PRODWEB.*$
    regex_name: true

- name: Get Snapshots for instances with assigned labels
  morpheus.core.instance_snapshot_info:
    labels:
      - PROD
      - WEB
```

## Return Values

|Key|Returned|Description|
|---|---|---|
|instance_snapshots|always|List of Instances and their snapshots|

## Status

### Authors
James Riach (@McGlovin1337)
