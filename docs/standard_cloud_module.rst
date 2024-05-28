
.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.9.0

.. Anchors

.. _ansible_collections.morpheus.core.standard_cloud_module:

.. Anchors: short name for ansible.builtin

.. Title

morpheus.core.standard_cloud module -- Manage a Standard Morpheus Cloud
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.1).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

    To use it in a playbook, specify: :code:`morpheus.core.standard_cloud`.

.. version_added

.. rst-class:: ansible-version-added

New in morpheus.core 0.7.0

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Manage Standard Morpheus Clouds.


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
        <div class="ansibleOptionAnchor" id="parameter-account_id"></div>
        <div class="ansibleOptionAnchor" id="parameter-tenant_id"></div>

      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-account_id:
      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-tenant_id:

      .. rst-class:: ansible-option-title

      **account_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-account_id" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-aliases:`aliases: tenant_id`

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Set the tenant for which Cloud is assigned to.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-agent_mode"></div>

      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-agent_mode:

      .. rst-class:: ansible-option-title

      **agent_mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-agent_mode" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Agent Install Mode.

      \ :ansval:`cloudinit`\  and \ :ansval:`unattend`\  are the same.

      \ :ansval:`guestexec`\ , \ :ansval:`ssh`\  and \ :ansval:`winrm`\  are the same.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"cloudinit"`
      - :ansible-option-choices-entry:`"guestexec"`
      - :ansible-option-choices-entry:`"ssh"`
      - :ansible-option-choices-entry:`"winrm"`
      - :ansible-option-choices-entry:`"unattend"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-appliance_url"></div>

      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-appliance_url:

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

      URL of the Morpheus Appliance.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-auto_recover_power_state"></div>

      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-auto_recover_power_state:

      .. rst-class:: ansible-option-title

      **auto_recover_power_state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-auto_recover_power_state" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Automatically Power-on Virtual Machines.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-code"></div>

      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-code:

      .. rst-class:: ansible-option-title

      **code**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-code" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The code to reference the Cloud for use in polcies etc.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-costing_mode"></div>
        <div class="ansibleOptionAnchor" id="parameter-costing"></div>

      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-costing:
      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-costing_mode:

      .. rst-class:: ansible-option-title

      **costing_mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-costing_mode" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-aliases:`aliases: costing`

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable costing on the Cloud.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"off"`
      - :ansible-option-choices-entry:`"costing"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-dark_logo"></div>

      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-dark_logo:

      .. rst-class:: ansible-option-title

      **dark_logo**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-dark_logo" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Path to an image file to use as the Cloud logo when in dark mode.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-datacenter_name"></div>

      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-datacenter_name:

      .. rst-class:: ansible-option-title

      **datacenter_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-datacenter_name" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Custom Datacenter Identifier.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-description"></div>

      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-description:

      .. rst-class:: ansible-option-title

      **description**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-description" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Set the description of the Cloud.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-enable_network_type_selection"></div>

      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-enable_network_type_selection:

      .. rst-class:: ansible-option-title

      **enable_network_type_selection**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-enable_network_type_selection" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable user to select the Network Interface type.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-enabled"></div>

      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-enabled:

      .. rst-class:: ansible-option-title

      **enabled**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-enabled" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable \ :ansopt:`morpheus.core.standard\_cloud#module:enabled=true`\  or Disable \ :ansopt:`morpheus.core.standard\_cloud#module:enabled=false`\  the Cloud.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-force_remove"></div>

      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-force_remove:

      .. rst-class:: ansible-option-title

      **force_remove**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-force_remove" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Force removal if Cloud is still in a group.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-group_id"></div>

      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-group_id:

      .. rst-class:: ansible-option-title

      **group_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-group_id" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Set the Cloud Group this Cloud is a member of.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-guidance_mode"></div>
        <div class="ansibleOptionAnchor" id="parameter-guidance"></div>

      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-guidance:
      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-guidance_mode:

      .. rst-class:: ansible-option-title

      **guidance_mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-guidance_mode" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-aliases:`aliases: guidance`

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Enable/Disable Cloud Guidance


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"off"`
      - :ansible-option-choices-entry:`"manual"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id"></div>
        <div class="ansibleOptionAnchor" id="parameter-cloud_id"></div>
        <div class="ansibleOptionAnchor" id="parameter-zone_id"></div>

      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-cloud_id:
      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-id:
      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-zone_id:

      .. rst-class:: ansible-option-title

      **id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-id" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-aliases:`aliases: cloud_id, zone_id`

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Specify an existing Cloud to Update or Remove.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-import_existing"></div>

      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-import_existing:

      .. rst-class:: ansible-option-title

      **import_existing**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-import_existing" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Inventory Cloud and Import existing Virtual Machines.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-location"></div>

      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-location:

      .. rst-class:: ansible-option-title

      **location**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-location" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Add location information for the Cloud.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-logo"></div>

      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-logo:

      .. rst-class:: ansible-option-title

      **logo**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-logo" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Path to an image file to use as the Cloud logo.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-name"></div>

      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-name:

      .. rst-class:: ansible-option-title

      **name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Set the name of the Cloud.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-refresh_mode"></div>

      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-refresh_mode:

      .. rst-class:: ansible-option-title

      **refresh_mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-refresh_mode" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The type of refresh to perform.

      \ :ansval:`costing`\  Pull costing data.

      \ :ansval:`costing\_rebuild`\  Purge existing costing data and rebuild by calling the Cloud API.

      \ :ansval:`daily`\  Perform a daily Cloud Sync.

      \ :ansval:`hourly`\  Perform hourly Cloud Sync.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"costing"`
      - :ansible-option-choices-entry:`"costing\_rebuild"`
      - :ansible-option-choices-entry:`"daily"`
      - :ansible-option-choices-entry-default:`"hourly"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-refresh_period"></div>

      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-refresh_period:

      .. rst-class:: ansible-option-title

      **refresh_period**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-refresh_period" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The invoice billing period to refresh.

      The value should be in the format of YYYYMM.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-remove_resources"></div>

      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-remove_resources:

      .. rst-class:: ansible-option-title

      **remove_resources**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-remove_resources" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Relevant when \ :ansopt:`morpheus.core.standard\_cloud#module:state=absent`\ , remove associated resources when removing the cloud.

      Includes removal of Virtual Machines and other forms of Compute.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-scale_priority"></div>

      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-scale_priority:

      .. rst-class:: ansible-option-title

      **scale_priority**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-scale_priority" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Set Scale Priority.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-security_mode"></div>

      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-security_mode:

      .. rst-class:: ansible-option-title

      **security_mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-security_mode" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Host firewall.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"off"`
      - :ansible-option-choices-entry:`"internal"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-state:

      .. rst-class:: ansible-option-title

      **state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Create, Update or Remove a Cloud.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"present"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"absent"`
      - :ansible-option-choices-entry:`"refresh"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-timezone"></div>

      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-timezone:

      .. rst-class:: ansible-option-title

      **timezone**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-timezone" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The Time Zone of the Cloud.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-visibility"></div>

      .. _ansible_collections.morpheus.core.standard_cloud_module__parameter-visibility:

      .. rst-class:: ansible-option-title

      **visibility**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-visibility" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Toggle tenant visibility between Private or Public.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"private"`
      - :ansible-option-choices-entry:`"public"`


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

      .. _ansible_collections.morpheus.core.standard_cloud_module__attribute-check_mode:

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

      .. _ansible_collections.morpheus.core.standard_cloud_module__attribute-diff_mode:

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

      .. _ansible_collections.morpheus.core.standard_cloud_module__attribute-platform:

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

    
    - name: Create Standard Cloud
      morpheus.core.standard_cloud:
        state: present
        name: Std Cloud
        description: Morpheus Std Cloud
        code: stdcloud
        location: everywhere
        auto_recover_power_state: false
        guidance: off
        costing: off
        group_id: 200
        account_id: 1
        timezone: Europe/London
        import_existing: false
        enable_network_type_selection: true
        agent_mode: cloudinit

    - name: Remove Standard Cloud
      morpheus.core.standard_cloud:
        state: absent
        name: Std Cloud
        force_remove: true

    - name: Refresh Cloud
      morpheus.core.standard_cloud:
        state: refresh
        name: Std Cloud
        refresh_mode: daily




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
        <div class="ansibleOptionAnchor" id="return-cloud"></div>

      .. _ansible_collections.morpheus.core.standard_cloud_module__return-cloud:

      .. rst-class:: ansible-option-title

      **cloud**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-cloud" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Information related to the specified cloud.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"cloud": {"account": {"id": 1, "name": "MasterTenant"}, "account\_id": 1, "agent\_mode": "cloudInit", "api\_proxy": null, "auto\_recover\_power\_state": false, "code": "stdcloud", "config": {"appliance\_url": null, "config\_cmdb\_discovery": false, "datacenter\_name": null, "enable\_network\_type\_selection": true, "import\_existing": false}, "console\_keymap": null, "container\_mode": "docker", "cost\_last\_sync": null, "cost\_last\_sync\_duration": null, "cost\_status": "ok", "cost\_status\_date": null, "cost\_status\_message": null, "costing\_mode": "off", "credential": {"type": "local"}, "dark\_image\_path": null, "date\_created": "2024-01-01T00:00:01Z", "domain\_name": "localdomain", "enabled": true, "external\_id": null, "groups": [{"account\_id": 1, "id": 200, "name": "STD Group"}], "guidance\_mode": "off", "id": 60, "image\_path": null, "inventory\_level": "off", "last\_sync": null, "last\_sync\_duration": null, "last\_updated": "2024-01-01T00:00:01Z", "location": "everywhere", "name": "Std Cloud", "network\_domain": null, "network\_server": null, "next\_run\_date": null, "owner": {"id": 1, "name": "MasterTenant"}, "provisioning\_proxy": null, "region\_code": null, "scale\_priority": 1, "security\_mode": "off", "security\_server": null, "server\_count": 0, "service\_version": null, "stats": {"server\_counts": {"all": 0, "baremetal": 0, "container\_host": 0, "host": 0, "hypervisor": 0, "unmanaged": 0, "vm": 0}}, "status": "initializing", "status\_date": null, "status\_message": null, "storage\_mode": "standard", "timezone": "Europe/London", "user\_data\_linux": null, "user\_data\_windows": null, "visibility": "private", "zone\_type": {"code": "standard", "id": 3, "name": "Morpheus"}, "zone\_type\_id": 3}}`


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

