
.. Created with antsibull-docs 2.7.0

morpheus.core.virtual_image module -- Manage Morpheus Virtual Images
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.0).

It is not included in ``ansible-core``.
To check whether it is installed, run ``ansible-galaxy collection list``.

To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

To use it in a playbook, specify: ``morpheus.core.virtual_image``.

New in morpheus.core 0.6.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Manage Morpheus Virtual Images.








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
      <div class="ansibleOptionAnchor" id="parameter-accounts"></div>
      <p style="display: inline;"><strong>accounts</strong></p>
      <a class="ansibleOptionLink" href="#parameter-accounts" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=integer</span>
      </p>
    </td>
    <td valign="top">
      <p>List of Tenants by Id Virtual Image is available to.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-azure_config"></div>
      <p style="display: inline;"><strong>azure_config</strong></p>
      <a class="ansibleOptionLink" href="#parameter-azure_config" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>For Azure Virtual Images, specify further options.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-azure_config/offer"></div>
      <p style="display: inline;"><strong>offer</strong></p>
      <a class="ansibleOptionLink" href="#parameter-azure_config/offer" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Name of Offer in the Azure Marketplace.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-azure_config/publisher"></div>
      <p style="display: inline;"><strong>publisher</strong></p>
      <a class="ansibleOptionLink" href="#parameter-azure_config/publisher" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Name of Publisher in the Azure Marketplace.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-azure_config/sku"></div>
      <p style="display: inline;"><strong>sku</strong></p>
      <a class="ansibleOptionLink" href="#parameter-azure_config/sku" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Name of SKU in the Azure Marketplace.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-azure_config/version"></div>
      <p style="display: inline;"><strong>version</strong></p>
      <a class="ansibleOptionLink" href="#parameter-azure_config/version" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Name of Version in the Azure Marketplace.</p>
    </td>
  </tr>

  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config"></div>
      <p style="display: inline;"><strong>config</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>Dictionary of Virtual Image configuration.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-file_url"></div>
      <p style="display: inline;"><strong>file_url</strong></p>
      <a class="ansibleOptionLink" href="#parameter-file_url" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>URL of file to upload.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-filename"></div>
      <p style="display: inline;"><strong>filename</strong></p>
      <a class="ansibleOptionLink" href="#parameter-filename" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Name of uploaded file.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-image_type"></div>
      <p style="display: inline;"><strong>image_type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-image_type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Set the Image Type code, e.g. vmware</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-install_agent"></div>
      <p style="display: inline;"><strong>install_agent</strong></p>
      <a class="ansibleOptionLink" href="#parameter-install_agent" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify if Morpheus Agent should be installed.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-is_auto_join_domain"></div>
      <p style="display: inline;"><strong>is_auto_join_domain</strong></p>
      <a class="ansibleOptionLink" href="#parameter-is_auto_join_domain" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Whether to Auto Join Domain.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-is_cloud_init"></div>
      <p style="display: inline;"><strong>is_cloud_init</strong></p>
      <a class="ansibleOptionLink" href="#parameter-is_cloud_init" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify if Cloud Init is enabled.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-is_sysprep"></div>
      <p style="display: inline;"><strong>is_sysprep</strong></p>
      <a class="ansibleOptionLink" href="#parameter-is_sysprep" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify if Sysprep is Enabled.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

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
      <p>Provide a list of labels to apply to Virtual Image.</p>
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
      <p>Set the Name of the Virtual Image</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-os_type"></div>
      <p style="display: inline;"><strong>os_type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-os_type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify the OS Type code or name.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-password"></div>
      <p style="display: inline;"><strong>password</strong></p>
      <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify the Password for the Virtual Image.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-ssh_key"></div>
      <p style="display: inline;"><strong>ssh_key</strong></p>
      <a class="ansibleOptionLink" href="#parameter-ssh_key" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify an SSH Key for the Virtual Image.</p>
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
      <p>Create, update or remove a Virtual Image.</p>
      <p>If <code class="ansible-option-value literal notranslate"><a class="reference internal" href="#parameter-state"><span class="std std-ref"><span class="pre">state=absent</span></span></a></code> and <code class="ansible-option literal notranslate"><strong><a class="reference internal" href="#parameter-filename"><span class="std std-ref"><span class="pre">filename</span></span></a></strong></code> is specified then remove the specified file.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;absent&#34;</code></p></li>
        <li><p><code style="color: blue;"><b>&#34;present&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-storage_provider_id"></div>
      <p style="display: inline;"><strong>storage_provider_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-storage_provider_id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify the Storage Provider by Id.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-tags"></div>
      <p style="display: inline;"><strong>tags</strong></p>
      <a class="ansibleOptionLink" href="#parameter-tags" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>List of Tags to apply.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-tags/name"></div>
      <p style="display: inline;"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-tags/name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>The Tag name.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-tags/value"></div>
      <p style="display: inline;"><strong>value</strong></p>
      <a class="ansibleOptionLink" href="#parameter-tags/value" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>The Tag value.</p>
    </td>
  </tr>

  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-trial_version"></div>
      <p style="display: inline;"><strong>trial_version</strong></p>
      <a class="ansibleOptionLink" href="#parameter-trial_version" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Is the Virtual Image a Trial Version.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-user_data"></div>
      <p style="display: inline;"><strong>user_data</strong></p>
      <a class="ansibleOptionLink" href="#parameter-user_data" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Cloud Init user data.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-username"></div>
      <p style="display: inline;"><strong>username</strong></p>
      <a class="ansibleOptionLink" href="#parameter-username" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify the Username for the Virtual Image.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-virtio_supported"></div>
      <p style="display: inline;"><strong>virtio_supported</strong></p>
      <a class="ansibleOptionLink" href="#parameter-virtio_supported" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Are Virtio Drivers installed.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-virtual_image_id"></div>
      <p style="display: inline;"><strong>virtual_image_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-virtual_image_id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify Virtual Image by Id.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-visibility"></div>
      <p style="display: inline;"><strong>visibility</strong></p>
      <a class="ansibleOptionLink" href="#parameter-visibility" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>If the Virtual Image should be private or public.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;private&#34;</code></p></li>
        <li><p><code>&#34;public&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vm_tools_installed"></div>
      <p style="display: inline;"><strong>vm_tools_installed</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vm_tools_installed" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Are VMware Tools installed.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
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

  * - .. _ansible_collections.morpheus.core.virtual_image_module__attribute-check_mode:

      **check_mode**

    - Support: full



    - 
      Can run in check\_mode and return changed status prediction without modifying target



  * - .. _ansible_collections.morpheus.core.virtual_image_module__attribute-diff_mode:

      **diff_mode**

    - Support: full



    - 
      Will return details on what has changed (or possibly needs changing in check\_mode), when in diff mode



  * - .. _ansible_collections.morpheus.core.virtual_image_module__attribute-platform:

      **platform**

    - Platforms:


    - 
      Target OS/families that can be operated against






