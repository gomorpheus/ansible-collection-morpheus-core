
.. Created with antsibull-docs 2.7.0

morpheus.core.virtual_image_info module -- Gather Virtual Image information
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.0).

It is not included in ``ansible-core``.
To check whether it is installed, run ``ansible-galaxy collection list``.

To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

To use it in a playbook, specify: ``morpheus.core.virtual_image_info``.

New in morpheus.core 0.6.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Gathers information about Virtual Images.








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
      <div class="ansibleOptionAnchor" id="parameter-detail"></div>
      <p style="display: inline;"><strong>detail</strong></p>
      <a class="ansibleOptionLink" href="#parameter-detail" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Level of detail returned about Virtual Images</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;full&#34;</code></p></li>
        <li><p><code style="color: blue;"><b>&#34;summary&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-filter_type"></div>
      <p style="display: inline;"><strong>filter_type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-filter_type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Filter Virtual Images by type</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;all&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;synced&#34;</code></p></li>
        <li><p><code>&#34;system&#34;</code></p></li>
        <li><p><code>&#34;user&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-image_type"></div>
      <p style="display: inline;"><strong>image_type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-image_type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Filter by image type code, e.g. vmware, ami</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-labels"></div>
      <p style="display: inline;"><strong>labels</strong></p>
      <a class="ansibleOptionLink" href="#parameter-labels" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </td>
    <td valign="top">
      <p>Filter by matching labels</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-match_all_labels"></div>
      <p style="display: inline;"><strong>match_all_labels</strong></p>
      <a class="ansibleOptionLink" href="#parameter-match_all_labels" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>If true, match all specified labels</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

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
      <p>Return info for Virtual Image by Name</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-regex_name"></div>
      <p style="display: inline;"><strong>regex_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-regex_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Treat name parameter as a Regular Expression</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-virtual_image_id"></div>
      <p style="display: inline;"><strong>virtual_image_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-virtual_image_id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Return info for specic Virtual Image by Id</p>
    </td>
  </tr>
  </tbody>
  </table>






Examples
--------

.. code-block:: yaml

    
    - name: Get Virtual Image by Id
      morpheus.core.virtual_image_info:
        virtual_image_id: 500

    - name: Get Virtual Image by Name
      morpheus.core.virtual_image_info:
        name: redhat_image

    - name: Get Virtual Images by Regex Match
      morpheus.core.virtual_image_info:
        name: ^.*$
        regex_name: true

    - name: Get Synced VMware Virtual Images
      morpheus.core.virtual_image_info:
        filter_type: synced
        image_type: vmware

    - name: Get User Virtual Images
      morpheus.core.virtual_image_info:
        filter_type: user





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
      <div class="ansibleOptionAnchor" id="return-virtual_images"></div>
      <p style="display: inline;"><strong>virtual_images</strong></p>
      <a class="ansibleOptionLink" href="#return-virtual_images" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>List of Virtual Images</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;virtual_images&#34;: [{&#34;date_created&#34;: &#34;2023-01-01T00:00:00Z&#34;, &#34;description&#34;: null, &#34;id&#34;: 500, &#34;image_type&#34;: &#34;vmdk&#34;, &#34;install_agent&#34;: false, &#34;is_cloud_init&#34;: false, &#34;is_force_customization&#34;: false, &#34;labels&#34;: [], &#34;locations&#34;: [], &#34;min_disk_gb&#34;: null, &#34;min_ram_gb&#34;: 4, &#34;name&#34;: &#34;My User Image&#34;, &#34;os_type&#34;: {&#34;bit_count&#34;: 64, &#34;category&#34;: &#34;suse&#34;, &#34;code&#34;: &#34;suse.11.64&#34;, &#34;description&#34;: null, &#34;id&#34;: 92, &#34;name&#34;: &#34;suse enterprise 11 64-bit&#34;, &#34;os_family&#34;: &#34;suse&#34;, &#34;os_version&#34;: &#34;11&#34;, &#34;platform&#34;: &#34;linux&#34;, &#34;vendor&#34;: &#34;suse&#34;}, &#34;raw_size_gb&#34;: null, &#34;ssh_username&#34;: null, &#34;status&#34;: &#34;queued&#34;, &#34;vm_tools_installed&#34;: true, &#34;volumes&#34;: []}]}</code></p>
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

