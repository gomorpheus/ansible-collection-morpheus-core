
.. Created with antsibull-docs 2.7.0

morpheus.core.group module -- Manage Groups
+++++++++++++++++++++++++++++++++++++++++++

This module is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.0).

It is not included in ``ansible-core``.
To check whether it is installed, run ``ansible-galaxy collection list``.

To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

To use it in a playbook, specify: ``morpheus.core.group``.

New in morpheus.core 0.7.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Create, Update and Remove Groups.








Parameters
----------

.. raw:: html

  <table style="width: 100%;">
  <thead>
    <tr>
    <th colspan="2"><p>Parameter</p></th>
    <th><p>Comments</p></th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-cm_id"></div>
      <p style="display: inline;"><strong>cm_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-cm_id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Id of a Change Management Integration.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-cmdb_discovery"></div>
      <p style="display: inline;"><strong>cmdb_discovery</strong></p>
      <a class="ansibleOptionLink" href="#parameter-cmdb_discovery" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Enable/Disable CMDB Discovery.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-cmdb_id"></div>
      <p style="display: inline;"><strong>cmdb_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-cmdb_id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Id of a CMDB Integration.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-code"></div>
      <p style="display: inline;"><strong>code</strong></p>
      <a class="ansibleOptionLink" href="#parameter-code" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Short Code name for the Group.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config_management_id"></div>
      <p style="display: inline;"><strong>config_management_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config_management_id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Id of a Configuration Management Integration.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-dns_id"></div>
      <p style="display: inline;"><strong>dns_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-dns_id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Id of a DNS Integration.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-id"></div>
      <p style="display: inline;"><strong>id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Id of an existing Group.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-labels"></div>
      <p style="display: inline;"><strong>labels</strong></p>
      <a class="ansibleOptionLink" href="#parameter-labels" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </td>
    <td valign="top">
      <p>List of Labels for the Group.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-location"></div>
      <p style="display: inline;"><strong>location</strong></p>
      <a class="ansibleOptionLink" href="#parameter-location" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Location information for the Group.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-name"></div>
      <p style="display: inline;"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Name of the Group.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-service_registry_id"></div>
      <p style="display: inline;"><strong>service_registry_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-service_registry_id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Id of a Service Registry Integration.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-state"></div>
      <p style="display: inline;"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p><code class="ansible-value literal notranslate">present</code> will create or update a Group, or <code class="ansible-value literal notranslate">absent</code> will remove a Group.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;absent&#34;</code></p></li>
        <li><p><code style="color: blue;"><b>&#34;present&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-zones"></div>
      <p style="display: inline;"><strong>zones</strong></p>
      <a class="ansibleOptionLink" href="#parameter-zones" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>Set the state of Clouds/Zones in this Group.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-zones/id"></div>
      <p style="display: inline;"><strong>id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-zones/id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td valign="top">
      <p>The Id of the Cloud/Zone.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-zones/state"></div>
      <p style="display: inline;"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-zones/state" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>The state of the Cloud/Zone in the Group.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;absent&#34;</code></p></li>
        <li><p><code style="color: blue;"><b>&#34;present&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

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

  * - .. _ansible_collections.morpheus.core.group_module__attribute-check_mode:

      **check_mode**

    - Support: full



    - 
      Can run in check\_mode and return changed status prediction without modifying target



  * - .. _ansible_collections.morpheus.core.group_module__attribute-diff_mode:

      **diff_mode**

    - Support: full



    - 
      Will return details on what has changed (or possibly needs changing in check\_mode), when in diff mode



  * - .. _ansible_collections.morpheus.core.group_module__attribute-platform:

      **platform**

    - Platforms:


    - 
      Target OS/families that can be operated against






Examples
--------

.. code-block:: yaml

    
    - name: Create/Update a Group
      morpheus.core.group:
        state: present
        name: MyGroup
        code: my_group
        location: Earth

    - name: Update Clouds/Zones in Group
      morpheus.core.group:
        state: present
        name: MyGroup
        zones:
          - state: present
            id: 17
          - state: present
            id: 18

    - name: Remove Group
      morpheus.core.group:
        state: absent
        name: MyGroup





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
      <div class="ansibleOptionAnchor" id="return-group"></div>
      <p style="display: inline;"><strong>group</strong></p>
      <a class="ansibleOptionLink" href="#return-group" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Group Information.</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;group&#34;: {&#34;account_id&#34;: 1, &#34;active&#34;: true, &#34;code&#34;: &#34;my_group&#34;, &#34;config&#34;: {&#34;config_cm_id&#34;: null, &#34;config_cmdb_discovery&#34;: false, &#34;config_cmdb_id&#34;: null, &#34;config_management_id&#34;: null, &#34;dns_integration_id&#34;: null, &#34;service_registry_id&#34;: null}, &#34;date_created&#34;: &#34;2024-01-01T00:00:01Z&#34;, &#34;id&#34;: 284, &#34;last_updated&#34;: &#34;2024-01-01T00:00:01Z&#34;, &#34;location&#34;: &#34;Earth&#34;, &#34;name&#34;: &#34;MyGroup&#34;, &#34;server_count&#34;: 0, &#34;stats&#34;: {&#34;instance_counts&#34;: {&#34;all&#34;: 0}, &#34;server_counts&#34;: {&#34;all&#34;: 0, &#34;baremetal&#34;: 0, &#34;container_host&#34;: 0, &#34;host&#34;: 0, &#34;hypervisor&#34;: 0, &#34;unmanaged&#34;: 0, &#34;vm&#34;: 0}}, &#34;zones&#34;: [{&#34;id&#34;: 17, &#34;name&#34;: &#34;MyCloud&#34;}]}}</code></p>
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

