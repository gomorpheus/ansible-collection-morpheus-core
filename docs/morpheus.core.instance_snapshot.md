# morpheus.core.instance_snapshot
Manage Morpheus Instance Snapshots

## Parameters

|Parameter|Choices/Defaults|Comments|
|---|---|---|
|id||Specify the id of an instance|
|name||Filter instances by name|
|regex_name|Choices:<br/> <ul><li>true</li><li>false &larr;(default)</li></ul>|Treat the name parameter as a regular expression|
|match_name|Choices:<br/> <ul><li>none &larr;(default)</li><li>first</li><li>last</li><li>all</li></ul>|Determines which instance(s) to match in the case that multiple instances match the name.<br />Defaults to `none` for safety.|
|state|Choices:<br/> <ul><li>absent</li><li>present &larr;(default)</li><li>revert</li><li>remove_all</li></ul>|Manage snapshot state|
|snapshot_id||Specify a snapshot by id, can be used with `state=absent` or `state=revert`|
|snapshot_name||Specify snapshot name <br/>Can be used with `state=absent`, `state=present`, `state=revert`|
|snapshot_description||Provide a description for snapshot when `state=present`|
|snapshot_age|Choices:<br/> <ul><li>latest &larr;(default)</li><li>oldest</li></ul>|If more than one snapshot matches parameters, which one to select based on age of snapshot|

## Attributes

|Attribute|Support|Comments|
|---|---|---|
|check_mode|Full|Can run in ```check_mode``` and predict changed status without performing any modifications|
|diff_mode|Full|Will return what has changed (or needs changing when run with ```check_mode```)|

## Examples

```yaml
- name: Snapshot All Instances
  morpheus.core.instance_snapshot:
    name: ^.*$
    match_name: all
    regex_name: true
    snapshot_name: Ansible Snapshot
    snapshot_description: Snapshot Created via Ansible
    state: present

- name: Remove All Snapshots for Specific Instance
  morpheus.core.instance_snapshot:
    id: 200
    state: remove_all

- name: Revert Instance to Oldest Snapshot matching Name
  morpheus.core.instance_snapshot:
    name: WebServer001
    snapshot_name: Ansible Snapshot
    snapshot_age: oldest
    state: revert

- name: Remove Specific Snapshot by Id
  morpheus.core.instance_snapshot:
    snapshot_id: 50
    state: absent

- name: Remove the Latest Snapshot matching Name for all Instances
  morpheus.core.instance_snapshot:
    name: ^.*$
    match_name: all
    regex_name: true
    snapshot_name: Ansible Snapshot
    state: absent
```

## Return Values

|Key|Returned|Description|
|---|---|---|
|snapshot_results|always|List of actions performed against the instances and snapshot(s)|

## Status

### Authors
James Riach (@McGlovin1337)