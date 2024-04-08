
.. Created with antsibull-docs 2.7.0

morpheus.core.role_info module -- Retrieves Role Information
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.0).

It is not included in ``ansible-core``.
To check whether it is installed, run ``ansible-galaxy collection list``.

To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

To use it in a playbook, specify: ``morpheus.core.role_info``.

New in morpheus.core 0.7.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Retrieves list of Morpheus Roles.








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
      <div class="ansibleOptionAnchor" id="parameter-diverged"></div>
      <p style="display: inline;"><strong>diverged</strong></p>
      <a class="ansibleOptionLink" href="#parameter-diverged" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Filter roles that have diverged.</p>
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
      <div class="ansibleOptionAnchor" id="parameter-multitenant"></div>
      <p style="display: inline;"><strong>multitenant</strong></p>
      <a class="ansibleOptionLink" href="#parameter-multitenant" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Filter Multi-Tenant Roles.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
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
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-role_type"></div>
      <p style="display: inline;"><strong>role_type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-role_type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Filter by Type of Role.</p>
      <p><code class="ansible-value literal notranslate">account</code> and <code class="ansible-value literal notranslate">tenant</code> are the same.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;account&#34;</code></p></li>
        <li><p><code>&#34;tenant&#34;</code></p></li>
        <li><p><code>&#34;user&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  </tbody>
  </table>






Examples
--------

.. code-block:: yaml

    
    - name: Get all Roles
      morpheus.core.role_info:

    - name: Get Role by specific Id
      morpheus.core.role_info:
        id: 120

    - name: Get all Account/Tenant Roles
      morpheus.core.role_info:
        role_type: tenant

    - name: Get all multitenant Roles
      morpheus.core.role_info:
        multitenant: true





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
      <div class="ansibleOptionAnchor" id="return-roles"></div>
      <p style="display: inline;"><strong>roles</strong></p>
      <a class="ansibleOptionLink" href="#return-roles" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>List of matching roles.</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;roles&#34;: [{&#34;authority&#34;: &#34;Support&#34;, &#34;date_created&#34;: &#34;2022-01-01T00:00:01Z&#34;, &#34;default_persona&#34;: null, &#34;description&#34;: &#34;Support Role&#34;, &#34;diverged&#34;: false, &#34;id&#34;: 10, &#34;last_updated&#34;: &#34;2022-01-01T00:00:01Z&#34;, &#34;multitenant&#34;: true, &#34;multitenant_locked&#34;: true, &#34;name&#34;: &#34;Support&#34;, &#34;owner&#34;: {&#34;id&#34;: 1, &#34;name&#34;: &#34;Owner&#34;}, &#34;owner_id&#34;: 1, &#34;parent_role_id&#34;: null, &#34;role_type&#34;: &#34;user&#34;, &#34;scope&#34;: &#34;Account&#34;}]}</code></p>
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

