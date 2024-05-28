
.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.9.0

.. Anchors

.. _ansible_collections.morpheus.core.appliance_settings_module:

.. Anchors: short name for ansible.builtin

.. Title

morpheus.core.appliance_settings module -- Configure Morpheus Appliance Settings
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.1).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

    To use it in a playbook, specify: :code:`morpheus.core.appliance_settings`.

.. version_added

.. rst-class:: ansible-version-added

New in morpheus.core 0.4.0

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Configures Morpheus Appliance Settings


.. Aliases


.. Requirements






.. Options

Parameters
----------

.. tabularcolumns:: \X{1}{3}\X{2}{3}

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1
  :class: longtable ansible-option-table

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appliance_url"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-appliance_url:

      .. rst-class:: ansible-option-title

      **appliance_url**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-appliance_url" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Defines the URL of the Morpheus Appliance.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-cors_allowed"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-cors_allowed:

      .. rst-class:: ansible-option-title

      **cors_allowed**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cors_allowed" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Define origins allowed to access the Morpheus API.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-currency_key"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-currency_key:

      .. rst-class:: ansible-option-title

      **currency_key**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-currency_key" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Set the API Key for the defined Currency Provider


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-currency_provider"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-currency_provider:

      .. rst-class:: ansible-option-title

      **currency_provider**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-currency_provider" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Define a Currency Provider


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-default_role_id"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-default_role_id:

      .. rst-class:: ansible-option-title

      **default_role_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-default_role_id" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Set the default Tenant Role applied to new Tenant Registrations.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-default_user_role_id"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-default_user_role_id:

      .. rst-class:: ansible-option-title

      **default_user_role_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-default_user_role_id" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Set the default User Role applied the user created from Tenant Registration.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable_after_attempts"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-disable_after_attempts:

      .. rst-class:: ansible-option-title

      **disable_after_attempts**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable_after_attempts" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Disable user account after this number of failed login attempts.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable_after_days_inactive"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-disable_after_days_inactive:

      .. rst-class:: ansible-option-title

      **disable_after_days_inactive**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable_after_days_inactive" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Disable user account after this number of days of inactivity.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable_all_zone_types"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-disable_all_zone_types:

      .. rst-class:: ansible-option-title

      **disable_all_zone_types**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable_all_zone_types" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Disable All Cloud (Zone) Types


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-disable_zone_types"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-disable_zone_types:

      .. rst-class:: ansible-option-title

      **disable_zone_types**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-disable_zone_types" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Specify List of Cloud (Zone) Types to Disable


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-docker_privileged_mode"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-docker_privileged_mode:

      .. rst-class:: ansible-option-title

      **docker_privileged_mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-docker_privileged_mode" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable or Disable Docker privileged mode.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-enable_all_zone_types"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-enable_all_zone_types:

      .. rst-class:: ansible-option-title

      **enable_all_zone_types**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-enable_all_zone_types" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable All Cloud (Zone) Types


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-enable_zone_types"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-enable_zone_types:

      .. rst-class:: ansible-option-title

      **enable_zone_types**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-enable_zone_types" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Specify List of Cloud (Zone) Types to Enable


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-expire_pwd_days"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-expire_pwd_days:

      .. rst-class:: ansible-option-title

      **expire_pwd_days**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-expire_pwd_days" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Expire passwords after this number of days. 0 disables this feature.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-internal_appliance_url"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-internal_appliance_url:

      .. rst-class:: ansible-option-title

      **internal_appliance_url**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-internal_appliance_url" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Defines the Internal URL of the Morpheus Appliance.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password_min_length"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-password_min_length:

      .. rst-class:: ansible-option-title

      **password_min_length**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-password_min_length" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Define the minimum length for passwords.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password_min_numbers"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-password_min_numbers:

      .. rst-class:: ansible-option-title

      **password_min_numbers**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-password_min_numbers" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Define the minimum number of numbers in passwords.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password_min_symbols"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-password_min_symbols:

      .. rst-class:: ansible-option-title

      **password_min_symbols**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-password_min_symbols" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Define the minimum number of symbols in passwords.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password_min_upper_case"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-password_min_upper_case:

      .. rst-class:: ansible-option-title

      **password_min_upper_case**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-password_min_upper_case" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Define the minimum number of upper case characters in passwords.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-proxy_domain"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-proxy_domain:

      .. rst-class:: ansible-option-title

      **proxy_domain**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-proxy_domain" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Set the Proxy Domain


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-proxy_host"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-proxy_host:

      .. rst-class:: ansible-option-title

      **proxy_host**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-proxy_host" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Define a Proxy Server


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-proxy_password"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-proxy_password:

      .. rst-class:: ansible-option-title

      **proxy_password**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-proxy_password" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Password to Authenticate with the define Proxy Server


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-proxy_port"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-proxy_port:

      .. rst-class:: ansible-option-title

      **proxy_port**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-proxy_port" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Set the Proxy Server port


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-proxy_user"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-proxy_user:

      .. rst-class:: ansible-option-title

      **proxy_user**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-proxy_user" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      User to Authenticate with the defined Proxy Server


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-proxy_workstation"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-proxy_workstation:

      .. rst-class:: ansible-option-title

      **proxy_workstation**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-proxy_workstation" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Set the Proxy Workstation


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-registration_enabled"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-registration_enabled:

      .. rst-class:: ansible-option-title

      **registration_enabled**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-registration_enabled" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable new users to register a new tenant.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-smtp_mail_from"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-smtp_mail_from:

      .. rst-class:: ansible-option-title

      **smtp_mail_from**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-smtp_mail_from" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Set the SMTP Mail From address header


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-smtp_password"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-smtp_password:

      .. rst-class:: ansible-option-title

      **smtp_password**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-smtp_password" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Password to Authenticate with the define SMTP Server


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-smtp_port"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-smtp_port:

      .. rst-class:: ansible-option-title

      **smtp_port**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-smtp_port" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Set the SMTP Server Port to connect to


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-smtp_server"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-smtp_server:

      .. rst-class:: ansible-option-title

      **smtp_server**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-smtp_server" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Set the SMTP Server to relay email through


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-smtp_ssl"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-smtp_ssl:

      .. rst-class:: ansible-option-title

      **smtp_ssl**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-smtp_ssl" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Use SSL to connect to the defined SMTP Server


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-smtp_tls"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-smtp_tls:

      .. rst-class:: ansible-option-title

      **smtp_tls**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-smtp_tls" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Use TLS to connect to the defined SMTP Server


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-smtp_user"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-smtp_user:

      .. rst-class:: ansible-option-title

      **smtp_user**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-smtp_user" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      User to Authenticate with the defined SMTP Server


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-user_browser_session_timeout"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-user_browser_session_timeout:

      .. rst-class:: ansible-option-title

      **user_browser_session_timeout**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-user_browser_session_timeout" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Define the period of time in minutes to logout an idle user session.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-user_browser_session_warning"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-user_browser_session_warning:

      .. rst-class:: ansible-option-title

      **user_browser_session_warning**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-user_browser_session_warning" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Define the period of time in minutes to warn the user of session timeout.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-warn_user_days_before"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__parameter-warn_user_days_before:

      .. rst-class:: ansible-option-title

      **warn_user_days_before**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-warn_user_days_before" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Warn user this number of days before account is disabled.


      .. raw:: html

        </div>


