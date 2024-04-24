
.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.9.0

.. Anchors

.. _ansible_collections.morpheus.core.cypher_module:

.. Anchors: short name for ansible.builtin

.. Title

morpheus.core.cypher module -- Manage items stored in Cypher
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.1).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

    To use it in a playbook, specify: :code:`morpheus.core.cypher`.

.. version_added

.. rst-class:: ansible-version-added

New in morpheus.core 0.7.0

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Create and Delete items stored in Cypher.


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
        <div class="ansibleOptionAnchor" id="parameter-cypher_path"></div>

      .. _ansible_collections.morpheus.core.cypher_module__parameter-cypher_path:

      .. rst-class:: ansible-option-title

      **cypher_path**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-cypher_path" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Specify a full Cypher mount and key path.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-length"></div>

      .. _ansible_collections.morpheus.core.cypher_module__parameter-length:

      .. rst-class:: ansible-option-title

      **length**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-length" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Required if \ :ansopt:`morpheus.core.cypher#module:mount`\  is either \ :ansval:`key`\  or \ :ansval:`password`\ 

      For \ :ansopt:`morpheus.core.cypher#module:mount=key`\  specify the bit length for the generated key.

      For \ :ansopt:`morpheus.core.cypher#module:mount=password`\  specify the character length for the generated password.

      Mutually exclusive with \ :ansopt:`morpheus.core.cypher#module:cypher\_path`\ .


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-mount"></div>

      .. _ansible_collections.morpheus.core.cypher_module__parameter-mount:

      .. rst-class:: ansible-option-title

      **mount**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-mount" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Specify the Cypher mount point.

      Mutually exclusive with \ :ansopt:`morpheus.core.cypher#module:cypher\_path`\ .


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"key"`
      - :ansible-option-choices-entry:`"password"`
      - :ansible-option-choices-entry:`"secret"`
      - :ansible-option-choices-entry:`"tfvars"`
      - :ansible-option-choices-entry:`"uuid"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-name"></div>

      .. _ansible_collections.morpheus.core.cypher_module__parameter-name:

      .. rst-class:: ansible-option-title

      **name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Specify the Key Name.

      Required when \ :ansopt:`morpheus.core.cypher#module:mount`\  is specified.

      Mutually exclusive with \ :ansopt:`morpheus.core.cypher#module:cypher\_path`\ .


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.morpheus.core.cypher_module__parameter-state:

      .. rst-class:: ansible-option-title

      **state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      State of the stored item.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"absent"`
      - :ansible-option-choices-entry-default:`"present"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-ttl"></div>
        <div class="ansibleOptionAnchor" id="parameter-lease_duration"></div>
        <div class="ansibleOptionAnchor" id="parameter-duration"></div>

      .. _ansible_collections.morpheus.core.cypher_module__parameter-duration:
      .. _ansible_collections.morpheus.core.cypher_module__parameter-lease_duration:
      .. _ansible_collections.morpheus.core.cypher_module__parameter-ttl:

      .. rst-class:: ansible-option-title

      **ttl**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-ttl" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-aliases:`aliases: lease_duration, duration`

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Specify the lease duration either in seconds or human readable format, e.g 15m, 8h, 7d.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"0"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-value"></div>

      .. _ansible_collections.morpheus.core.cypher_module__parameter-value:

      .. rst-class:: ansible-option-title

      **value**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-value" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Specify the data to be stored when \ :ansopt:`morpheus.core.cypher#module:mount`\  is either \ :ansval:`secret`\  or \ :ansval:`tfvars`\ .

      Required when \ :ansopt:`morpheus.core.cypher#module:mount`\  is either \ :ansval:`secret`\  or \ :ansval:`tfvars`\ .


      .. raw:: html

        </div>


.. Attributes


Attributes
----------

.. tabularcolumns:: \X{2}{10}\X{3}{10}\X{5}{10}

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1
  :class: longtable ansible-option-table

  * - Attribute
    - Support
    - Description

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="attribute-check_mode"></div>

      .. _ansible_collections.morpheus.core.cypher_module__attribute-check_mode:

      .. rst-class:: ansible-option-title

      **check_mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#attribute-check_mode" title="Permalink to this attribute"></a>

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      :ansible-attribute-support-label:`Support: \ `\ :ansible-attribute-support-none:`none`


      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Can run in check\_mode and return changed status prediction without modifying target


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="attribute-diff_mode"></div>

      .. _ansible_collections.morpheus.core.cypher_module__attribute-diff_mode:

      .. rst-class:: ansible-option-title

      **diff_mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#attribute-diff_mode" title="Permalink to this attribute"></a>

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      :ansible-attribute-support-label:`Support: \ `\ :ansible-attribute-support-none:`none`


      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Will return details on what has changed (or possibly needs changing in check\_mode), when in diff mode


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="attribute-platform"></div>

      .. _ansible_collections.morpheus.core.cypher_module__attribute-platform:

      .. rst-class:: ansible-option-title

      **platform**

      .. raw:: html

        <a class="ansibleOptionLink" href="#attribute-platform" title="Permalink to this attribute"></a>

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      :ansible-attribute-support-property:`Platform:` |antsibull-internal-nbsp|:ansible-attribute-support-full:`httpapi`


      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Target OS/families that can be operated against


      .. raw:: html

        </div>



.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Generate a 7 Character Password
      morpheus.core.cypher:
        state: present
        cypher_path: password/7/my_password

    - name: Generate a 1024bit Key
      morpheus.core.cypher:
        state: present
        mount: key
        name: my_key
        length: 1024

    - name: Add a Secret with a 7 day Lease
      morpheus.core.cypher:
        state: present
        mount: secret
        name: my_secret
        value: 5uper5ecret
        ttl: 7d

    - name: Remove a UUID item
      morpheus.core.cypher:
        state: absent
        cypher_path: uuid/my_uuid




.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. tabularcolumns:: \X{1}{3}\X{2}{3}

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1
  :class: longtable ansible-option-table

  * - Key
    - Description

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-cypher"></div>

      .. _ansible_collections.morpheus.core.cypher_module__return-cypher:

      .. rst-class:: ansible-option-title

      **cypher**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-cypher" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Details of the Cypher item.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"cypher": {"created\_by": "130", "data": "rfYTVB\>1VNQpW5!%b{Sj=I60o!\`q.V%jXk/Aga^0&B\_/p/w\>Q08~\_0Pze\_fhyfQrx)", "date\_created": null, "expire\_date": null, "id": 165, "item\_key": "password/64/my\_pass", "last\_accessed": "2024-01-01T00:00:01Z", "last\_updated": "2024-01-01T00:00:01Z", "lease\_duration": null, "lease\_timeout": 0, "success": true, "type": "string"}}`


      .. raw:: html

        </div>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- James Riach (@McGlovin1337)



.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. ansible-links::

  - title: "Repository (Sources)"
    url: "https://www.github.com/gomorpheus/ansible-collection-morpheus-core"
    external: true


.. Parsing errors

