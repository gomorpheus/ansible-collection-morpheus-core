
.. Created with antsibull-docs 2.7.0

morpheus.core.morpheus httpapi -- Httpapi Plugin for Morpheus
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This httpapi plugin is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.0).

It is not included in ``ansible-core``.
To check whether it is installed, run ``ansible-galaxy collection list``.

To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

To use it in a playbook, specify: ``morpheus.core.morpheus``.

New in morpheus.core 0.3.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Httpapi plugin to connect to and manage morpheus appliances through the morpheus api.








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
      <div class="ansibleOptionAnchor" id="parameter-morpheus_api_token"></div>
      <p style="display: inline;"><strong>morpheus_api_token</strong></p>
      <a class="ansibleOptionLink" href="#parameter-morpheus_api_token" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Specify an API token instead of <code class="ansible-option literal notranslate"><strong><a class="reference internal" href="#parameter-morpheus_user"><span class="std std-ref"><span class="pre">morpheus_user</span></span></a></strong></code> and <code class="ansible-option literal notranslate"><strong><a class="reference internal" href="#parameter-morpheus_password"><span class="std std-ref"><span class="pre">morpheus_password</span></span></a></strong></code>.</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Environment variable: <code>ANSIBLE_MORPHEUS_TOKEN</code></p>

      </li>
      <li>
        <p>Variable: ansible_morpheus_token</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-morpheus_password"></div>
      <p style="display: inline;"><strong>morpheus_password</strong></p>
      <a class="ansibleOptionLink" href="#parameter-morpheus_password" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>Password associated with the specified Username.</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Environment variable: <code>ANSIBLE_MORPHEUS_PASSWORD</code></p>

      </li>
      <li>
        <p>Variable: ansible_morpheus_password</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-morpheus_user"></div>
      <p style="display: inline;"><strong>morpheus_user</strong></p>
      <a class="ansibleOptionLink" href="#parameter-morpheus_user" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td valign="top">
      <p>A Morpheus Username to Authenticate as.</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Environment variable: <code>ANSIBLE_MORPHEUS_USER</code></p>

      </li>
      <li>
        <p>Variable: ansible_morpheus_user</p>

      </li>
      </ul>
    </td>
  </tr>
  </tbody>
  </table>











Authors
~~~~~~~

- James Riach


.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

Collection links
~~~~~~~~~~~~~~~~

* `Repository (Sources) <https://www.github.com/gomorpheus/ansible-collection-morpheus-core>`__

