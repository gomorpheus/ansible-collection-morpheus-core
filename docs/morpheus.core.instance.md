# morpheus.core.instance
Provides basic management of Morpheus Instances, such as setting running state, backup, deletion and lock status.

## Parameters

|Parameter|Choices/Defaults|Comments|
|---|---|---|
|id||Select instance by id.<br/>Mutually exclusive with `name`|
|name||Select instances by name.<br/>Mutually exclusive with `id`|
|regex_name||Treat the name parameter as a regular expression.|
|match_name|Choices:<br/> <ul><li>none &larr;(default)</li><li>first</li><li>last</li><li>all</li></ul>|Determines which instance(s) to match in the case that multiple instances match the name.<br />Defaults to `none` for safety.|
|state<br/>(required)|Choices:<br/> <ul><li>running</li><li>started</li><li>stopped</li><li>restarted</li><li>suspended</li><li>locked</li><li>unlocked</li><li>backup</li><li>absent</li><li>eject</li></ul>|Set the state/action for the instance(s).|
|remove_options||Dictionary of sub-options available when `state = absent`|
|preserve_volumes<br/>(remove_options)|Choices:<br/><ul><li>true</li><li>false &larr;(default)</li></ul>|Preserve the volumes of the removed instance|
|keep_backups<br/>(remove_options)|Choices:<br/><ul><li>true</li><li>false &larr;(default)</li></ul>|Keep backup copies of instance|
|release_floating_ips<br/>(remove_options)|Choices:<br/><ul><li>true</li><li>false &larr;(default)</li></ul>|Release floating IP Addresses|
|force<br/>(remove_options)|Choices:<br/><ul><li>true</li><li>false &larr;(default)</li></ul>|Force removal of instance|

## Attributes

|Attribute|Support|Comments|
|---|---|---|
|check_mode|Full|Can run in ```check_mode``` and predict changed status without performing any modifications|
|diff_mode|Partial|Will return what has changed (or needs changing when run with ```check_mode```)<br/>Not all states support diff mode|

## Examples

```yaml
- name: Restart a specific instance
  morpheus.core.instance:
    id: 200
    state: restarted

- name: Stop all instances matching regex name pattern
  morpheus.core.instance:
    name: ^PROD.*$
    regex_name: true
    match_name: all
    state: stopped

- name: Suspend the first instance that matches name
  morpheus.core.instance:
    name: PRODWEBSVR001
    match_name: first
    state: suspended

- name: Remove instance but keep backups
  morpheus.core.instance:
    name: PRODWEBSVR002
    match_name: first
    state: absent
    remove_options:
      keep_backups: true

- name: Backup all instances
  morpheus.core.instance:
    name: ^.*$
    regex_name: true
    match_name: all
    state: backup
```

## Return Values

|Key|Returned|Description|
|---|---|---|
|instance_state|always|State of the instance(s) following the requested action|

## Status

### Authors
James Riach (@McGlovin1337)