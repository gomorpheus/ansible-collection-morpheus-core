
.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.9.0

.. Anchors

.. _ansible_collections.morpheus.core.tenant_module:

.. Anchors: short name for ansible.builtin

.. Title

morpheus.core.tenant module -- Manage Tenants
+++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.1).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

    To use it in a playbook, specify: :code:`morpheus.core.tenant`.

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

- Create, Update and Remove Tenants.


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

      .. _ansible_collections.morpheus.core.tenant_module__parameter-account_name:

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

      Additional Tenant Identifier.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-account_number"></div>

      .. _ansible_collections.morpheus.core.tenant_module__parameter-account_number:

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

      Additional Tenant Identifier.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-currency"></div>

      .. _ansible_collections.morpheus.core.tenant_module__parameter-currency:

      .. rst-class:: ansible-option-title

      **currency**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-currency" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      ISO Currency Code.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"AUD"`
      - :ansible-option-choices-entry:`"BGN"`
      - :ansible-option-choices-entry:`"BRL"`
      - :ansible-option-choices-entry:`"CAD"`
      - :ansible-option-choices-entry:`"CHF"`
      - :ansible-option-choices-entry:`"CLF"`
      - :ansible-option-choices-entry:`"CLP"`
      - :ansible-option-choices-entry:`"CNY"`
      - :ansible-option-choices-entry:`"CZK"`
      - :ansible-option-choices-entry:`"DKK"`
      - :ansible-option-choices-entry:`"EUR"`
      - :ansible-option-choices-entry:`"GBP"`
      - :ansible-option-choices-entry:`"HKD"`
      - :ansible-option-choices-entry:`"HRK"`
      - :ansible-option-choices-entry:`"HUF"`
      - :ansible-option-choices-entry:`"IDR"`
      - :ansible-option-choices-entry:`"ILS"`
      - :ansible-option-choices-entry:`"INR"`
      - :ansible-option-choices-entry:`"JPY"`
      - :ansible-option-choices-entry:`"KRW"`
      - :ansible-option-choices-entry:`"MXN"`
      - :ansible-option-choices-entry:`"MYR"`
      - :ansible-option-choices-entry:`"NOK"`
      - :ansible-option-choices-entry:`"NZD"`
      - :ansible-option-choices-entry:`"PHP"`
      - :ansible-option-choices-entry:`"PLN"`
      - :ansible-option-choices-entry:`"RON"`
      - :ansible-option-choices-entry:`"RUB"`
      - :ansible-option-choices-entry:`"SEK"`
      - :ansible-option-choices-entry:`"SGD"`
      - :ansible-option-choices-entry:`"THB"`
      - :ansible-option-choices-entry:`"TRY"`
      - :ansible-option-choices-entry:`"USD"`
      - :ansible-option-choices-entry:`"ZAR"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-customer_number"></div>

      .. _ansible_collections.morpheus.core.tenant_module__parameter-customer_number:

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

      Additional Tenant Identifier.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-description"></div>

      .. _ansible_collections.morpheus.core.tenant_module__parameter-description:

      .. rst-class:: ansible-option-title

      **description**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-description" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Description for the Tenant.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id"></div>

      .. _ansible_collections.morpheus.core.tenant_module__parameter-id:

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

      The Id of an existing Tenant.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-name"></div>

      .. _ansible_collections.morpheus.core.tenant_module__parameter-name:

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

      The name of the Tenant.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-role"></div>

      .. _ansible_collections.morpheus.core.tenant_module__parameter-role:

      .. rst-class:: ansible-option-title

      **role**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-role" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Id of a Role to act as the Tenant base role.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.morpheus.core.tenant_module__parameter-state:

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

      The state of the Tenant.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"absent"`
      - :ansible-option-choices-entry-default:`"present"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-subdomain"></div>

      .. _ansible_collections.morpheus.core.tenant_module__parameter-subdomain:

      .. rst-class:: ansible-option-title

      **subdomain**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-subdomain" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Subdomain name used in login URL and subtenant users.


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

      .. _ansible_collections.morpheus.core.tenant_module__attribute-check_mode:

      .. rst-class:: ansible-option-title

      **check_mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#attribute-check_mode" title="Permalink to this attribute"></a>

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      :ansible-attribute-support-label:`Support: \ `\ :ansible-attribute-support-full:`full`


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

      .. _ansible_collections.morpheus.core.tenant_module__attribute-diff_mode:

      .. rst-class:: ansible-option-title

      **diff_mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#attribute-diff_mode" title="Permalink to this attribute"></a>

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      :ansible-attribute-support-label:`Support: \ `\ :ansible-attribute-support-full:`full`


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

      .. _ansible_collections.morpheus.core.tenant_module__attribute-platform:

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
        <div class="ansibleOptionAnchor" id="return-tenant"></div>

      .. _ansible_collections.morpheus.core.tenant_module__return-tenant:

      .. rst-class:: ansible-option-title

      **tenant**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-tenant" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Details of the Tenant state.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"tenant": {"account\_name": null, "account\_number": null, "active": true, "currency": "GBP", "customer\_number": null, "date\_created": "2024-01-01T00:00:01Z", "description": "Testing Tenant", "external\_id": null, "id": 30, "last\_updated": "2024-01-01T00:00:01Z", "master": false, "name": "Test Tenant", "role": {"authority": "Customer Base Role", "description": null, "id": 4, "name": "Customer Base Role"}, "stats": {"instance\_count": 0, "user\_count": 0}, "subdomain": "test"}}`


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

