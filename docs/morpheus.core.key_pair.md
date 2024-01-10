# morpheus.core.key_pair
Create and Remove Key Pairs.
Key Pairs can be user provided or generated.

## Parameters

|Parameter|Choices/Defaults|Comments|
|---|---|---|
|state|Choices:<br/><ul><li>absent</li><li>present &larr;(default)</li></ul>|Create or Remove a Key Pair|
|id||Required when `state=absent`, specify the Key Pair to remove|
|name||Required when `state=present`, specify the name of the Key Pair<br/>Specifying this parameter on its own will generate a Key Pair|
|private_key||Specify the Private Key in PEM format|
|public_key||Specify the Public Key|
|passphrase||Specify the Private Key passphrase|

## Attributes

|Attribute|Support|Comments|
|---|---|---|
|check_mode|None|Does not support ```check_mode```|
|diff_mode|Full|Will return what has changed|

## Examples

```yaml
- name: Generate a Key Pair
  morpheus.core.key_pair:
    state: present
    name: My Generated Key Pair

- name: Add a Key Pair
  morpheus.core.key_pair:
    state: present
    name: My Existing Key Pair
    private_key: "{{ q('ansible.builtin.file', 'path/to/private_key')[0] }}"
    public_key: "{{ q('ansible.builtin.file', 'path/to/public_key)[0] }}"
    passphrase: Password123

- name: Delete a Key Pair
  morpheus.core.key_pair:
    state: absent
    id: 50
```

## Return Values

|Key|Returned|Description|
|---|---|---|
|key_pair|always|Dictionary information about the Key Pair.<br/>If this was a Generated Key Pair, it will include details of the Private Key.|

## Status

### Authors
James Riach (@McGlovin1337)
