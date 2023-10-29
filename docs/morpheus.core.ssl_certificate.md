# morpheus.core.ssl_certificate
Manage SSL Certificates

## Parameters

|Parameter|Choices/Defaults|Comments|
|---|---|---|
|state|Choices:<br/><ul><li>absent</li><li>present &larr;(default)</li></ul>|Create, Update or Remove an SSL Certificate|
|id||Specify the SSL Certificate to remove|
|name||Specify the name of the SSL Certificate|
|domain_name||The Domain Name the SSL Certificate is responsible for|
|wildcard||Specify if the SSL Certificate is a wildcard certificate|
|certificate||The SSL Certificate contents|
|key||The SSL Certificate Private Key|

## Attributes

|Attribute|Support|Comments|
|---|---|---|
|check_mode|Full|Can run in ```check_mode``` and predict changed status without performing any modifications|
|diff_mode|Full|Will return what has changed (or needs changing when run with ```check_mode```)|

## Examples

```yaml
- name: Create SSL Certificate
  morpheus.core.ssl_certificate:
    state: present
    name: WebSvr SSL Cert
    domain_name: www.domain.tld
    wildcard: false
    certificate: "{{ q('ansible.builtin.file', '/path/to/cert.crt') }}"
    key: "{{ q('ansible.builtin.file', '/path/to/private_key.pem') }}"

- name: Remove SSL Certificate
  morpheus.core.ssl_certificate:
    state: absent
    name: WebSvr SSL Cert

- name: Change Name of SSL Certificate
  morpheus.core.ssl_certificate:
    id: 17
    name: New Name SSL Cert
```

## Return Values

|Key|Returned|Description|
|---|---|---|
|certificate|always|SSL Certificate details|

## Status

### Authors
James Riach (@McGlovin1337)
