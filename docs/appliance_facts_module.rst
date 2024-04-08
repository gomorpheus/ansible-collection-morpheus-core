
.. Created with antsibull-docs 2.7.0

morpheus.core.appliance_facts module -- Gather Morpheus Appliance Facts
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.0).

It is not included in ``ansible-core``.
To check whether it is installed, run ``ansible-galaxy collection list``.

To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

To use it in a playbook, specify: ``morpheus.core.appliance_facts``.

New in morpheus.core 0.3.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Gathers Morpheus Appliance Facts








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
      <div class="ansibleOptionAnchor" id="parameter-filter"></div>
      <p style="display: inline;"><strong>filter</strong></p>
      <a class="ansibleOptionLink" href="#parameter-filter" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </td>
    <td valign="top">
      <p>Match facts to one of the specified patterns.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">[]</code></p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-gather_subset"></div>
      <p style="display: inline;"><strong>gather_subset</strong></p>
      <a class="ansibleOptionLink" href="#parameter-gather_subset" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </td>
    <td valign="top">
      <p>Specify or restrict the facts that are gathered. Possible values: <code class="ansible-value literal notranslate">all</code>, <code class="ansible-value literal notranslate">database</code>, <code class="ansible-value literal notranslate">elastic</code>, <code class="ansible-value literal notranslate">license</code>, <code class="ansible-value literal notranslate">rabbitmq</code>, <code class="ansible-value literal notranslate">settings</code>, <code class="ansible-value literal notranslate">system</code>, <code class="ansible-value literal notranslate">threads</code>. The minimum subset is: <code class="ansible-value literal notranslate">license</code>, <code class="ansible-value literal notranslate">settings</code>, <code class="ansible-value literal notranslate">system</code>. To specify a specific subset, use <code class="ansible-value literal notranslate">!all, !min</code> and then specify the fact(s) required.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">[&#34;all&#34;]</code></p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-gather_timeout"></div>
      <p style="display: inline;"><strong>gather_timeout</strong></p>
      <a class="ansibleOptionLink" href="#parameter-gather_timeout" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Timeout period for collecting individual facts</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">10</code></p>
    </td>
  </tr>
  </tbody>
  </table>






Examples
--------

.. code-block:: yaml

    
    - name: Gather All Facts
      morpheus.core.appliance_facts:

    - name: Gather Minimum Facts
      morpheus.core.appliance_facts:
        gather_subset:
          - "!all"

    - name: Gather License Facts
      morpheus.core.appliance_facts:
        gather_subset:
          - "!all"
          - "!min"
          - "license"







Authors
~~~~~~~

- James Riach



Collection links
~~~~~~~~~~~~~~~~

* `Repository (Sources) <https://www.github.com/gomorpheus/ansible-collection-morpheus-core>`__

