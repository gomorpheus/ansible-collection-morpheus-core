
.. Created with antsibull-docs 2.7.0

morpheus.core.instance module -- Basic Management of Morpheus Instances
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.0).

It is not included in ``ansible-core``.
To check whether it is installed, run ``ansible-galaxy collection list``.

To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

To use it in a playbook, specify: ``morpheus.core.instance``.

New in morpheus.core 0.5.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module provides basic management of Morpheus Instances, such as setting running state, backup, deletion and lock status.








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
    <td colspan="2" valign="top">
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
    <td colspan="2" valign="top">
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
    <td colspan="2" valign="top">
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
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-remove_options"></div>
      <p style="display: inline;"><strong>remove_options</strong></p>
      <a class="ansibleOptionLink" href="#parameter-remove_options" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>When <code class="ansible-option-value literal notranslate"><a class="reference internal" href="#parameter-state"><span class="std std-ref"><span class="pre">state=absent</span></span></a></code> specify additional removal options.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-remove_options/force"></div>
      <p style="display: inline;"><strong>force</strong></p>
      <a class="ansibleOptionLink" href="#parameter-remove_options/force" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Force removal of instance.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-remove_options/keep_backups"></div>
      <p style="display: inline;"><strong>keep_backups</strong></p>
      <a class="ansibleOptionLink" href="#parameter-remove_options/keep_backups" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Keep instances backups.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-remove_options/preserve_volumes"></div>
      <p style="display: inline;"><strong>preserve_volumes</strong></p>
      <a class="ansibleOptionLink" href="#parameter-remove_options/preserve_volumes" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Preserve the instances volumes.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-remove_options/release_floating_ips"></div>
      <p style="display: inline;"><strong>release_floating_ips</strong></p>
      <a class="ansibleOptionLink" href="#parameter-remove_options/release_floating_ips" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Release instances floating IP Addresses.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>

  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-state"></div>
      <p style="display: inline;"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td valign="top">
      <p>Set the State of the Instance.</p>
      <p><code class="ansible-value literal notranslate">eject</code> - Ejects ISO media from the instance.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;running&#34;</code></p></li>
        <li><p><code>&#34;started&#34;</code></p></li>
        <li><p><code>&#34;stopped&#34;</code></p></li>
        <li><p><code>&#34;restarted&#34;</code></p></li>
        <li><p><code>&#34;suspended&#34;</code></p></li>
        <li><p><code>&#34;locked&#34;</code></p></li>
        <li><p><code>&#34;unlocked&#34;</code></p></li>
        <li><p><code>&#34;backup&#34;</code></p></li>
        <li><p><code>&#34;absent&#34;</code></p></li>
        <li><p><code>&#34;eject&#34;</code></p></li>
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

  * - .. _ansible_collections.morpheus.core.instance_module__attribute-check_mode:

      **check_mode**

    - Support: full



    - 
      Can run in check\_mode and return changed status prediction without modifying target



  * - .. _ansible_collections.morpheus.core.instance_module__attribute-diff_mode:

      **diff_mode**

    - Support: full



    - 
      Will return details on what has changed (or possibly needs changing in check\_mode), when in diff mode



  * - .. _ansible_collections.morpheus.core.instance_module__attribute-platform:

      **platform**

    - Platforms:


    - 
      Target OS/families that can be operated against






Examples
--------

.. code-block:: yaml

    
    - name: Restart a specific instance
      morpheus.core.instance:
        id: 200
        state: restarted

    - name: Stop all instances matching regex name pattern
      morpheus.core.instance:
        name: ^PROD.*$
        regex_name: true
        match_name: all
        state: stopped

    - name: Suspend the first instance that matches name
      morpheus.core.instance:
        name: PRODWEBSVR001
        match_name: first
        state: suspended

    - name: Remove instance but keep backups
      morpheus.core.instance:
        name: PRODWEBSVR002
        match_name: first
        state: absent
        remove_options:
          keep_backups: true

    - name: Backup all instances
      morpheus.core.instance:
        name: ^.*$
        regex_name: true
        match_name: all
        state: backup





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
      <div class="ansibleOptionAnchor" id="return-instance_state"></div>
      <p style="display: inline;"><strong>instance_state</strong></p>
      <a class="ansibleOptionLink" href="#return-instance_state" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>State of the instance(s) following the requested action.</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;instance_state&#34;: [{&#34;id&#34;: 200, &#34;locked&#34;: true, &#34;name&#34;: &#34;PRODWEBSVR001&#34;, &#34;status&#34;: &#34;running&#34;}]}</code></p>
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

