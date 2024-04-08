
.. Created with antsibull-docs 2.7.0

morpheus.core.cypher module -- Manage items stored in Cypher
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.0).

It is not included in ``ansible-core``.
To check whether it is installed, run ``ansible-galaxy collection list``.

To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

To use it in a playbook, specify: ``morpheus.core.cypher``.

New in morpheus.core 0.7.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Create and Delete items stored in Cypher.








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
      <div class="ansibleOptionAnchor" id="parameter-cypher_path"></div>
      <p style="display: inline;"><strong>cypher_path</strong></p>
      <a class="ansibleOptionLink" href="#parameter-cypher_path" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify a full Cypher mount and key path.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-length"></div>
      <p style="display: inline;"><strong>length</strong></p>
      <a class="ansibleOptionLink" href="#parameter-length" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Required if <code class="ansible-option literal notranslate"><strong><a class="reference internal" href="#parameter-mount"><span class="std std-ref"><span class="pre">mount</span></span></a></strong></code> is either <code class="ansible-value literal notranslate">key</code> or <code class="ansible-value literal notranslate">password</code></p>
      <p>For <code class="ansible-option-value literal notranslate"><a class="reference internal" href="#parameter-mount"><span class="std std-ref"><span class="pre">mount=key</span></span></a></code> specify the bit length for the generated key.</p>
      <p>For <code class="ansible-option-value literal notranslate"><a class="reference internal" href="#parameter-mount"><span class="std std-ref"><span class="pre">mount=password</span></span></a></code> specify the character length for the generated password.</p>
      <p>Mutually exclusive with <code class="ansible-option literal notranslate"><strong><a class="reference internal" href="#parameter-cypher_path"><span class="std std-ref"><span class="pre">cypher_path</span></span></a></strong></code>.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-mount"></div>
      <p style="display: inline;"><strong>mount</strong></p>
      <a class="ansibleOptionLink" href="#parameter-mount" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify the Cypher mount point.</p>
      <p>Mutually exclusive with <code class="ansible-option literal notranslate"><strong><a class="reference internal" href="#parameter-cypher_path"><span class="std std-ref"><span class="pre">cypher_path</span></span></a></strong></code>.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;key&#34;</code></p></li>
        <li><p><code>&#34;password&#34;</code></p></li>
        <li><p><code>&#34;secret&#34;</code></p></li>
        <li><p><code>&#34;tfvars&#34;</code></p></li>
        <li><p><code>&#34;uuid&#34;</code></p></li>
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
      <p>Specify the Key Name.</p>
      <p>Required when <code class="ansible-option literal notranslate"><strong><a class="reference internal" href="#parameter-mount"><span class="std std-ref"><span class="pre">mount</span></span></a></strong></code> is specified.</p>
      <p>Mutually exclusive with <code class="ansible-option literal notranslate"><strong><a class="reference internal" href="#parameter-cypher_path"><span class="std std-ref"><span class="pre">cypher_path</span></span></a></strong></code>.</p>
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
      <p>State of the stored item.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;absent&#34;</code></p></li>
        <li><p><code style="color: blue;"><b>&#34;present&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-ttl"></div>
      <div class="ansibleOptionAnchor" id="parameter-lease_duration"></div>
      <div class="ansibleOptionAnchor" id="parameter-duration"></div>
      <p style="display: inline;"><strong>ttl</strong></p>
      <a class="ansibleOptionLink" href="#parameter-ttl" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: lease_duration, duration</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify the lease duration either in seconds or human readable format, e.g 15m, 8h, 7d.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;0&#34;</code></p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-value"></div>
      <p style="display: inline;"><strong>value</strong></p>
      <a class="ansibleOptionLink" href="#parameter-value" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify the data to be stored when <code class="ansible-option literal notranslate"><strong><a class="reference internal" href="#parameter-mount"><span class="std std-ref"><span class="pre">mount</span></span></a></strong></code> is either <code class="ansible-value literal notranslate">secret</code> or <code class="ansible-value literal notranslate">tfvars</code>.</p>
      <p>Required when <code class="ansible-option literal notranslate"><strong><a class="reference internal" href="#parameter-mount"><span class="std std-ref"><span class="pre">mount</span></span></a></strong></code> is either <code class="ansible-value literal notranslate">secret</code> or <code class="ansible-value literal notranslate">tfvars</code>.</p>
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

  * - .. _ansible_collections.morpheus.core.cypher_module__attribute-check_mode:

      **check_mode**

    - Support: none



    - 
      Can run in check\_mode and return changed status prediction without modifying target



  * - .. _ansible_collections.morpheus.core.cypher_module__attribute-diff_mode:

      **diff_mode**

    - Support: none



    - 
      Will return details on what has changed (or possibly needs changing in check\_mode), when in diff mode



  * - .. _ansible_collections.morpheus.core.cypher_module__attribute-platform:

      **platform**

    - Platforms:


    - 
      Target OS/families that can be operated against






Examples
--------

.. code-block:: yaml

    
    - name: Generate a 7 Character Password
      morpheus.core.cypher:
        state: present
        cypher_path: password/7/my_password

    - name: Generate a 1024bit Key
      morpheus.core.cypher:
        state: present
        mount: key
        name: my_key
        length: 1024

    - name: Add a Secret with a 7 day Lease
      morpheus.core.cypher:
        state: present
        mount: secret
        name: my_secret
        value: 5uper5ecret
        ttl: 7d

    - name: Remove a UUID item
      morpheus.core.cypher:
        state: absent
        cypher_path: uuid/my_uuid





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
      <div class="ansibleOptionAnchor" id="return-cypher"></div>
      <p style="display: inline;"><strong>cypher</strong></p>
      <a class="ansibleOptionLink" href="#return-cypher" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Details of the Cypher item.</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;cypher&#34;: {&#34;created_by&#34;: &#34;130&#34;, &#34;data&#34;: &#34;rfYTVB&gt;1VNQpW5!%b{Sj=I60o!`q.V%jXk/Aga^0&amp;B_/p/w&gt;Q08~_0Pze_fhyfQrx)&#34;, &#34;date_created&#34;: null, &#34;expire_date&#34;: null, &#34;id&#34;: 165, &#34;item_key&#34;: &#34;password/64/my_pass&#34;, &#34;last_accessed&#34;: &#34;2024-01-01T00:00:01Z&#34;, &#34;last_updated&#34;: &#34;2024-01-01T00:00:01Z&#34;, &#34;lease_duration&#34;: null, &#34;lease_timeout&#34;: 0, &#34;success&#34;: true, &#34;type&#34;: &#34;string&#34;}}</code></p>
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