.. Attributes


Attributes
----------

.. tabularcolumns:: \X{2}{10}\X{3}{10}\X{5}{10}

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1
  :class: longtable ansible-option-table

  * - Attribute
    - Support
    - Description

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="attribute-check_mode"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__attribute-check_mode:

      .. rst-class:: ansible-option-title

      **check_mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#attribute-check_mode" title="Permalink to this attribute"></a>

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      :ansible-attribute-support-label:`Support: \ `\ :ansible-attribute-support-full:`full`


      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Can run in check\_mode and return changed status prediction without modifying target


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="attribute-diff_mode"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__attribute-diff_mode:

      .. rst-class:: ansible-option-title

      **diff_mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#attribute-diff_mode" title="Permalink to this attribute"></a>

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      :ansible-attribute-support-label:`Support: \ `\ :ansible-attribute-support-full:`full`


      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Will return details on what has changed (or possibly needs changing in check\_mode), when in diff mode


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="attribute-platform"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__attribute-platform:

      .. rst-class:: ansible-option-title

      **platform**

      .. raw:: html

        <a class="ansibleOptionLink" href="#attribute-platform" title="Permalink to this attribute"></a>

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      :ansible-attribute-support-property:`Platform:` |antsibull-internal-nbsp|:ansible-attribute-support-full:`httpapi`


      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Target OS/families that can be operated against


      .. raw:: html

        </div>



.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Configure SMTP Settings
      morpheus.core.appliance_settings:
        smtp_server: smtp.domain.tld
        smtp_port: 25
        smtp_tls: true

    - name: Set Appliance URL
      morpheus.core.appliance_settings:
        appliance_url: cmp.domain.tld




.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. tabularcolumns:: \X{1}{3}\X{2}{3}

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1
  :class: longtable ansible-option-table

  * - Key
    - Description

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-appliance_settings"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__return-appliance_settings:

      .. rst-class:: ansible-option-title

      **appliance_settings**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-appliance_settings" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The current Morpheus Appliance Settings


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"appliance\_settings": {"appliance\_url": "https://cmp.domain.tld", "cors\_allowed": null, "currency\_key": null, "currency\_provider": null, "default\_role\_id": null, "default\_user\_role\_id": null, "disable\_after\_attempts": "5", "disable\_after\_days\_inactive": null, "docker\_privileged\_mode": false, "enabled\_zone\_types": [{"id": 4, "name": "Amazon"}, {"id": 9, "name": "Azure (Public)"}, {"id": 11, "name": "DigitalOcean"}, {"id": 3, "name": "Morpheus"}, {"id": 18, "name": "Oracle Public Cloud"}, {"id": 40, "name": "PowerVC"}, {"id": 17, "name": "UpCloud"}, {"id": 38, "name": "VMware Fusion"}, {"id": 28, "name": "VMware vCenter"}, {"id": 34, "name": "vCloud Director"}], "expire\_pwd\_days": null, "internal\_appliance\_url": null, "maintenance\_mode": false, "proxy\_domain": null, "proxy\_host": null, "proxy\_password": null, "proxy\_password\_hash": null, "proxy\_port": null, "proxy\_user": null, "proxy\_workstation": null, "registration\_enabled": false, "smtp\_mail\_from": "morpheus@domain.tld", "smtp\_password": null, "smtp\_password\_hash": null, "smtp\_port": "25", "smtp\_server": "smtp.domain.tld", "smtp\_ssl": false, "smtp\_tls": true, "smtp\_user": null, "stats\_retainment\_period": null, "warn\_user\_days\_before": null}}`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-success"></div>

      .. _ansible_collections.morpheus.core.appliance_settings_module__return-success:

      .. rst-class:: ansible-option-title

      **success**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-success" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If the API Request was Successful


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"success": true}`


      .. raw:: html

        </div>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- James Riach (@McGlovin1337)



.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. ansible-links::

  - title: "Repository (Sources)"
    url: "https://www.github.com/gomorpheus/ansible-collection-morpheus-core"
    external: true


.. Parsing errors

