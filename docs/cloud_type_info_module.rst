
.. Created with antsibull-docs 2.7.0

morpheus.core.cloud_type_info module -- Return available Cloud types
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.0).

It is not included in ``ansible-core``.
To check whether it is installed, run ``ansible-galaxy collection list``.

To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

To use it in a playbook, specify: ``morpheus.core.cloud_type_info``.

New in morpheus.core 0.7.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Returns the available Cloud Types.








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
      <div class="ansibleOptionAnchor" id="parameter-code"></div>
      <p style="display: inline;"><strong>code</strong></p>
      <a class="ansibleOptionLink" href="#parameter-code" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Filter Cloud Types by code.</p>
    </td>
  </tr>
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

    
    - name: Return all Cloud Types
      morpheus.core.cloud_type_info:

    - name: Return Cloud Type by Type Code
      morpheus.core.cloud_type_info:
        code: vmware

    - name: Return Full Info about Cloud Types
      morpheus.core.cloud_type_info:
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
      <div class="ansibleOptionAnchor" id="return-cloud_types"></div>
      <p style="display: inline;"><strong>cloud_types</strong></p>
      <a class="ansibleOptionLink" href="#return-cloud_types" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>List of Cloud Type Info.</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;cloud_types&#34;: [{&#34;cloud&#34;: &#34;private&#34;, &#34;code&#34;: &#34;fusion&#34;, &#34;enabled&#34;: true, &#34;id&#34;: 38, &#34;name&#34;: &#34;VMware Fusion&#34;}, {&#34;cloud&#34;: &#34;private&#34;, &#34;code&#34;: &#34;vmware&#34;, &#34;enabled&#34;: true, &#34;id&#34;: 28, &#34;name&#34;: &#34;VMware vCenter&#34;}]}</code></p>
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

