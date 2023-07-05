# morpheus.core.appliance_maintenance_mode
Set the Maintenance Mode state of the target Morpheus Appliance

## Parameters

|Parameter|Choices/Defaults|Comments|
|---|---|---|
|state|Choices:<br/> <ul><li>enabled &larr;</li><li>disabled</li></ul>|Set the Maintenance Mode state|

## Attributes

|Attribute|Support|Comments|
|---|---|---|
|check_mode|Full|Can run in ```check_mode``` and predict changed status without performing any modifications|
|diff_mode|Full|Will return what has changed (or needs changing when run with ```check_mode```)|

## Examples

```yaml
- name: Enable Appliance Maintenance Mode
  morpheus.core.appliance_maintenance_mode:
    state: enabled

- name: Disable Appliance Maintenance Mode
  morpheus.core.appliance_maintenance_mode:
    state: disabled
```

## Return Values

|Key|Returned|Description|
|---|---|---|
|success|always|If the API Request was Successful|

## Status

### Authors
James Riach (@McGlovin1337)