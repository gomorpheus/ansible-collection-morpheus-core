
.. Created with antsibull-docs 2.7.0

morpheus.core.cloud_datastore module -- Configure Cloud Datastores
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.0).

It is not included in ``ansible-core``.
To check whether it is installed, run ``ansible-galaxy collection list``.

To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

To use it in a playbook, specify: ``morpheus.core.cloud_datastore``.

New in morpheus.core 0.7.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Update the configuration of Cloud Datastores.








Parameters
----------

.. raw:: html

  <table style="width: 100%;">
  <thead>
    <tr>
    <th colspan="3"><p>Parameter</p></th>
    <th><p>Comments</p></th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td colspan="3" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-id"></div>
      <p style="display: inline;"><strong>id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td valign="top">
      <p>The Id of the Datastore.</p>
    </td>
  </tr>
  <tr>
    <td colspan="3" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-resource_permissions"></div>
      <p style="display: inline;"><strong>resource_permissions</strong></p>
      <a class="ansibleOptionLink" href="#parameter-resource_permissions" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>Resource permissions for the Datastore.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-resource_permissions/all_groups"></div>
      <p style="display: inline;"><strong>all_groups</strong></p>
      <a class="ansibleOptionLink" href="#parameter-resource_permissions/all_groups" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Allow or disallow access to all groups.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-resource_permissions/all_plans"></div>
      <p style="display: inline;"><strong>all_plans</strong></p>
      <a class="ansibleOptionLink" href="#parameter-resource_permissions/all_plans" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Allow access to all plans.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-resource_permissions/groups"></div>
      <div class="ansibleOptionAnchor" id="parameter-resource_permissions/sites"></div>
      <p style="display: inline;"><strong>groups</strong></p>
      <a class="ansibleOptionLink" href="#parameter-resource_permissions/groups" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: sites</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>List of groups that are allowed access to the Datastore.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-resource_permissions/groups/group_id"></div>
      <div class="ansibleOptionAnchor" id="parameter-resource_permissions/sites/group_id"></div>
      <div class="ansibleOptionAnchor" id="parameter-resource_permissions/groups/site_id"></div>
      <div class="ansibleOptionAnchor" id="parameter-resource_permissions/sites/site_id"></div>
      <p style="display: inline;"><strong>group_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-resource_permissions/groups/group_id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: site_id</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Id of the group to allow access.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-resource_permissions/groups/state"></div>
      <div class="ansibleOptionAnchor" id="parameter-resource_permissions/sites/state"></div>
      <p style="display: inline;"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-resource_permissions/groups/state" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>If the Group should have access or not.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;absent&#34;</code></p></li>
        <li><p><code style="color: blue;"><b>&#34;present&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>

  <tr>
    <td></td>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-resource_permissions/plans"></div>
      <p style="display: inline;"><strong>plans</strong></p>
      <a class="ansibleOptionLink" href="#parameter-resource_permissions/plans" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>List of Plans to allow access.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-resource_permissions/plans/plan_id"></div>
      <p style="display: inline;"><strong>plan_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-resource_permissions/plans/plan_id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Id of the Plan to allow access.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-resource_permissions/plans/state"></div>
      <p style="display: inline;"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-resource_permissions/plans/state" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>If the plan should be present or not.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;absent&#34;</code></p></li>
        <li><p><code style="color: blue;"><b>&#34;present&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>


  <tr>
    <td colspan="3" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-state"></div>
      <p style="display: inline;"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>The active state of the Datastore.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;active&#34;</code></p></li>
        <li><p><code>&#34;inactive&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="3" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-tenant_permissions"></div>
      <p style="display: inline;"><strong>tenant_permissions</strong></p>
      <a class="ansibleOptionLink" href="#parameter-tenant_permissions" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>List of Tenant Permissions on the Datastore.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-tenant_permissions/default_store"></div>
      <p style="display: inline;"><strong>default_store</strong></p>
      <a class="ansibleOptionLink" href="#parameter-tenant_permissions/default_store" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Set the Datastore as the default image store for the specified tenant.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-tenant_permissions/default_target"></div>
      <p style="display: inline;"><strong>default_target</strong></p>
      <a class="ansibleOptionLink" href="#parameter-tenant_permissions/default_target" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Set the Datastore as the default for the specified tenant.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-tenant_permissions/state"></div>
      <p style="display: inline;"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-tenant_permissions/state" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>If the Account should have access or not.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;absent&#34;</code></p></li>
        <li><p><code style="color: blue;"><b>&#34;present&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-tenant_permissions/tenant_id"></div>
      <p style="display: inline;"><strong>tenant_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-tenant_permissions/tenant_id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>The id of the tenant to add or remove permissions for.</p>
    </td>
  </tr>

  <tr>
    <td colspan="3" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-visibility"></div>
      <p style="display: inline;"><strong>visibility</strong></p>
      <a class="ansibleOptionLink" href="#parameter-visibility" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>The visibility of the Datastore.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;private&#34;</code></p></li>
        <li><p><code>&#34;public&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="3" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-zone_id"></div>
      <div class="ansibleOptionAnchor" id="parameter-cloud_id"></div>
      <p style="display: inline;"><strong>zone_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-zone_id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: cloud_id</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td valign="top">
      <p>The Id of the Cloud the Datastore belongs to.</p>
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

  * - .. _ansible_collections.morpheus.core.cloud_datastore_module__attribute-check_mode:

      **check_mode**

    - Support: full



    - 
      Can run in check\_mode and return changed status prediction without modifying target



  * - .. _ansible_collections.morpheus.core.cloud_datastore_module__attribute-diff_mode:

      **diff_mode**

    - Support: full



    - 
      Will return details on what has changed (or possibly needs changing in check\_mode), when in diff mode



  * - .. _ansible_collections.morpheus.core.cloud_datastore_module__attribute-platform:

      **platform**

    - Platforms:


    - 
      Target OS/families that can be operated against






