# morpheus.core.ssl_certificate_info
Gather information about SSL Certificates

## Parameters

|Parameter|Choices/Defaults|Comments|
|---|---|---|
|id||The Id of a specific SSL Certificate|
|name||The name of an SSL Certificate|
|regex_name||Treat the name parameter as a Regular Expression|

## Attributes

|Attribute|Support|Comments|
|---|---|---|
|check_mode|Full|Can run in ```check_mode``` and predict changed status without performing any modifications|

## Examples

```yaml
- name: Get All SSL Certificates
  morpheus.core.ssl_certificate_info:

- name: Get Specific Certificate by Id
  morpheus.core.ssl_certificate_info:
    id: 20

- name: Get Certificates matching Regular Expression
  morpheus.core.ssl_certificate_info:
    name: ^Web.*$
    regex_name: true
```

## Return Values

|Key|Returned|Description|
|---|---|---|
|certificates|always|List of SSL Certificate details|

## Status

### Authors
James Riach (@McGlovin1337)
