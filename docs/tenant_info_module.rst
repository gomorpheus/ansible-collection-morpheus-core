
.. Created with antsibull-docs 2.7.0

morpheus.core.tenant_info module -- Retrieves Tenant Info
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.0).

It is not included in ``ansible-core``.
To check whether it is installed, run ``ansible-galaxy collection list``.

To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

To use it in a playbook, specify: ``morpheus.core.tenant_info``.

New in morpheus.core 0.7.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Returns information about Morpheus Tenants.








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
      <div class="ansibleOptionAnchor" id="parameter-account_name"></div>
      <p style="display: inline;"><strong>account_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-account_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Filter tenants by account name.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-account_number"></div>
      <p style="display: inline;"><strong>account_number</strong></p>
      <a class="ansibleOptionLink" href="#parameter-account_number" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Filter tenants by account number.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-customer_number"></div>
      <p style="display: inline;"><strong>customer_number</strong></p>
      <a class="ansibleOptionLink" href="#parameter-customer_number" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Filter tenants by customer number.</p>
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

    
    - name: Get Info for a Specific Tenant by id
      morpheus.core.tenant_info:
        id: 50

    - name: Get Tenants Matching Regex Name
      morpheus.core.tenant_info:
        name: ^tenant.*$
        regex_name: true

    - name: Get Tenant with Matching Customer Number
      morpheus.core.tenant_info:
        customer_number: T3ST





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
      <div class="ansibleOptionAnchor" id="return-tenants"></div>
      <p style="display: inline;"><strong>tenants</strong></p>
      <a class="ansibleOptionLink" href="#return-tenants" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>List of matching tenants.</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;tenants&#34;: [{&#34;account_name&#34;: null, &#34;account_number&#34;: null, &#34;active&#34;: true, &#34;currency&#34;: &#34;GBP&#34;, &#34;customer_number&#34;: &#34;T3ST&#34;, &#34;date_created&#34;: &#34;2022-01-01T0:00:01Z&#34;, &#34;description&#34;: null, &#34;external_id&#34;: null, &#34;id&#34;: 10, &#34;last_updated&#34;: &#34;2022-01-01T0:00:01Z&#34;, &#34;master&#34;: true, &#34;name&#34;: &#34;TestTenant&#34;, &#34;role&#34;: {&#34;authority&#34;: &#34;Tenant Base Role&#34;, &#34;description&#34;: null, &#34;id&#34;: 5, &#34;name&#34;: &#34;Tenant Base Role&#34;}, &#34;stats&#34;: {&#34;instance_count&#34;: 5, &#34;user_count&#34;: 10}, &#34;subdomain&#34;: &#34;test&#34;}]}</code></p>
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