Examples
--------

.. code-block:: yaml

    
    - name: Create Virtual Image and upload File
      morpheus.core.virtual_image:
        state: present
        name: My VMware Image
        image_type: vmware
        is_cloud_init: true
        install_agent: true
        username: root
        password: Password123
        os_type: redhat 8 64bit
        visibility: public
        accounts:
            - 1
        vm_tools_installed: true
        filename: rhel8x64.ova
        file_url: https://my.domain.tld/rhel8x64.ova

    - name: Remove Virtual Image by Name
      morpheus.core.virtual_image:
        state: absent
        name: Win2016

    - name: Remove Virtual Image by Id
      morpheus.core.virtual_image:
        state: absent
        virtual_image_id: 700

    - name: Remove Virtual Image File
      morpheus.core.virtual_image:
        virtual_image_id: 750
        filename: windows_template.ova
        state: absent





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
      <div class="ansibleOptionAnchor" id="return-virtual_image"></div>
      <p style="display: inline;"><strong>virtual_image</strong></p>
      <a class="ansibleOptionLink" href="#return-virtual_image" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Information about the Virtual Image.</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;virtual_image&#34;: {&#34;accounts&#34;: [{&#34;id&#34;: 1, &#34;name&#34;: &#34;TenantA&#34;}], &#34;config&#34;: {&#34;disk_ids&#34;: []}, &#34;console_keymap&#34;: null, &#34;date_created&#34;: &#34;2023-10-06T23:15:39Z&#34;, &#34;description&#34;: null, &#34;external_id&#34;: null, &#34;fips_enabled&#34;: false, &#34;guest_console_password&#34;: null, &#34;guest_console_password_hash&#34;: null, &#34;guest_console_port&#34;: null, &#34;guest_console_type&#34;: null, &#34;guest_console_username&#34;: null, &#34;id&#34;: 700, &#34;image_type&#34;: &#34;vmware&#34;, &#34;install_agent&#34;: true, &#34;is_auto_join_domain&#34;: false, &#34;is_cloud_init&#34;: false, &#34;is_force_customization&#34;: false, &#34;is_sysprep&#34;: true, &#34;labels&#34;: [], &#34;last_updated&#34;: &#34;2023-10-08T21:15:26Z&#34;, &#34;linked_clone&#34;: false, &#34;locations&#34;: [], &#34;min_disk&#34;: null, &#34;min_disk_gb&#34;: null, &#34;min_ram&#34;: null, &#34;min_ram_gb&#34;: null, &#34;name&#34;: &#34;Windows 2022 Template&#34;, &#34;network_interfaces&#34;: [], &#34;os_type&#34;: {&#34;bit_count&#34;: 64, &#34;category&#34;: &#34;windows&#34;, &#34;code&#34;: &#34;windows.server.2022&#34;, &#34;description&#34;: null, &#34;id&#34;: 27, &#34;name&#34;: &#34;windows server 2022&#34;, &#34;os_family&#34;: &#34;windows&#34;, &#34;os_version&#34;: &#34;2022&#34;, &#34;platform&#34;: &#34;windows&#34;, &#34;vendor&#34;: &#34;microsoft&#34;}, &#34;owner_id&#34;: 1, &#34;raw_size&#34;: null, &#34;raw_size_gb&#34;: null, &#34;ssh_key&#34;: null, &#34;ssh_password&#34;: &#34;************&#34;, &#34;ssh_password_hash&#34;: &#34;936a185caaa266bb9cbe981e9e05cb78cd732b0b3280eb944412bb6f8f8f07af&#34;, &#34;ssh_username&#34;: &#34;Administrator&#34;, &#34;status&#34;: &#34;Active&#34;, &#34;storage_controllers&#34;: [], &#34;storage_provider&#34;: null, &#34;system_image&#34;: false, &#34;tags&#34;: [{&#34;id&#34;: 150, &#34;name&#34;: &#34;Bleh&#34;, &#34;value&#34;: &#34;Blah&#34;}, {&#34;id&#34;: 149, &#34;name&#34;: &#34;Foo&#34;, &#34;value&#34;: &#34;Bar&#34;}], &#34;tenant&#34;: {&#34;id&#34;: 1, &#34;name&#34;: &#34;TenantA&#34;}, &#34;trial_version&#34;: false, &#34;uefi&#34;: false, &#34;user_data&#34;: null, &#34;user_defined&#34;: false, &#34;user_uploaded&#34;: true, &#34;virtio_supported&#34;: false, &#34;visibility&#34;: &#34;public&#34;, &#34;vm_tools_installed&#34;: true, &#34;volumes&#34;: []}}</code></p>
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

