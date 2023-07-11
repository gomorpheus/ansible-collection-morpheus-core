# morpheus.core.appliance_maintenance_mode
Set the Maintenance Mode state of the target Morpheus Appliance

## Parameters

|Parameter|Choices/Defaults|Comments|
|---|---|---|
|state|Choices:<br/> <ul><li>enabled &larr;(default)</li><li>disabled</li></ul>|Set the Maintenance Mode state|

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

## Notes
It seems not all versions of the Morpheus API return a key for the current Maintenance Mode state, therefore when using this module with diff mode enabled, it may not accurately reflect a change.

## Status

### Authors
James Riach (@McGlovin1337)