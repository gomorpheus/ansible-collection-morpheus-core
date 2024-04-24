
.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.9.0

.. Anchors

.. _ansible_collections.morpheus.core.tenant_info_module:

.. Anchors: short name for ansible.builtin

.. Title

morpheus.core.tenant_info module -- Retrieves Tenant Info
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.1).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

    To use it in a playbook, specify: :code:`morpheus.core.tenant_info`.

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

- Returns information about Morpheus Tenants.


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
        <div class="ansibleOptionAnchor" id="parameter-account_name"></div>

      .. _ansible_collections.morpheus.core.tenant_info_module__parameter-account_name:

      .. rst-class:: ansible-option-title

      **account_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-account_name" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Filter tenants by account name.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-account_number"></div>

      .. _ansible_collections.morpheus.core.tenant_info_module__parameter-account_number:

      .. rst-class:: ansible-option-title

      **account_number**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-account_number" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Filter tenants by account number.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-customer_number"></div>

      .. _ansible_collections.morpheus.core.tenant_info_module__parameter-customer_number:

      .. rst-class:: ansible-option-title

      **customer_number**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-customer_number" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Filter tenants by customer number.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id"></div>

      .. _ansible_collections.morpheus.core.tenant_info_module__parameter-id:

      .. rst-class:: ansible-option-title

      **id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-id" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Return specific object by id.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-name"></div>

      .. _ansible_collections.morpheus.core.tenant_info_module__parameter-name:

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

      Filter by name.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-regex_name"></div>

      .. _ansible_collections.morpheus.core.tenant_info_module__parameter-regex_name:

      .. rst-class:: ansible-option-title

      **regex_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-regex_name" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Treat the name parameter as a regular expression.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


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

      .. _ansible_collections.morpheus.core.tenant_info_module__attribute-check_mode:

      .. rst-class:: ansible-option-title

      **check_mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#attribute-check_mode" title="Permalink to this attribute"></a>

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      :ansible-attribute-support-label:`Support: \ `      \ :ansible-attribute-support-na:`N/A`

      Not Required, Module does not make changes.


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

      .. _ansible_collections.morpheus.core.tenant_info_module__attribute-diff_mode:

      .. rst-class:: ansible-option-title

      **diff_mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#attribute-diff_mode" title="Permalink to this attribute"></a>

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      :ansible-attribute-support-label:`Support: \ `      \ :ansible-attribute-support-na:`N/A`


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

      .. _ansible_collections.morpheus.core.tenant_info_module__attribute-platform:

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
        <div class="ansibleOptionAnchor" id="return-tenants"></div>

      .. _ansible_collections.morpheus.core.tenant_info_module__return-tenants:

      .. rst-class:: ansible-option-title

      **tenants**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-tenants" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of matching tenants.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"tenants": [{"account\_name": null, "account\_number": null, "active": true, "currency": "GBP", "customer\_number": "T3ST", "date\_created": "2022-01-01T0:00:01Z", "description": null, "external\_id": null, "id": 10, "last\_updated": "2022-01-01T0:00:01Z", "master": true, "name": "TestTenant", "role": {"authority": "Tenant Base Role", "description": null, "id": 5, "name": "Tenant Base Role"}, "stats": {"instance\_count": 5, "user\_count": 10}, "subdomain": "test"}]}`


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

