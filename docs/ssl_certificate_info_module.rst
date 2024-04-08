
.. Created with antsibull-docs 2.7.0

morpheus.core.ssl_certificate_info module -- Gather information about SSL Certificates
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.0).

It is not included in ``ansible-core``.
To check whether it is installed, run ``ansible-galaxy collection list``.

To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

To use it in a playbook, specify: ``morpheus.core.ssl_certificate_info``.

New in morpheus.core 0.6.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Gathers information about SSL Certificates.








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

    
    - name: Get All SSL Certificates
      morpheus.core.ssl_certificate_info:

    - name: Get Specific Certificate by Id
      morpheus.core.ssl_certificate_info:
        id: 20

    - name: Get Certificates matching Regular Expression
      morpheus.core.ssl_certificate_info:
        name: ^Web.*$
        regex_name: true





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
      <div class="ansibleOptionAnchor" id="return-certificates"></div>
      <p style="display: inline;"><strong>certificates</strong></p>
      <a class="ansibleOptionLink" href="#return-certificates" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>List of SSL Certificates.</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;certificates&#34;: [{&#34;account_id&#34;: 1, &#34;category&#34;: null, &#34;cert_type&#34;: &#34;server&#34;, &#34;common_name&#34;: null, &#34;description&#34;: &#34;Dev Web Server&#34;, &#34;domain_name&#34;: &#34;dev.domain.tld&#34;, &#34;enabled&#34;: true, &#34;generated&#34;: false, &#34;id&#34;: 73, &#34;integration_id&#34;: null, &#34;key_file_md5&#34;: &#34;0000....&#34;, &#34;name&#34;: &#34;Dev Web Server&#34;, &#34;self_signed&#34;: false, &#34;type&#34;: {&#34;code&#34;: &#34;internal&#34;, &#34;id&#34;: 1}, &#34;wildcard&#34;: false}]}</code></p>
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

