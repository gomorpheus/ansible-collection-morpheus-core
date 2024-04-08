
.. Created with antsibull-docs 2.7.0

morpheus.core.group_info module -- Retrieves Group Info
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.0).

It is not included in ``ansible-core``.
To check whether it is installed, run ``ansible-galaxy collection list``.

To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

To use it in a playbook, specify: ``morpheus.core.group_info``.

New in morpheus.core 0.7.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Retrieves information about Groups.








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
      <p>Level of detail returned.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;summary&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;full&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-id"></div>
      <p style="display: inline;"><strong>id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Return specific object by id.</p>
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
      <p>Filter by name.</p>
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
      <p>Treat the name parameter as a regular expression.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  </tbody>
  </table>






Examples
--------

.. code-block:: yaml

    
    - name: Get Info for a Specific Group by id
      morpheus.core.group_info:
        id: 5

    - name: Get Groups Matching Regex Pattern
      morpheus.core.group_info:
        name: ^linux.*$
        regex_name: true

    - name: Get Full Info for all Groups
      morpheus.core.group_info:
        detail: full





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
      <div class="ansibleOptionAnchor" id="return-groups"></div>
      <p style="display: inline;"><strong>groups</strong></p>
      <a class="ansibleOptionLink" href="#return-groups" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>List of groups information.</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;groups&#34;: [{&#34;account_id&#34;: 1, &#34;active&#34;: true, &#34;code&#34;: &#34;linuxClouds&#34;, &#34;config&#34;: {&#34;config_cmdb_discovery&#34;: false, &#34;service_registry_id&#34;: &#34;&#34;}, &#34;date_created&#34;: &#34;2024-01-01T00:00:01Z&#34;, &#34;id&#34;: 5, &#34;last_updated&#34;: &#34;2024-01-01T00:00:01Z&#34;, &#34;location&#34;: null, &#34;name&#34;: &#34;Linux Cloud Group&#34;, &#34;server_count&#34;: 9, &#34;stats&#34;: {&#34;instance_counts&#34;: {&#34;all&#34;: 2}, &#34;server_counts&#34;: {&#34;all&#34;: 9, &#34;baremetal&#34;: 0, &#34;container_host&#34;: 0, &#34;host&#34;: 9, &#34;hypervisor&#34;: 9, &#34;unmanaged&#34;: 0, &#34;vm&#34;: 3}}}]}</code></p>
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

