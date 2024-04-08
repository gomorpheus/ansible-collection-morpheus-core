
.. Created with antsibull-docs 2.7.0

morpheus.core.instance_snapshot module -- Manage Instance Snapshots
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.0).

It is not included in ``ansible-core``.
To check whether it is installed, run ``ansible-galaxy collection list``.

To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

To use it in a playbook, specify: ``morpheus.core.instance_snapshot``.

New in morpheus.core 0.5.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Manage Snapshots of Morpheus Instances.








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
      <div class="ansibleOptionAnchor" id="parameter-match_name"></div>
      <p style="display: inline;"><strong>match_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-match_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Define instance selection method when specifying <code class="ansible-option literal notranslate"><strong><a class="reference internal" href="#parameter-name"><span class="std std-ref"><span class="pre">name</span></span></a></strong></code> should more than one instance match.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;none&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;first&#34;</code></p></li>
        <li><p><code>&#34;last&#34;</code></p></li>
        <li><p><code>&#34;all&#34;</code></p></li>
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
      <div class="ansibleOptionAnchor" id="parameter-snapshot_age"></div>
      <p style="display: inline;"><strong>snapshot_age</strong></p>
      <a class="ansibleOptionLink" href="#parameter-snapshot_age" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify the age of the snapshot to match.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;latest&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;oldest&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-snapshot_description"></div>
      <p style="display: inline;"><strong>snapshot_description</strong></p>
      <a class="ansibleOptionLink" href="#parameter-snapshot_description" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify description for snapshot.</p>
      <p>Used with <code class="ansible-option-value literal notranslate"><a class="reference internal" href="#parameter-state"><span class="std std-ref"><span class="pre">state=present</span></span></a></code></p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-snapshot_id"></div>
      <p style="display: inline;"><strong>snapshot_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-snapshot_id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify snapshot by id when using <code class="ansible-option-value literal notranslate"><a class="reference internal" href="#parameter-state"><span class="std std-ref"><span class="pre">state=absent</span></span></a></code> or <code class="ansible-option-value literal notranslate"><a class="reference internal" href="#parameter-state"><span class="std std-ref"><span class="pre">state=revert</span></span></a></code>.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-snapshot_name"></div>
      <p style="display: inline;"><strong>snapshot_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-snapshot_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify snapshot name.</p>
      <p>Can be used with <code class="ansible-option-value literal notranslate"><a class="reference internal" href="#parameter-state"><span class="std std-ref"><span class="pre">state=present</span></span></a></code>, <code class="ansible-option-value literal notranslate"><a class="reference internal" href="#parameter-state"><span class="std std-ref"><span class="pre">state=absent</span></span></a></code>, <code class="ansible-option-value literal notranslate"><a class="reference internal" href="#parameter-state"><span class="std std-ref"><span class="pre">state=revert</span></span></a></code>.</p>
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
      <p>Manage snapshot state of the specified instance(s)</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;absent&#34;</code></p></li>
        <li><p><code style="color: blue;"><b>&#34;present&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;revert&#34;</code></p></li>
        <li><p><code>&#34;remove_all&#34;</code></p></li>
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

  * - .. _ansible_collections.morpheus.core.instance_snapshot_module__attribute-check_mode:

      **check_mode**

    - Support: full



    - 
      Can run in check\_mode and return changed status prediction without modifying target



  * - .. _ansible_collections.morpheus.core.instance_snapshot_module__attribute-diff_mode:

      **diff_mode**

    - Support: full



    - 
      Will return details on what has changed (or possibly needs changing in check\_mode), when in diff mode



  * - .. _ansible_collections.morpheus.core.instance_snapshot_module__attribute-platform:

      **platform**

    - Platforms:


    - 
      Target OS/families that can be operated against






Examples
--------

.. code-block:: yaml

    
    - name: Snapshot All Instances
      morpheus.core.instance_snapshot:
        name: ^.*$
        match_name: all
        regex_name: true
        snapshot_name: Ansible Snapshot
        snapshot_description: Snapshot Created via Ansible
        state: present

    - name: Remove All Snapshots for Specific Instance
      morpheus.core.instance_snapshot:
        id: 200
        state: remove_all

    - name: Revert Instance to Oldest Snapshot matching Name
      morpheus.core.instance_snapshot:
        name: WebServer001
        snapshot_name: Ansible Snapshot
        snapshot_age: oldest
        state: revert

    - name: Remove Specific Snapshot by Id
      morpheus.core.instance_snapshot:
        snapshot_id: 50
        state: absent

    - name: Remove the Latest Snapshot matching Name for all Instances
      morpheus.core.instance_snapshot:
        name: ^.*$
        match_name: all
        regex_name: true
        snapshot_name: Ansible Snapshot
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
      <div class="ansibleOptionAnchor" id="return-snapshot_results"></div>
      <p style="display: inline;"><strong>snapshot_results</strong></p>
      <a class="ansibleOptionLink" href="#return-snapshot_results" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>List of results of each action performed against each instance and/or snapshot.</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;snapshot_results&#34;: [{&#34;action&#34;: &#34;create&#34;, &#34;instance_id&#34;: 1, &#34;instance_name&#34;: &#34;WebServer001&#34;, &#34;msg&#34;: &#34;&#34;, &#34;snapshot_date&#34;: null, &#34;snapshot_description&#34;: &#34;Snapshot Created via Ansible&#34;, &#34;snapshot_id&#34;: null, &#34;snapshot_name&#34;: &#34;Ansible Snapshot&#34;, &#34;success&#34;: true}]}</code></p>
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

