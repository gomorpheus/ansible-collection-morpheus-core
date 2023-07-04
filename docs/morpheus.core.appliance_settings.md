# morpheus.core.appliance_settings
Configure Morpheus Appliance Settings

## Parameters

|Parameter|Choices/Defaults|Comments|
|---|---|---|
|appliance_url||Defines the URL of the Morpheus Appliance|
|internal_appliance_url||Defines the Internal URL of the Morpheus Appliance|
|cors_allowed||Define origins allowed to access the Morpheus API|
|registration_enabled|Choices:<br/> <ul><li>true</li><li>false</li></ul>|Enable new users to register a new tenant|
|default_role_id||Set the default Tenant Role applied to new Tenant Registrations|
|default_user_role_id||Set the default User Role applied the user created from Tenant Registration|
|docker_privilged_mode|Choices:<br/> <ul><li>true</li><li>false</li></ul>|Enable or Disable Docker privileged mode|
|password_min_length||Define the minimum length for passwords|
|password_min_upper_case||Define the minimum number of upper case characters in passwords|
|password_min_numbers||Define the minimum number of numbers in passwords|
|password_min_symbols||Define the minimum number of symbols in passwords|
|user_browser_session_timeout||Define the period of time in minutes to logout an idle user session|
|user_browser_session_warning||Define the period of time in minutes to warn the user of session timeout|
|expire_pwd_days||Expire passwords after this number of days. 0 disables this feature|
|disable_after_attempts||Disable user account after this number of failed login attempts|
|disable_after_days_inactive||Disable user account after this number of days of inactivity|
|warn_user_days_before||Warn user this number of days before account is disabled|
|smtp_mail_from||Set the SMTP Mail From address header|
|smtp_server||Set the SMTP Server to relay email through|
|smtp_port||Set the SMTP Server Port to connect to|
|smtp_ssl||Use SSL to connect to the defined SMTP Server|
|smtp_tls||Use TLS to connect to the defined SMTP Server|
|smtp_user||User to Authenticate with the defined SMTP Server|
|smtp_password||Password to Authenticate with the define SMTP Server|
|proxy_host||Define a Proxy Server|
|proxy_port||Set the Proxy Server port|
|proxy_user||User to Authenticate with the defined Proxy Server|
|proxy_password||Password to Authenticate with the define Proxy Server|
|proxy_domain||Set the Proxy Domain|
|proxy_workstation||Set the Proxy Workstation|
|currency_provider||Define a Currency Provider|
|currency_key||Set the API Key for the defined Currency Provider|
|enable_all_zone_types|Choices:<br/> <ul><li>true</li><li>false</li></ul>|Enable All Cloud (Zone) Types|
|enable_zone_types||Specify List of Cloud (Zone) Types to Enable|
|disable_zone_types||Specify List of Cloud (Zone) Types to Disable|
|disable_all_zone_types|Choices:<br/> <ul><li>true</li><li>false</li></ul>|Disable All Cloud (Zone) Types|
||||

## Attributes

|Attribute|Support|Comments|
|---|---|---|
|check_mode|Full|Can run in ```check_mode``` and predict changed status without performing any modifications|
|diff_mode|Full|Will return what has changed (or needs changing when run with ```check_mode```)|
||||

## Examples

```yaml
- name: Configure SMTP Server Settings
  morpheus.core.appliance_settings:
    smtp_server: smtp.domain.tld
    smtp_port: 25
    smtp_tls: true
    smtp_user: patrick.clifton
    smtp_pass: Black&WhiteC4tJess
    smtp_mail_from: postman.pat@domain.tld

- name: Enable All Cloud Types
  morpheus.core.appliance_settings:
    enable_all_zone_types: true
```

## Return Values

|Key|Returned|Description|
|---|---|---|
|success|always|If the API Request was Successful|
|appliance_settings|on success|Appliance Settings after successful API request|
||||

## Status

### Authors
James Riach (@McGlovin1337)