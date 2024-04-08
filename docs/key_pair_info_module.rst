
.. Created with antsibull-docs 2.7.0

morpheus.core.key_pair_info module -- Gather Key Pair Information
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.0).

It is not included in ``ansible-core``.
To check whether it is installed, run ``ansible-galaxy collection list``.

To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

To use it in a playbook, specify: ``morpheus.core.key_pair_info``.

New in morpheus.core 0.6.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Gathers Information of Key Pairs.








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
      <div class="ansibleOptionAnchor" id="parameter-has_private_key"></div>
      <p style="display: inline;"><strong>has_private_key</strong></p>
      <a class="ansibleOptionLink" href="#parameter-has_private_key" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Filter Key Pairs with or without a stored Private Key.</p>
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

    
    - name: Get Specific Key by Id
      morpheus.core.key_pair_info:
        id: 20

    - name: Get Keys matching Regular Expression
      morpheus.core.key_pair_info:
        name: ^morpheus_.*$
        regex_name: true

    - name: Get All Keys with Private Key
      morpheus.core.key_pair_info:
        has_private_key: true





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
      <div class="ansibleOptionAnchor" id="return-key_pairs"></div>
      <p style="display: inline;"><strong>key_pairs</strong></p>
      <a class="ansibleOptionLink" href="#return-key_pairs" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>List of Key Pairs.</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;key_pairs&#34;: [{&#34;account_id&#34;: 1, &#34;date_created&#34;: &#34;2023-07-18T08:39:48Z&#34;, &#34;fingerprint&#34;: null, &#34;has_private_key&#34;: false, &#34;id&#34;: 1, &#34;last_updated&#34;: &#34;2023-07-18T08:39:48Z&#34;, &#34;name&#34;: &#34;dev-ssh-key&#34;, &#34;private_key_hash&#34;: null, &#34;public_key&#34;: &#34;ssh-rsa AAAAB3...&#34;}, {&#34;account_id&#34;: 1, &#34;date_created&#34;: &#34;2023-07-18T08:39:48Z&#34;, &#34;fingerprint&#34;: null, &#34;has_private_key&#34;: false, &#34;id&#34;: 2, &#34;last_updated&#34;: &#34;2023-07-18T08:39:48Z&#34;, &#34;name&#34;: &#34;test-ssh-key&#34;, &#34;private_key_hash&#34;: null, &#34;public_key&#34;: &#34;ssh-rsa AAAAB3...&#34;}]}</code></p>
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

