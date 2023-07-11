# morpheus.core.appliance_facts
Gather facts about the target Morpheus Appliance(s)

## Parameters

|Parameter|Choices/Defaults|Comments|
|---|---|---|
|filter||Match facts to one of the specified patterns.|
|gather_subset||Specify or restrict the facts that are gathered.<br />Possible values: `all`, `database`, `elastic`, `license`, `rabbitmq`, `settings`, `system`.<br />To specify a specific subset, use (`!all`, `!min`) and then specify the fact(s) required.|
|gather_timeout||Timeout period for collecting individual facts|

## Attributes

|Attribute|Support|Comments|
|---|---|---|
|check_mode|Full|Can run in `check_mode` and predict changed status without performing any modifications|
|diff_mode|None|Will return what has changed (or needs changing when run with `check_mode`)|
|facts|Full|Action returns an `ansible_facts` dictionary that will update existing host facts|

## Examples

```yaml
- name: Gather All Facts
  morpheus.core.appliance_facts:

- name: Gather Minimum Facts
  morpheus.core.appliance_facts:
    gather_subset:
      - "!all"

- name: Gather License Facts
  morpheus.core.appliance_facts:
    gather_subset:
      - "!all"
      - "!min"
      - "license"
```

## Status

### Authors
James Riach (@McGlovin1337)