
.. Created with antsibull-docs 2.7.0

morpheus.core.cypher_info module -- Return Cypher Information
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.0).

It is not included in ``ansible-core``.
To check whether it is installed, run ``ansible-galaxy collection list``.

To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

To use it in a playbook, specify: ``morpheus.core.cypher_info``.

New in morpheus.core 0.7.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Returns items stored in Cypher.








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
      <p>Filter Cypher items by path.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-decrypt"></div>
      <p style="display: inline;"><strong>decrypt</strong></p>
      <a class="ansibleOptionLink" href="#parameter-decrypt" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify to decrypt matching Cypher items.</p>
      <p>Requires <code class="ansible-option literal notranslate"><strong><a class="reference internal" href="#parameter-cypher_path"><span class="std std-ref"><span class="pre">cypher_path</span></span></a></strong></code> to be specified, cannot be used to decrypt all items when no parameters are specified.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-regex_match"></div>
      <p style="display: inline;"><strong>regex_match</strong></p>
      <a class="ansibleOptionLink" href="#parameter-regex_match" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify to treat <code class="ansible-option literal notranslate"><strong><a class="reference internal" href="#parameter-cypher_path"><span class="std std-ref"><span class="pre">cypher_path</span></span></a></strong></code> as regex.</p>
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

    
    - name: List all items in Cypher
      morpheus.core.cypher_info:

    - name: List items matching regex pattern
      morpheus.core.cypher_info:
        cypher_path: ^.*vcenter.*$
        regex_match: true

    - name: Return a specific item and decrypt
      morpheus.core.cypher_info:
        cypher_path: secret/my_secret
        decrypt: true

    - name: List items matching pattern and decrypt
      morpheus.core.cypher_info:
        cypher_path: ^password/.*/my_pass$
        regex_match: true
        decrypt: true





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
      <div class="ansibleOptionAnchor" id="return-cyphers"></div>
      <p style="display: inline;"><strong>cyphers</strong></p>
      <a class="ansibleOptionLink" href="#return-cyphers" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>List of items stored in Cypher.</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;cyphers&#34;: [{&#34;created_by&#34;: &#34;15&#34;, &#34;date_created&#34;: &#34;2024-01-01T00:00:01Z&#34;, &#34;expire_date&#34;: null, &#34;id&#34;: 99, &#34;item_key&#34;: &#34;secret/netbox_token&#34;, &#34;last_accessed&#34;: &#34;2024-03-28T15:36:38Z&#34;, &#34;last_updated&#34;: &#34;2024-01-01T00:00:01Z&#34;, &#34;lease_timeout&#34;: 0}, {&#34;created_by&#34;: &#34;1&#34;, &#34;date_created&#34;: null, &#34;expire_date&#34;: null, &#34;id&#34;: 100, &#34;item_key&#34;: &#34;secret/redhat8templatepass&#34;, &#34;last_accessed&#34;: &#34;2024-01-01T00:00:01Z&#34;, &#34;last_updated&#34;: &#34;2024-01-01T00:00:01Z&#34;, &#34;lease_timeout&#34;: 0}]}</code></p>
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