Examples
--------

.. code-block:: yaml

    
    - name: Set a Datastore to Active and Public Visibility
      morpheus.core.cloud_datastore:
        id: 30
        cloud_id: 5
        state: active
        visibility: public

    - name: Configure Tenant Access to Datastore
      morpheus.core.cloud_datastore:
        id: 30
        cloud_id: 5
        tenant_permissions:
            - state: present
              tenant_id: 50
              default_target: true
            - state: present
              tenant_id: 51
              default_target: true
              default_store: true
            - state: absent
              tenant_id: 2

    - name: Configure Group Access and Allow all Price Plans
      morpheus.core.cloud_datastore:
        id: 35
        cloud_id: 6
        resource_permissions:
            groups:
                - state: present
                  group_id: 7
            all_plans: true





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
      <div class="ansibleOptionAnchor" id="return-datastore"></div>
      <p style="display: inline;"><strong>datastore</strong></p>
      <a class="ansibleOptionLink" href="#return-datastore" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Information about the datastore after changes.</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;datastore&#34;: {&#34;active&#34;: true, &#34;free_space&#34;: 17589585575936, &#34;id&#34;: 100, &#34;name&#34;: &#34;vmfs01&#34;, &#34;online&#34;: true, &#34;resource_permission&#34;: {&#34;all&#34;: true, &#34;all_plans&#34;: false, &#34;plans&#34;: [], &#34;sites&#34;: []}, &#34;tenants&#34;: [{&#34;default_store&#34;: false, &#34;default_target&#34;: false, &#34;id&#34;: 1, &#34;name&#34;: &#34;MasterTenant&#34;}], &#34;type&#34;: &#34;vmfs&#34;, &#34;visibility&#34;: &#34;private&#34;, &#34;zone&#34;: {&#34;id&#34;: 20, &#34;name&#34;: &#34;VMware Cloud&#34;}}}</code></p>
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

