# Morpheus Settings

This role creates integrations in Morpheus.

## Variables

`morpheus_url` - Morpheus URL eg. `https://morpheus.example.com`

`morpheus_token` - Morpheus Access Token

`morpheus_integrations` - Provisioning settings to be applied.  Example in `defaults/main.yml`

Additional options in same format as in the API docs are supported: https://apidocs.morpheusdata.com/#integrations

## Currently Supported Integrations
- Git
- Ansible