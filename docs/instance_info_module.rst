
.. Created with antsibull-docs 2.7.0

morpheus.core.instance_info module -- Gather information about instances
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.0).

It is not included in ``ansible-core``.
To check whether it is installed, run ``ansible-galaxy collection list``.

To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

To use it in a playbook, specify: ``morpheus.core.instance_info``.

New in morpheus.core 0.4.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Gathers information about Morpheus instances








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
      <div class="ansibleOptionAnchor" id="parameter-agent_installed"></div>
      <p style="display: inline;"><strong>agent_installed</strong></p>
      <a class="ansibleOptionLink" href="#parameter-agent_installed" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Filter by if agent is installed or not.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-deleted"></div>
      <p style="display: inline;"><strong>deleted</strong></p>
      <a class="ansibleOptionLink" href="#parameter-deleted" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Include, Exclude or Only show deleted instances or those pending removal.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;exclude&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;include&#34;</code></p></li>
        <li><p><code>&#34;only&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-detail"></div>
      <p style="display: inline;"><strong>detail</strong></p>
      <a class="ansibleOptionLink" href="#parameter-detail" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify the level of detail returned for matching instances.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;minimal&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;full&#34;</code></p></li>
        <li><p><code>&#34;extra&#34;</code></p></li>
        <li><p><code>&#34;summary&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-environment"></div>
      <p style="display: inline;"><strong>environment</strong></p>
      <a class="ansibleOptionLink" href="#parameter-environment" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Filter instances by environment.</p>
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
      <p>Specify the id of an instance.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-instance_type"></div>
      <p style="display: inline;"><strong>instance_type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-instance_type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Filter by the instance type code.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-labels"></div>
      <p style="display: inline;"><strong>labels</strong></p>
      <a class="ansibleOptionLink" href="#parameter-labels" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </td>
    <td valign="top">
      <p>Filter instances by matching labels.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-match_all_labels"></div>
      <p style="display: inline;"><strong>match_all_labels</strong></p>
      <a class="ansibleOptionLink" href="#parameter-match_all_labels" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>If labels have been specified, filter instances by those that match all specified labels.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
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
      <div class="ansibleOptionAnchor" id="parameter-status"></div>
      <p style="display: inline;"><strong>status</strong></p>
      <a class="ansibleOptionLink" href="#parameter-status" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Filter by instance status, e.g. running</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-tags"></div>
      <p style="display: inline;"><strong>tags</strong></p>
      <a class="ansibleOptionLink" href="#parameter-tags" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </td>
    <td valign="top">
      <p>Filter instances by matching tags.</p>
    </td>
  </tr>
  </tbody>
  </table>






Examples
--------

.. code-block:: yaml

    
    - name: Get Info for a Specific Instance by id
      morpheus.core.instance_info:
        id: 200

    - name: Get a short summary of instances
      morpheus.core.instance_info:
        detail: summary

    - name: Get Info for instance by name
      morpheus.core.instance_info:
        name: WebServer001

    - name: Get Info for instances where name matches regular expression
      morpheus.core.instance_info:
        name: ^WebServer.*$
        regex_name: true

    - name: Get Extra Info for a Specific Instance by id
      morpheus.core.instance_info:
        id: 200
        detail: extra

    - name: Get Info for all Instances with any of the specified labels
      morpheus.core.instance_info:
        labels:
          - foo
          - bar
          - prod

    - name: Get Info of all Running Instances
      morpheus.core.instance_info:
        status: running





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
      <div class="ansibleOptionAnchor" id="return-morpheus_instances"></div>
      <p style="display: inline;"><strong>morpheus_instances</strong></p>
      <a class="ansibleOptionLink" href="#return-morpheus_instances" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>List of instances with info</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;morpheus_instances&#34;: [{&#34;cloud&#34;: {&#34;id&#34;: 31, &#34;name&#34;: &#34;VMWare Cloud&#34;, &#34;type&#34;: &#34;vmware&#34;}, &#34;connection_info&#34;: [{&#34;ip&#34;: &#34;192.168.0.10&#34;, &#34;name&#34;: null, &#34;port&#34;: null}], &#34;date_created&#34;: &#34;2023-06-01T13:37:00Z&#34;, &#34;description&#34;: &#34;Webserver Instance&#34;, &#34;id&#34;: 100, &#34;instance_type&#34;: {&#34;code&#34;: &#34;win2019&#34;, &#34;id&#34;: 110, &#34;name&#34;: &#34;Windows Server 2019&#34;}, &#34;instance_version&#34;: &#34;2019&#34;, &#34;interfaces&#34;: [{&#34;id&#34;: &#34;network-100&#34;, &#34;ip_address&#34;: null, &#34;ip_mode&#34;: null, &#34;network&#34;: {&#34;dhcp_server&#34;: false, &#34;group&#34;: null, &#34;id&#34;: 150, &#34;name&#34;: &#34;inside-network-001&#34;, &#34;pool&#34;: {&#34;id&#34;: 30, &#34;name&#34;: &#34;inside-network-pool-001&#34;}, &#34;subnet&#34;: null}, &#34;network_interface_type_id&#34;: null}], &#34;labels&#34;: [&#34;production&#34;, &#34;webservers&#34;], &#34;name&#34;: &#34;WebServ001&#34;, &#34;owner&#34;: {&#34;username&#34;: &#34;patrick.clifton@domain.tld&#34;}, &#34;plan&#34;: {&#34;name&#34;: &#34;Cheap Plan 001&#34;}, &#34;stats&#34;: {&#34;cpu_usage&#34;: 0, &#34;cpu_usage_avg&#34;: 0, &#34;cpu_usage_peak&#34;: 0.0, &#34;max_memory&#34;: 4293943296, &#34;max_storage&#34;: 53687091200, &#34;used_cpu&#34;: 0.0, &#34;used_memory&#34;: 2080228608, &#34;used_storage&#34;: 25341928960}, &#34;status&#34;: &#34;running&#34;, &#34;volumes&#34;: [{&#34;name&#34;: &#34;root&#34;, &#34;resizeable&#34;: true, &#34;root_volume&#34;: true, &#34;size&#34;: 50}]}]}</code></p>
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

