
.. Created with antsibull-docs 2.7.0

morpheus.core.morpheus_inventory inventory -- Returns Ansible inventory from Morpheus
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This inventory plugin is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.0).

It is not included in ``ansible-core``.
To check whether it is installed, run ``ansible-galaxy collection list``.

To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

To use it in a playbook, specify: ``morpheus.core.morpheus_inventory``.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Returns Ansible inventory from Morpheus








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
      <div class="ansibleOptionAnchor" id="parameter-groups"></div>
      <p style="display: inline;"><strong>groups</strong></p>
      <a class="ansibleOptionLink" href="#parameter-groups" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>

    </td>
    <td valign="top">
      <p>whatever</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-morpheus_api_key"></div>
      <p style="display: inline;"><strong>morpheus_api_key</strong></p>
      <a class="ansibleOptionLink" href="#parameter-morpheus_api_key" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Morpheus API Key - Can be a vault encrypted string</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-morpheus_url"></div>
      <p style="display: inline;"><strong>morpheus_url</strong></p>
      <a class="ansibleOptionLink" href="#parameter-morpheus_url" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Morpheus URL</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-plugin"></div>
      <p style="display: inline;"><strong>plugin</strong></p>
      <a class="ansibleOptionLink" href="#parameter-plugin" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>

    </td>
    <td valign="top">
      <p>Morpheus Inventory</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;morpheus_inventory&#34;</code></p></li>
        <li><p><code>&#34;morpheus.core.morpheus_inventory&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-searchstring"></div>
      <p style="display: inline;"><strong>searchstring</strong></p>
      <a class="ansibleOptionLink" href="#parameter-searchstring" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Search term</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-searchtype"></div>
      <p style="display: inline;"><strong>searchtype</strong></p>
      <a class="ansibleOptionLink" href="#parameter-searchtype" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Search type</p>
    </td>
  </tr>
  </tbody>
  </table>












.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

Collection links
~~~~~~~~~~~~~~~~

* `Repository (Sources) <https://www.github.com/gomorpheus/ansible-collection-morpheus-core>`__

