
.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.9.0

.. Anchors

.. _ansible_collections.morpheus.core.morpheus_httpapi:

.. Anchors: short name for ansible.builtin

.. Title

morpheus.core.morpheus httpapi -- Httpapi Plugin for Morpheus
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This httpapi plugin is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.1).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

    To use it in a playbook, specify: :code:`morpheus.core.morpheus`.

.. version_added

.. rst-class:: ansible-version-added

New in morpheus.core 0.3.0

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Httpapi plugin to connect to and manage morpheus appliances through the morpheus api.


.. Aliases


.. Requirements






.. Options

Parameters
----------

.. tabularcolumns:: \X{1}{3}\X{2}{3}

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1
  :class: longtable ansible-option-table

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-morpheus_api_token"></div>

      .. _ansible_collections.morpheus.core.morpheus_httpapi__parameter-morpheus_api_token:

      .. rst-class:: ansible-option-title

      **morpheus_api_token**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-morpheus_api_token" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Specify an API token instead of \ :ansopt:`morpheus.core.morpheus#httpapi:morpheus\_user`\  and \ :ansopt:`morpheus.core.morpheus#httpapi:morpheus\_password`\ .


      .. rst-class:: ansible-option-line

      :ansible-option-configuration:`Configuration:`

      - Environment variable: :envvar:`ANSIBLE\_MORPHEUS\_TOKEN`

      - Variable: ansible\_morpheus\_token


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-morpheus_password"></div>

      .. _ansible_collections.morpheus.core.morpheus_httpapi__parameter-morpheus_password:

      .. rst-class:: ansible-option-title

      **morpheus_password**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-morpheus_password" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Password associated with the specified Username.


      .. rst-class:: ansible-option-line

      :ansible-option-configuration:`Configuration:`

      - Environment variable: :envvar:`ANSIBLE\_MORPHEUS\_PASSWORD`

      - Variable: ansible\_morpheus\_password


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-morpheus_user"></div>

      .. _ansible_collections.morpheus.core.morpheus_httpapi__parameter-morpheus_user:

      .. rst-class:: ansible-option-title

      **morpheus_user**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-morpheus_user" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A Morpheus Username to Authenticate as.


      .. rst-class:: ansible-option-line

      :ansible-option-configuration:`Configuration:`

      - Environment variable: :envvar:`ANSIBLE\_MORPHEUS\_USER`

      - Variable: ansible\_morpheus\_user


      .. raw:: html

        </div>


.. Attributes


.. Notes


.. Seealso


.. Examples



.. Facts


.. Return values


..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- James Riach (@McGlovin1337)


.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. ansible-links::

  - title: "Repository (Sources)"
    url: "https://www.github.com/gomorpheus/ansible-collection-morpheus-core"
    external: true


.. Parsing errors

