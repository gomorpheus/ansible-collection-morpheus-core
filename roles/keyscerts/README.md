# Morpheus Keys and Certs

This role creates SSH Keys and Certificates in Morpheus.

## Variables

`morpheus_url` - Morpheus URL eg. `https://morpheus.example.com`

`morpheus_token` - Morpheus Access Token

`morpheus_keyscerts` - Keys to be created.  Private key is optional.  Example in `defaults/main.yml`

NOTE: SSH private keys must be unencrypted for use in Morpheus.  Use the following command to create compatible keys: `ssh-keygen -m PEM`

## Currently Supported
- SSH Keys