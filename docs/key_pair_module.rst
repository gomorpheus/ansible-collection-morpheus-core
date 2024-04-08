
.. Created with antsibull-docs 2.7.0

morpheus.core.key_pair module -- Create and Remove Key Pairs
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.0).

It is not included in ``ansible-core``.
To check whether it is installed, run ``ansible-galaxy collection list``.

To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

To use it in a playbook, specify: ``morpheus.core.key_pair``.

New in morpheus.core 0.6.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Create and Remove Key Pairs.
- Keys can be user provided or generated.








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
      <p>Required when <code class="ansible-option-value literal notranslate"><a class="reference internal" href="#parameter-state"><span class="std std-ref"><span class="pre">state=absent</span></span></a></code>, specify the Key Pair to remove.</p>
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
      <p>Required when <code class="ansible-option-value literal notranslate"><a class="reference internal" href="#parameter-state"><span class="std std-ref"><span class="pre">state=present</span></span></a></code>, specify the name of the Key Pair.</p>
      <p>Specifying this parameter alone will generate a Key Pair.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-passphrase"></div>
      <p style="display: inline;"><strong>passphrase</strong></p>
      <a class="ansibleOptionLink" href="#parameter-passphrase" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify the Private Key passphrase.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-private_key"></div>
      <p style="display: inline;"><strong>private_key</strong></p>
      <a class="ansibleOptionLink" href="#parameter-private_key" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify the Private Key.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-public_key"></div>
      <p style="display: inline;"><strong>public_key</strong></p>
      <a class="ansibleOptionLink" href="#parameter-public_key" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify the Public Key.</p>
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
      <p>Create or Remove a Key Pair.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;absent&#34;</code></p></li>
        <li><p><code style="color: blue;"><b>&#34;present&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
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

  * - .. _ansible_collections.morpheus.core.key_pair_module__attribute-check_mode:

      **check_mode**

    - Support: none



    - 
      Can run in check\_mode and return changed status prediction without modifying target



  * - .. _ansible_collections.morpheus.core.key_pair_module__attribute-diff_mode:

      **diff_mode**

    - Support: full



    - 
      Will return details on what has changed (or possibly needs changing in check\_mode), when in diff mode



  * - .. _ansible_collections.morpheus.core.key_pair_module__attribute-platform:

      **platform**

    - Platforms:


    - 
      Target OS/families that can be operated against






Examples
--------

.. code-block:: yaml

    
    - name: Generate a Key Pair
      morpheus.core.key_pair:
        state: present
        name: My Generated Key Pair

    - name: Add a Key Pair
      morpheus.core.key_pair:
        state: present
        name: My Existing Key Pair
        private_key: "{{ q('ansible.builtin.file', 'path/to/private_key')[0] }}"
        public_key: "{{ q('ansible.builtin.file', 'path/to/public_key')[0] }}"
        passphrase: Password123

    - name: Delete a Key Pair
      morpheus.core.key_pair:
        state: absent
        id: 50





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
      <div class="ansibleOptionAnchor" id="return-errors"></div>
      <p style="display: inline;"><strong>errors</strong></p>
      <a class="ansibleOptionLink" href="#return-errors" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Any errors when generating or adding a Key Pair.</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;errors&#34;: {&#34;private_key&#34;: &#34;Unable to generate public key from private key&#34;}}</code></p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="return-key_pair"></div>
      <p style="display: inline;"><strong>key_pair</strong></p>
      <a class="ansibleOptionLink" href="#return-key_pair" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Dictionary information about the Key Pair.</p>
      <p>If this was a Generated Key Pair, it will include details of the Private Key.</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;key_pair&#34;: {&#34;account_id&#34;: 1, &#34;date_created&#34;: &#34;2023-10-23T11:56:56Z&#34;, &#34;fingerprint&#34;: &#34;0f:f7:4c:5a:71:60:47:11:56:bb:1b:1f:ff:b4:70:cb&#34;, &#34;has_private_key&#34;: false, &#34;id&#34;: 50, &#34;last_updated&#34;: &#34;2023-10-23T11:56:56Z&#34;, &#34;name&#34;: &#34;Ansible Created Key Pair&#34;, &#34;private_key_hash&#34;: null, &#34;public_key&#34;: &#34;ssh-rsa AAAAB3N...&#34;}}</code></p>
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

