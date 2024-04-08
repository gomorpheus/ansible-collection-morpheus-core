
.. Created with antsibull-docs 2.7.0

morpheus.core.appliance_settings module -- Configure Morpheus Appliance Settings
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.0).

It is not included in ``ansible-core``.
To check whether it is installed, run ``ansible-galaxy collection list``.

To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

To use it in a playbook, specify: ``morpheus.core.appliance_settings``.

New in morpheus.core 0.4.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Configures Morpheus Appliance Settings








Parameters
----------

.. raw:: html

  <table style="width: 100%;">
  <thead>
    <tr>
    <th><p>Parameter</p></th>
    <th><p>Comments</p></th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-appliance_url"></div>
      <p style="display: inline;"><strong>appliance_url</strong></p>
      <a class="ansibleOptionLink" href="#parameter-appliance_url" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Defines the URL of the Morpheus Appliance.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-cors_allowed"></div>
      <p style="display: inline;"><strong>cors_allowed</strong></p>
      <a class="ansibleOptionLink" href="#parameter-cors_allowed" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Define origins allowed to access the Morpheus API.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-currency_key"></div>
      <p style="display: inline;"><strong>currency_key</strong></p>
      <a class="ansibleOptionLink" href="#parameter-currency_key" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Set the API Key for the defined Currency Provider</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-currency_provider"></div>
      <p style="display: inline;"><strong>currency_provider</strong></p>
      <a class="ansibleOptionLink" href="#parameter-currency_provider" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Define a Currency Provider</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-default_role_id"></div>
      <p style="display: inline;"><strong>default_role_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-default_role_id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Set the default Tenant Role applied to new Tenant Registrations.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-default_user_role_id"></div>
      <p style="display: inline;"><strong>default_user_role_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-default_user_role_id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Set the default User Role applied the user created from Tenant Registration.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-disable_after_attempts"></div>
      <p style="display: inline;"><strong>disable_after_attempts</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disable_after_attempts" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Disable user account after this number of failed login attempts.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-disable_after_days_inactive"></div>
      <p style="display: inline;"><strong>disable_after_days_inactive</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disable_after_days_inactive" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Disable user account after this number of days of inactivity.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-disable_all_zone_types"></div>
      <p style="display: inline;"><strong>disable_all_zone_types</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disable_all_zone_types" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Disable All Cloud (Zone) Types</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-disable_zone_types"></div>
      <p style="display: inline;"><strong>disable_zone_types</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disable_zone_types" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify List of Cloud (Zone) Types to Disable</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-docker_privilged_mode"></div>
      <p style="display: inline;"><strong>docker_privilged_mode</strong></p>
      <a class="ansibleOptionLink" href="#parameter-docker_privilged_mode" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Enable or Disable Docker privileged mode.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-enable_all_zone_types"></div>
      <p style="display: inline;"><strong>enable_all_zone_types</strong></p>
      <a class="ansibleOptionLink" href="#parameter-enable_all_zone_types" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Enable All Cloud (Zone) Types</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-enable_zone_types"></div>
      <p style="display: inline;"><strong>enable_zone_types</strong></p>
      <a class="ansibleOptionLink" href="#parameter-enable_zone_types" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify List of Cloud (Zone) Types to Enable</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-expire_pwd_days"></div>
      <p style="display: inline;"><strong>expire_pwd_days</strong></p>
      <a class="ansibleOptionLink" href="#parameter-expire_pwd_days" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Expire passwords after this number of days. 0 disables this feature.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-internal_appliance_url"></div>
      <p style="display: inline;"><strong>internal_appliance_url</strong></p>
      <a class="ansibleOptionLink" href="#parameter-internal_appliance_url" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Defines the Internal URL of the Morpheus Appliance.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-password_min_length"></div>
      <p style="display: inline;"><strong>password_min_length</strong></p>
      <a class="ansibleOptionLink" href="#parameter-password_min_length" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Define the minimum length for passwords.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-password_min_numbers"></div>
      <p style="display: inline;"><strong>password_min_numbers</strong></p>
      <a class="ansibleOptionLink" href="#parameter-password_min_numbers" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Define the minimum number of numbers in passwords.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-password_min_symbols"></div>
      <p style="display: inline;"><strong>password_min_symbols</strong></p>
      <a class="ansibleOptionLink" href="#parameter-password_min_symbols" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Define the minimum number of symbols in passwords.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-password_min_upper_case"></div>
      <p style="display: inline;"><strong>password_min_upper_case</strong></p>
      <a class="ansibleOptionLink" href="#parameter-password_min_upper_case" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Define the minimum number of upper case characters in passwords.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-proxy_domain"></div>
      <p style="display: inline;"><strong>proxy_domain</strong></p>
      <a class="ansibleOptionLink" href="#parameter-proxy_domain" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Set the Proxy Domain</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-proxy_host"></div>
      <p style="display: inline;"><strong>proxy_host</strong></p>
      <a class="ansibleOptionLink" href="#parameter-proxy_host" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Define a Proxy Server</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-proxy_password"></div>
      <p style="display: inline;"><strong>proxy_password</strong></p>
      <a class="ansibleOptionLink" href="#parameter-proxy_password" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Password to Authenticate with the define Proxy Server</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-proxy_port"></div>
      <p style="display: inline;"><strong>proxy_port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-proxy_port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Set the Proxy Server port</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-proxy_user"></div>
      <p style="display: inline;"><strong>proxy_user</strong></p>
      <a class="ansibleOptionLink" href="#parameter-proxy_user" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>User to Authenticate with the defined Proxy Server</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-proxy_workstation"></div>
      <p style="display: inline;"><strong>proxy_workstation</strong></p>
      <a class="ansibleOptionLink" href="#parameter-proxy_workstation" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Set the Proxy Workstation</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-registration_enabled"></div>
      <p style="display: inline;"><strong>registration_enabled</strong></p>
      <a class="ansibleOptionLink" href="#parameter-registration_enabled" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Enable new users to register a new tenant.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-smtp_mail_from"></div>
      <p style="display: inline;"><strong>smtp_mail_from</strong></p>
      <a class="ansibleOptionLink" href="#parameter-smtp_mail_from" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Set the SMTP Mail From address header</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-smtp_password"></div>
      <p style="display: inline;"><strong>smtp_password</strong></p>
      <a class="ansibleOptionLink" href="#parameter-smtp_password" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Password to Authenticate with the define SMTP Server</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-smtp_port"></div>
      <p style="display: inline;"><strong>smtp_port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-smtp_port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Set the SMTP Server Port to connect to</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-smtp_server"></div>
      <p style="display: inline;"><strong>smtp_server</strong></p>
      <a class="ansibleOptionLink" href="#parameter-smtp_server" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Set the SMTP Server to relay email through</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-smtp_ssl"></div>
      <p style="display: inline;"><strong>smtp_ssl</strong></p>
      <a class="ansibleOptionLink" href="#parameter-smtp_ssl" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Use SSL to connect to the defined SMTP Server</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-smtp_tls"></div>
      <p style="display: inline;"><strong>smtp_tls</strong></p>
      <a class="ansibleOptionLink" href="#parameter-smtp_tls" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Use TLS to connect to the defined SMTP Server</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-smtp_user"></div>
      <p style="display: inline;"><strong>smtp_user</strong></p>
      <a class="ansibleOptionLink" href="#parameter-smtp_user" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>User to Authenticate with the defined SMTP Server</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-user_browser_session_timeout"></div>
      <p style="display: inline;"><strong>user_browser_session_timeout</strong></p>
      <a class="ansibleOptionLink" href="#parameter-user_browser_session_timeout" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Define the period of time in minutes to logout an idle user session.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-user_browser_session_warning"></div>
      <p style="display: inline;"><strong>user_browser_session_warning</strong></p>
      <a class="ansibleOptionLink" href="#parameter-user_browser_session_warning" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Define the period of time in minutes to warn the user of session timeout.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-warn_user_days_before"></div>
      <p style="display: inline;"><strong>warn_user_days_before</strong></p>
      <a class="ansibleOptionLink" href="#parameter-warn_user_days_before" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Warn user this number of days before account is disabled.</p>
    </td>
  </tr>
  </tbody>
  </table>




