
.. Created with antsibull-docs 2.7.0

morpheus.core.vcenter_cloud module -- Manage a VMware VCenter Cloud
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.0).

It is not included in ``ansible-core``.
To check whether it is installed, run ``ansible-galaxy collection list``.

To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

To use it in a playbook, specify: ``morpheus.core.vcenter_cloud``.

New in morpheus.core 0.7.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Manage VMware VCenter Clouds.








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
      <div class="ansibleOptionAnchor" id="parameter-account_id"></div>
      <div class="ansibleOptionAnchor" id="parameter-tenant_id"></div>
      <p style="display: inline;"><strong>account_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-account_id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: tenant_id</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Set the tenant for which Cloud is assigned to.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-agent_mode"></div>
      <p style="display: inline;"><strong>agent_mode</strong></p>
      <a class="ansibleOptionLink" href="#parameter-agent_mode" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Agent Install Mode.</p>
      <p><code class="ansible-value literal notranslate">cloudinit</code> and <code class="ansible-value literal notranslate">unattend</code> are the same.</p>
      <p><code class="ansible-value literal notranslate">guestexec</code>, <code class="ansible-value literal notranslate">ssh</code> and <code class="ansible-value literal notranslate">winrm</code> are the same.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;cloudinit&#34;</code></p></li>
        <li><p><code>&#34;guestexec&#34;</code></p></li>
        <li><p><code>&#34;ssh&#34;</code></p></li>
        <li><p><code>&#34;winrm&#34;</code></p></li>
        <li><p><code>&#34;unattend&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-api_url"></div>
      <p style="display: inline;"><strong>api_url</strong></p>
      <a class="ansibleOptionLink" href="#parameter-api_url" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>The VCenter API URL.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-api_version"></div>
      <p style="display: inline;"><strong>api_version</strong></p>
      <a class="ansibleOptionLink" href="#parameter-api_version" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>The VCenter API Version.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;7.0&#34;</code></p></li>
        <li><p><code>&#34;6.7&#34;</code></p></li>
        <li><p><code>&#34;6.5&#34;</code></p></li>
        <li><p><code>&#34;6.0&#34;</code></p></li>
      </ul>

    </td>
  </tr>
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
      <p>URL of the Morpheus Appliance.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-auto_recover_power_state"></div>
      <p style="display: inline;"><strong>auto_recover_power_state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-auto_recover_power_state" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Automatically Power-on Virtual Machines.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-cluster"></div>
      <p style="display: inline;"><strong>cluster</strong></p>
      <a class="ansibleOptionLink" href="#parameter-cluster" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>VCenter Cluster name.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-code"></div>
      <p style="display: inline;"><strong>code</strong></p>
      <a class="ansibleOptionLink" href="#parameter-code" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>The code to reference the Cloud for use in polcies etc.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-console_keymap"></div>
      <div class="ansibleOptionAnchor" id="parameter-keyboard_layout"></div>
      <p style="display: inline;"><strong>console_keymap</strong></p>
      <a class="ansibleOptionLink" href="#parameter-console_keymap" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: keyboard_layout</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Guest console keyboard layout.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;us&#34;</code></p></li>
        <li><p><code>&#34;uk&#34;</code></p></li>
        <li><p><code>&#34;de&#34;</code></p></li>
        <li><p><code>&#34;de-ch&#34;</code></p></li>
        <li><p><code>&#34;es&#34;</code></p></li>
        <li><p><code>&#34;fi&#34;</code></p></li>
        <li><p><code>&#34;fr&#34;</code></p></li>
        <li><p><code>&#34;fr-be&#34;</code></p></li>
        <li><p><code>&#34;fr-ch&#34;</code></p></li>
        <li><p><code>&#34;is&#34;</code></p></li>
        <li><p><code>&#34;it&#34;</code></p></li>
        <li><p><code>&#34;jp&#34;</code></p></li>
        <li><p><code>&#34;nl-be&#34;</code></p></li>
        <li><p><code>&#34;False&#34;</code></p></li>
        <li><p><code>&#34;pt&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-costing_mode"></div>
      <div class="ansibleOptionAnchor" id="parameter-costing"></div>
      <p style="display: inline;"><strong>costing_mode</strong></p>
      <a class="ansibleOptionLink" href="#parameter-costing_mode" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: costing</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Enable costing on the Cloud.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;False&#34;</code></p></li>
        <li><p><code>&#34;costing&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-credential_id"></div>
      <p style="display: inline;"><strong>credential_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-credential_id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify id of existing credentials to use.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-dark_logo"></div>
      <p style="display: inline;"><strong>dark_logo</strong></p>
      <a class="ansibleOptionLink" href="#parameter-dark_logo" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Path to an image file to use as the Cloud logo when in dark mode.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-datacenter"></div>
      <p style="display: inline;"><strong>datacenter</strong></p>
      <a class="ansibleOptionLink" href="#parameter-datacenter" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>VCenter Datacenter name.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-datacenter_name"></div>
      <p style="display: inline;"><strong>datacenter_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-datacenter_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Custom Datacenter Identifier.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-description"></div>
      <p style="display: inline;"><strong>description</strong></p>
      <a class="ansibleOptionLink" href="#parameter-description" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Set the description of the Cloud.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-disk_storage_type"></div>
      <p style="display: inline;"><strong>disk_storage_type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk_storage_type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>The default Virtual Machine Disk type.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;thin&#34;</code></p></li>
        <li><p><code>&#34;thick&#34;</code></p></li>
        <li><p><code>&#34;thick_eager&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-enable_disk_type_selection"></div>
      <p style="display: inline;"><strong>enable_disk_type_selection</strong></p>
      <a class="ansibleOptionLink" href="#parameter-enable_disk_type_selection" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Enable user to select Virtual Machine Disk type.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-enable_network_type_selection"></div>
      <p style="display: inline;"><strong>enable_network_type_selection</strong></p>
      <a class="ansibleOptionLink" href="#parameter-enable_network_type_selection" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Enable user to select the Network Interface type.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-enable_storage_type_selection"></div>
      <p style="display: inline;"><strong>enable_storage_type_selection</strong></p>
      <a class="ansibleOptionLink" href="#parameter-enable_storage_type_selection" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Enable user to select the Storage type.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-enable_vnc"></div>
      <div class="ansibleOptionAnchor" id="parameter-enable_console"></div>
      <p style="display: inline;"><strong>enable_vnc</strong></p>
      <a class="ansibleOptionLink" href="#parameter-enable_vnc" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: enable_console</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Enable Hyper-Visor Console.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-enabled"></div>
      <p style="display: inline;"><strong>enabled</strong></p>
      <a class="ansibleOptionLink" href="#parameter-enabled" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Enable <code class="ansible-option-value literal notranslate"><a class="reference internal" href="#parameter-enabled"><span class="std std-ref"><span class="pre">enabled=true</span></span></a></code> or Disable <code class="ansible-option-value literal notranslate"><a class="reference internal" href="#parameter-enabled"><span class="std std-ref"><span class="pre">enabled=false</span></span></a></code> the Cloud.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-force_remove"></div>
      <p style="display: inline;"><strong>force_remove</strong></p>
      <a class="ansibleOptionLink" href="#parameter-force_remove" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Force removal if Cloud is still in a group.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-group_id"></div>
      <p style="display: inline;"><strong>group_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-group_id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Set the Cloud Group this Cloud is a member of.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-guidence_mode"></div>
      <div class="ansibleOptionAnchor" id="parameter-guidance"></div>
      <p style="display: inline;"><strong>guidence_mode</strong></p>
      <a class="ansibleOptionLink" href="#parameter-guidence_mode" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: guidance</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Enable/Disable Cloud Guidance</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;False&#34;</code></p></li>
        <li><p><code>&#34;manual&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-hide_host_selection"></div>
      <p style="display: inline;"><strong>hide_host_selection</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hide_host_selection" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Hide Cloud Host selection.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-id"></div>
      <div class="ansibleOptionAnchor" id="parameter-cloud_id"></div>
      <div class="ansibleOptionAnchor" id="parameter-zone_id"></div>
      <p style="display: inline;"><strong>id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: cloud_id, zone_id</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify an existing Cloud to Update or Remove.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-import_existing"></div>
      <p style="display: inline;"><strong>import_existing</strong></p>
      <a class="ansibleOptionLink" href="#parameter-import_existing" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Inventory Cloud and Import existing Virtual Machines.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-location"></div>
      <p style="display: inline;"><strong>location</strong></p>
      <a class="ansibleOptionLink" href="#parameter-location" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Add location information for the Cloud.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-logo"></div>
      <p style="display: inline;"><strong>logo</strong></p>
      <a class="ansibleOptionLink" href="#parameter-logo" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Path to an image file to use as the Cloud logo.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-name"></div>
      <p style="display: inline;"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Set the name of the Cloud.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-password"></div>
      <p style="display: inline;"><strong>password</strong></p>
      <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify a password to access the cloud.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-refresh_mode"></div>
      <p style="display: inline;"><strong>refresh_mode</strong></p>
      <a class="ansibleOptionLink" href="#parameter-refresh_mode" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>The type of refresh to perform.</p>
      <p><code class="ansible-value literal notranslate">costing</code> Pull costing data.</p>
      <p><code class="ansible-value literal notranslate">costing_rebuild</code> Purge existing costing data and rebuild by calling the Cloud API.</p>
      <p><code class="ansible-value literal notranslate">daily</code> Perform a daily Cloud Sync.</p>
      <p><code class="ansible-value literal notranslate">hourly</code> Perform hourly Cloud Sync.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;costing&#34;</code></p></li>
        <li><p><code>&#34;costing_rebuild&#34;</code></p></li>
        <li><p><code>&#34;daily&#34;</code></p></li>
        <li><p><code style="color: blue;"><b>&#34;hourly&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-refresh_period"></div>
      <p style="display: inline;"><strong>refresh_period</strong></p>
      <a class="ansibleOptionLink" href="#parameter-refresh_period" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>The invoice billing period to refresh.</p>
      <p>The value should be in the format of YYYYMM.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-remove_resources"></div>
      <p style="display: inline;"><strong>remove_resources</strong></p>
      <a class="ansibleOptionLink" href="#parameter-remove_resources" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Relevant when <code class="ansible-option-value literal notranslate"><a class="reference internal" href="#parameter-state"><span class="std std-ref"><span class="pre">state=absent</span></span></a></code>, remove associated resources when removing the cloud.</p>
      <p>Includes removal of Virtual Machines and other forms of Compute.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-resource_pool"></div>
      <p style="display: inline;"><strong>resource_pool</strong></p>
      <a class="ansibleOptionLink" href="#parameter-resource_pool" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>VCenter Resource Pool name.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-rpc_mode"></div>
      <p style="display: inline;"><strong>rpc_mode</strong></p>
      <a class="ansibleOptionLink" href="#parameter-rpc_mode" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Cloud workload interaction method.</p>
      <p><code class="ansible-value literal notranslate">guestexec</code> = VMWare Tools</p>
      <p><code class="ansible-value literal notranslate">rpc</code> = SSH/WinRM</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;guestexec&#34;</code></p></li>
        <li><p><code>&#34;rpc&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-scale_priority"></div>
      <p style="display: inline;"><strong>scale_priority</strong></p>
      <a class="ansibleOptionLink" href="#parameter-scale_priority" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Set Scale Priority.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-security_mode"></div>
      <p style="display: inline;"><strong>security_mode</strong></p>
      <a class="ansibleOptionLink" href="#parameter-security_mode" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Host firewall.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;False&#34;</code></p></li>
        <li><p><code>&#34;internal&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-state"></div>
      <p style="display: inline;"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Create, Update or Remove a Cloud.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;present&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;absent&#34;</code></p></li>
        <li><p><code>&#34;refresh&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-timezone"></div>
      <p style="display: inline;"><strong>timezone</strong></p>
      <a class="ansibleOptionLink" href="#parameter-timezone" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>The Time Zone of the Cloud.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-username"></div>
      <p style="display: inline;"><strong>username</strong></p>
      <a class="ansibleOptionLink" href="#parameter-username" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify a username to access the cloud.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-visibility"></div>
      <p style="display: inline;"><strong>visibility</strong></p>
      <a class="ansibleOptionLink" href="#parameter-visibility" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Toggle tenant visibility between Private or Public.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;private&#34;</code></p></li>
        <li><p><code>&#34;public&#34;</code></p></li>
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

  * - .. _ansible_collections.morpheus.core.vcenter_cloud_module__attribute-check_mode:

      **check_mode**

    - Support: full



    - 
      Can run in check\_mode and return changed status prediction without modifying target



  * - .. _ansible_collections.morpheus.core.vcenter_cloud_module__attribute-diff_mode:

      **diff_mode**

    - Support: full



    - 
      Will return details on what has changed (or possibly needs changing in check\_mode), when in diff mode



  * - .. _ansible_collections.morpheus.core.vcenter_cloud_module__attribute-platform:

      **platform**

    - Platforms:


    - 
      Target OS/families that can be operated against






