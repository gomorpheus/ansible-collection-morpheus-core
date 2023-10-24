# morpheus.core.key_pair_info
Gather Key Pair Information

## Parameters

|Parameter|Choices/Defaults|Comments|
|---|---|---|
|id||Specify the Id of a Key Pair|
|name||The name of the Key Pair|
|regex_name|Choices:<br/><ul><li>true</li><li>false &larr;(default)</li></ul>|Treat name Parameter as a Regular Expression|
|has_private_key|Choices:<br/><ul><li>true</li><li>false</li></ul>|Filter Key Pairs by whether they have a Private Key or not|

## Attributes

|Attribute|Support|Comments|
|---|---|---|
|check_mode|Full|Can run in ```check_mode``` and predict changed status without performing any modifications|

## Examples

```yaml
- name: Get Specific Key by Id
  morpheus.core.key_pair_info:
    id: 20

- name: Get Keys matching Regular Expression
  morpheus.core.key_pair_info:
    name: ^morpheus_.*$
    regex_name: true

- name: Get All Keys with Private Key
  morpheus.core.key_pair_info:
    has_private_key: true
```

## Return Values

|Key|Returned|Description|
|---|---|---|
|key_pairs|always|List of matching Key Pairs|

## Status

### Authors
James Riach (@McGlovin1337)