Attributes
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Attribute
    - Support
    - Description

  * - .. _ansible_collections.morpheus.core.appliance_settings_module__attribute-check_mode:

      **check_mode**

    - Support: full



    - 
      Can run in check\_mode and return changed status prediction without modifying target



  * - .. _ansible_collections.morpheus.core.appliance_settings_module__attribute-diff_mode:

      **diff_mode**

    - Support: full



    - 
      Will return details on what has changed (or possibly needs changing in check\_mode), when in diff mode



  * - .. _ansible_collections.morpheus.core.appliance_settings_module__attribute-platform:

      **platform**

    - Platforms:


    - 
      Target OS/families that can be operated against






Examples
--------

.. code-block:: yaml

    
    - name: Configure SMTP Settings
      morpheus.core.appliance_settings:
        smtp_server: smtp.domain.tld
        smtp_port: 25
        smtp_tls: true

    - name: Set Appliance URL
      morpheus.core.appliance_settings:
        appliance_url: cmp.domain.tld





Return Values
-------------
The following are the fields unique to this module:

.. raw:: html

  <table style="width: 100%;">
  <thead>
    <tr>
    <th><p>Key</p></th>
    <th><p>Description</p></th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="return-appliance_settings"></div>
      <p style="display: inline;"><strong>appliance_settings</strong></p>
      <a class="ansibleOptionLink" href="#return-appliance_settings" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>The current Morpheus Appliance Settings</p>
      <p style="margin-top: 8px;"><b>Returned:</b> success</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;appliance_settings&#34;: {&#34;appliance_url&#34;: &#34;https://cmp.domain.tld&#34;, &#34;cors_allowed&#34;: null, &#34;currency_key&#34;: null, &#34;currency_provider&#34;: null, &#34;default_role_id&#34;: null, &#34;default_user_role_id&#34;: null, &#34;disable_after_attempts&#34;: &#34;5&#34;, &#34;disable_after_days_inactive&#34;: null, &#34;docker_privileged_mode&#34;: false, &#34;enabled_zone_types&#34;: [{&#34;id&#34;: 4, &#34;name&#34;: &#34;Amazon&#34;}, {&#34;id&#34;: 9, &#34;name&#34;: &#34;Azure (Public)&#34;}, {&#34;id&#34;: 11, &#34;name&#34;: &#34;DigitalOcean&#34;}, {&#34;id&#34;: 3, &#34;name&#34;: &#34;Morpheus&#34;}, {&#34;id&#34;: 18, &#34;name&#34;: &#34;Oracle Public Cloud&#34;}, {&#34;id&#34;: 40, &#34;name&#34;: &#34;PowerVC&#34;}, {&#34;id&#34;: 17, &#34;name&#34;: &#34;UpCloud&#34;}, {&#34;id&#34;: 38, &#34;name&#34;: &#34;VMware Fusion&#34;}, {&#34;id&#34;: 28, &#34;name&#34;: &#34;VMware vCenter&#34;}, {&#34;id&#34;: 34, &#34;name&#34;: &#34;vCloud Director&#34;}], &#34;expire_pwd_days&#34;: null, &#34;internal_appliance_url&#34;: null, &#34;maintenance_mode&#34;: false, &#34;proxy_domain&#34;: null, &#34;proxy_host&#34;: null, &#34;proxy_password&#34;: null, &#34;proxy_password_hash&#34;: null, &#34;proxy_port&#34;: null, &#34;proxy_user&#34;: null, &#34;proxy_workstation&#34;: null, &#34;registration_enabled&#34;: false, &#34;smtp_mail_from&#34;: &#34;morpheus@domain.tld&#34;, &#34;smtp_password&#34;: null, &#34;smtp_password_hash&#34;: null, &#34;smtp_port&#34;: &#34;25&#34;, &#34;smtp_server&#34;: &#34;smtp.domain.tld&#34;, &#34;smtp_ssl&#34;: false, &#34;smtp_tls&#34;: true, &#34;smtp_user&#34;: null, &#34;stats_retainment_period&#34;: null, &#34;warn_user_days_before&#34;: null}}</code></p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="return-success"></div>
      <p style="display: inline;"><strong>success</strong></p>
      <a class="ansibleOptionLink" href="#return-success" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>If the API Request was Successful</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;success&#34;: true}</code></p>
    </td>
  </tr>
  </tbody>
  </table>




Authors
~~~~~~~

- James Riach



Collection links
~~~~~~~~~~~~~~~~

* `Repository (Sources) <https://www.github.com/gomorpheus/ansible-collection-morpheus-core>`__

