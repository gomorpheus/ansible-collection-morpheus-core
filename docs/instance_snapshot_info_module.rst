
.. Created with antsibull-docs 2.7.0

morpheus.core.instance_snapshot_info module -- Gather Snapshot information for instances
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.0).

It is not included in ``ansible-core``.
To check whether it is installed, run ``ansible-galaxy collection list``.

To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

To use it in a playbook, specify: ``morpheus.core.instance_snapshot_info``.

New in morpheus.core 0.5.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Gather Snapshot information for instances.








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
      <div class="ansibleOptionAnchor" id="parameter-environment"></div>
      <p style="display: inline;"><strong>environment</strong></p>
      <a class="ansibleOptionLink" href="#parameter-environment" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Filter instances by environment.</p>
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
      <p>Specify the id of an instance.</p>
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
      <p>Filter instances by matching labels.</p>
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
      <p>If labels have been specified, filter instances by those that match all specified labels.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-match_name"></div>
      <p style="display: inline;"><strong>match_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-match_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Define instance selection method when specifying <em>name</em> should more than one instance match.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;none&#34;</code></p></li>
        <li><p><code>&#34;first&#34;</code></p></li>
        <li><p><code>&#34;last&#34;</code></p></li>
        <li><p><code style="color: blue;"><b>&#34;all&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
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
      <p>Filter instances by name.</p>
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
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-tags"></div>
      <p style="display: inline;"><strong>tags</strong></p>
      <a class="ansibleOptionLink" href="#parameter-tags" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </td>
    <td valign="top">
      <p>Filter instances by matching tags.</p>
    </td>
  </tr>
  </tbody>
  </table>






Examples
--------

.. code-block:: yaml

    
    - name: Get Snapshots for specific instance
      morpheus.core.instance_snapshot_info:
        id: 200

    - name: Get Snapshots for instances matching regex pattern
      morpheus.core.instance_snapshot_info:
        name: ^PRODWEB.*$
        regex_name: true

    - name: Get Snapshots for instances with assigned labels
      morpheus.core.instance_snapshot_info:
        labels:
          - PROD
          - WEB





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
      <div class="ansibleOptionAnchor" id="return-instance_snapshots"></div>
      <p style="display: inline;"><strong>instance_snapshots</strong></p>
      <a class="ansibleOptionLink" href="#return-instance_snapshots" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>List of Instances and their snapshots</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;instance_snapshots&#34;: [{&#34;instance_id&#34;: 200, &#34;instance_name&#34;: &#34;PRODWEBSVR001&#34;, &#34;snapshot_count&#34;: 1, &#34;snapshots&#34;: [{&#34;currently_active&#34;: true, &#34;datastore&#34;: null, &#34;date_created&#34;: &#34;2023-07-29T15:33:05Z&#34;, &#34;description&#34;: &#34;Pre-maintenance Snapshot&#34;, &#34;external_id&#34;: &#34;snapshot-100000&#34;, &#34;id&#34;: 1, &#34;name&#34;: &#34;PRODWEBSVR001-2023-07-29T15:32:51.774Z&#34;, &#34;parent_snapshot&#34;: null, &#34;snapshot_created&#34;: &#34;2023-07-29T15:33:36Z&#34;, &#34;snapshot_type&#34;: &#34;vm&#34;, &#34;state&#34;: null, &#34;status&#34;: &#34;complete&#34;, &#34;zone&#34;: {&#34;id&#34;: 5, &#34;name&#34;: &#34;Web Cloud&#34;}}]}]}</code></p>
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