Examples
--------

.. code-block:: yaml

    
    - name: Create new VCenter Cloud
      morpheus.core.vcenter_cloud:
        state: present
        name: VCenter Cloud
        description: A VCenter Cloud
        code: 'vccloud'
        location: 'south'
        visibility: private
        group_id: 50
        account_id: 1
        enabled: true
        agent_mode: cloudinit
        auto_recover_power_state: false
        import_existing: false
        costing_mode: off
        guidance_mode: off
        security_mode: off
        credential_id: 3
        api_url: 'https://vcenter.domain.tld/sdk'
        api_version: '7.0'
        datacenter: 'VCCloud'
        cluster: 'Cluster01'
        resource_pool: 'All'
        rpc_mode: guestexec
        disk_storage_type: thin
        enable_disk_type_selection: true
        enable_storage_type_selection: false
        enable_network_type_selection: true
        enable_vnc: true
        hide_host_selection: true
        console_keymap: uk
        timezone: "Europe/London"

    - name: Remove VCenter Cloud
      morpheus.core.vcenter_cloud:
        state: absent
        id: 56
        force_remove: true

    - name: Refresh and Rebuild Cloud Costing
      morpheus.core.vcenter_cloud:
        state: refresh
        name: VCenter Cloud
        refresh_mode: costing_rebuild





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
      <div class="ansibleOptionAnchor" id="return-cloud"></div>
      <p style="display: inline;"><strong>cloud</strong></p>
      <a class="ansibleOptionLink" href="#return-cloud" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Information related to the specified cloud.</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;cloud&#34;: {&#34;account&#34;: {&#34;id&#34;: 1, &#34;name&#34;: &#34;MasterTenant&#34;}, &#34;account_id&#34;: 1, &#34;agent_mode&#34;: &#34;cloudinit&#34;, &#34;api_proxy&#34;: null, &#34;auto_recover_power_state&#34;: false, &#34;code&#34;: &#34;vccloud&#34;, &#34;config&#34;: {&#34;api_url&#34;: &#34;https://vcenter.domain.tld/sdk&#34;, &#34;api_version&#34;: &#34;7.0&#34;, &#34;appliance_url&#34;: null, &#34;cluster&#34;: &#34;Cluster01&#34;, &#34;config_cmdb_discovery&#34;: false, &#34;datacenter&#34;: &#34;VCCloud&#34;, &#34;datacenter_name&#34;: null, &#34;disk_storage_type&#34;: &#34;thin&#34;, &#34;enable_disk_type_selection&#34;: true, &#34;enable_network_type_selection&#34;: true, &#34;enable_storage_type_selection&#34;: false, &#34;enable_vnc&#34;: true, &#34;hide_host_selection&#34;: true, &#34;import_existing&#34;: false, &#34;resource_pool&#34;: &#34;All&#34;, &#34;rpc_mode&#34;: &#34;guestexec&#34;}, &#34;console_keymap&#34;: &#34;uk&#34;, &#34;container_mode&#34;: &#34;docker&#34;, &#34;cost_last_sync&#34;: null, &#34;cost_last_sync_duration&#34;: null, &#34;cost_status&#34;: &#34;ok&#34;, &#34;cost_status_date&#34;: null, &#34;cost_status_message&#34;: null, &#34;costing_mode&#34;: &#34;off&#34;, &#34;credential&#34;: {&#34;id&#34;: 3, &#34;name&#34;: &#34;VCenter Creds&#34;, &#34;type&#34;: &#34;username-password&#34;}, &#34;dark_image_path&#34;: null, &#34;date_created&#34;: &#34;2024-01-01T00:00:01Z&#34;, &#34;domain_name&#34;: &#34;localdomain&#34;, &#34;enabled&#34;: false, &#34;external_id&#34;: null, &#34;groups&#34;: [{&#34;account_id&#34;: 1, &#34;id&#34;: 50, &#34;name&#34;: &#34;VCGroup&#34;}], &#34;guidance_mode&#34;: &#34;manual&#34;, &#34;id&#34;: 56, &#34;image_path&#34;: null, &#34;inventory_level&#34;: &#34;off&#34;, &#34;last_sync&#34;: null, &#34;last_sync_duration&#34;: null, &#34;last_updated&#34;: &#34;2024-01-01T00:00:01Z&#34;, &#34;location&#34;: &#34;south&#34;, &#34;name&#34;: &#34;VCenter Cloud&#34;, &#34;network_domain&#34;: null, &#34;network_server&#34;: null, &#34;next_run_date&#34;: null, &#34;owner&#34;: {&#34;id&#34;: 1, &#34;name&#34;: &#34;MasterTenant&#34;}, &#34;provisioning_proxy&#34;: null, &#34;region_code&#34;: null, &#34;scale_priority&#34;: 1, &#34;security_mode&#34;: &#34;off&#34;, &#34;security_server&#34;: null, &#34;server_count&#34;: 0, &#34;service_version&#34;: null, &#34;stats&#34;: {&#34;server_counts&#34;: {&#34;all&#34;: 0, &#34;baremetal&#34;: 0, &#34;container_host&#34;: 0, &#34;host&#34;: 0, &#34;hypervisor&#34;: 0, &#34;unmanaged&#34;: 0, &#34;vm&#34;: 0}}, &#34;status&#34;: &#34;initializing&#34;, &#34;status_date&#34;: null, &#34;status_message&#34;: null, &#34;storage_mode&#34;: &#34;standard&#34;, &#34;timezone&#34;: &#34;Europe/London&#34;, &#34;user_data_linux&#34;: null, &#34;user_data_windows&#34;: null, &#34;visibility&#34;: &#34;private&#34;, &#34;zone_type&#34;: {&#34;code&#34;: &#34;vmware&#34;, &#34;id&#34;: 28, &#34;name&#34;: &#34;VMware vCenter&#34;}, &#34;zone_type_id&#34;: 28}}</code></p>
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

