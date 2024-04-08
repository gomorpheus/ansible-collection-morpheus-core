
.. Created with antsibull-docs 2.7.0

morpheus.core.tenant module -- Manage Tenants
+++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.0).

It is not included in ``ansible-core``.
To check whether it is installed, run ``ansible-galaxy collection list``.

To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

To use it in a playbook, specify: ``morpheus.core.tenant``.

New in morpheus.core 0.7.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Create, Update and Remove Tenants.








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
      <p>Additional Tenant Identifier.</p>
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
      <p>Additional Tenant Identifier.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-currency"></div>
      <p style="display: inline;"><strong>currency</strong></p>
      <a class="ansibleOptionLink" href="#parameter-currency" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>ISO Currency Code.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;AUD&#34;</code></p></li>
        <li><p><code>&#34;BGN&#34;</code></p></li>
        <li><p><code>&#34;BRL&#34;</code></p></li>
        <li><p><code>&#34;CAD&#34;</code></p></li>
        <li><p><code>&#34;CHF&#34;</code></p></li>
        <li><p><code>&#34;CLF&#34;</code></p></li>
        <li><p><code>&#34;CLP&#34;</code></p></li>
        <li><p><code>&#34;CNY&#34;</code></p></li>
        <li><p><code>&#34;CZK&#34;</code></p></li>
        <li><p><code>&#34;DKK&#34;</code></p></li>
        <li><p><code>&#34;EUR&#34;</code></p></li>
        <li><p><code>&#34;GBP&#34;</code></p></li>
        <li><p><code>&#34;HKD&#34;</code></p></li>
        <li><p><code>&#34;HRK&#34;</code></p></li>
        <li><p><code>&#34;HUF&#34;</code></p></li>
        <li><p><code>&#34;IDR&#34;</code></p></li>
        <li><p><code>&#34;ILS&#34;</code></p></li>
        <li><p><code>&#34;INR&#34;</code></p></li>
        <li><p><code>&#34;JPY&#34;</code></p></li>
        <li><p><code>&#34;KRW&#34;</code></p></li>
        <li><p><code>&#34;MXN&#34;</code></p></li>
        <li><p><code>&#34;MYR&#34;</code></p></li>
        <li><p><code>&#34;NOK&#34;</code></p></li>
        <li><p><code>&#34;NZD&#34;</code></p></li>
        <li><p><code>&#34;PHP&#34;</code></p></li>
        <li><p><code>&#34;PLN&#34;</code></p></li>
        <li><p><code>&#34;RON&#34;</code></p></li>
        <li><p><code>&#34;RUB&#34;</code></p></li>
        <li><p><code>&#34;SEK&#34;</code></p></li>
        <li><p><code>&#34;SGD&#34;</code></p></li>
        <li><p><code>&#34;THB&#34;</code></p></li>
        <li><p><code>&#34;TRY&#34;</code></p></li>
        <li><p><code>&#34;USD&#34;</code></p></li>
        <li><p><code>&#34;ZAR&#34;</code></p></li>
      </ul>

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
      <p>Additional Tenant Identifier.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-description"></div>
      <p style="display: inline;"><strong>description</strong></p>
      <a class="ansibleOptionLink" href="#parameter-description" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Description for the Tenant.</p>
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
      <p>The Id of an existing Tenant.</p>
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
      <p>The name of the Tenant.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-role"></div>
      <p style="display: inline;"><strong>role</strong></p>
      <a class="ansibleOptionLink" href="#parameter-role" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Id of a Role to act as the Tenant base role.</p>
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
      <p>The state of the Tenant.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;absent&#34;</code></p></li>
        <li><p><code style="color: blue;"><b>&#34;present&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-subdomain"></div>
      <p style="display: inline;"><strong>subdomain</strong></p>
      <a class="ansibleOptionLink" href="#parameter-subdomain" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Subdomain name used in login URL and subtenant users.</p>
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

  * - .. _ansible_collections.morpheus.core.tenant_module__attribute-check_mode:

      **check_mode**

    - Support: full



    - 
      Can run in check\_mode and return changed status prediction without modifying target



  * - .. _ansible_collections.morpheus.core.tenant_module__attribute-diff_mode:

      **diff_mode**

    - Support: full



    - 
      Will return details on what has changed (or possibly needs changing in check\_mode), when in diff mode



  * - .. _ansible_collections.morpheus.core.tenant_module__attribute-platform:

      **platform**

    - Platforms:


    - 
      Target OS/families that can be operated against






Examples
--------

.. code-block:: yaml

    
    - name: Create / Update Tenant
      morpheus.core.tenant:
        name: Test Tenant
        description: Testing Tenant
        role: 4
        subdomain: test
        currency: GBP

    - name: Remove Tenant
      morpheus.core.tenant:
        state: absent
        name: Test Tenant





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
      <div class="ansibleOptionAnchor" id="return-tenant"></div>
      <p style="display: inline;"><strong>tenant</strong></p>
      <a class="ansibleOptionLink" href="#return-tenant" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Details of the Tenant state.</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;tenant&#34;: {&#34;account_name&#34;: null, &#34;account_number&#34;: null, &#34;active&#34;: true, &#34;currency&#34;: &#34;GBP&#34;, &#34;customer_number&#34;: null, &#34;date_created&#34;: &#34;2024-01-01T00:00:01Z&#34;, &#34;description&#34;: &#34;Testing Tenant&#34;, &#34;external_id&#34;: null, &#34;id&#34;: 30, &#34;last_updated&#34;: &#34;2024-01-01T00:00:01Z&#34;, &#34;master&#34;: false, &#34;name&#34;: &#34;Test Tenant&#34;, &#34;role&#34;: {&#34;authority&#34;: &#34;Customer Base Role&#34;, &#34;description&#34;: null, &#34;id&#34;: 4, &#34;name&#34;: &#34;Customer Base Role&#34;}, &#34;stats&#34;: {&#34;instance_count&#34;: 0, &#34;user_count&#34;: 0}, &#34;subdomain&#34;: &#34;test&#34;}}</code></p>
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

