
.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.9.0

.. Anchors

.. _ansible_collections.morpheus.core.instance_info_module:

.. Anchors: short name for ansible.builtin

.. Title

morpheus.core.instance_info module -- Gather information about instances
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `morpheus.core collection <https://galaxy.ansible.com/ui/repo/published/morpheus/core/>`_ (version 0.7.1).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install morpheus.core`.

    To use it in a playbook, specify: :code:`morpheus.core.instance_info`.

.. version_added

.. rst-class:: ansible-version-added

New in morpheus.core 0.4.0

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Gathers information about Morpheus instances


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
        <div class="ansibleOptionAnchor" id="parameter-agent_installed"></div>

      .. _ansible_collections.morpheus.core.instance_info_module__parameter-agent_installed:

      .. rst-class:: ansible-option-title

      **agent_installed**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-agent_installed" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Filter by if agent is installed or not.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-deleted"></div>

      .. _ansible_collections.morpheus.core.instance_info_module__parameter-deleted:

      .. rst-class:: ansible-option-title

      **deleted**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-deleted" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Include, Exclude or Only show deleted instances or those pending removal.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"exclude"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"include"`
      - :ansible-option-choices-entry:`"only"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-detail"></div>

      .. _ansible_collections.morpheus.core.instance_info_module__parameter-detail:

      .. rst-class:: ansible-option-title

      **detail**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-detail" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Specify the level of detail returned for matching instances.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"minimal"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"full"`
      - :ansible-option-choices-entry:`"extra"`
      - :ansible-option-choices-entry:`"summary"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-environment"></div>

      .. _ansible_collections.morpheus.core.instance_info_module__parameter-environment:

      .. rst-class:: ansible-option-title

      **environment**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-environment" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Filter instances by environment.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-id"></div>

      .. _ansible_collections.morpheus.core.instance_info_module__parameter-id:

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

      Specify the id of an instance.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-instance_type"></div>

      .. _ansible_collections.morpheus.core.instance_info_module__parameter-instance_type:

      .. rst-class:: ansible-option-title

      **instance_type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-instance_type" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Filter by the instance type code.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-labels"></div>

      .. _ansible_collections.morpheus.core.instance_info_module__parameter-labels:

      .. rst-class:: ansible-option-title

      **labels**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-labels" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Filter instances by matching labels.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-match_all_labels"></div>

      .. _ansible_collections.morpheus.core.instance_info_module__parameter-match_all_labels:

      .. rst-class:: ansible-option-title

      **match_all_labels**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-match_all_labels" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If labels have been specified, filter instances by those that match all specified labels.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-name"></div>

      .. _ansible_collections.morpheus.core.instance_info_module__parameter-name:

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

      Filter instances by name.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-regex_name"></div>

      .. _ansible_collections.morpheus.core.instance_info_module__parameter-regex_name:

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

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-status"></div>

      .. _ansible_collections.morpheus.core.instance_info_module__parameter-status:

      .. rst-class:: ansible-option-title

      **status**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-status" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Filter by instance status, e.g. running


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-tags"></div>

      .. _ansible_collections.morpheus.core.instance_info_module__parameter-tags:

      .. rst-class:: ansible-option-title

      **tags**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-tags" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Filter instances by matching tags.


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

      .. _ansible_collections.morpheus.core.instance_info_module__attribute-check_mode:

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

      .. _ansible_collections.morpheus.core.instance_info_module__attribute-diff_mode:

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

      .. _ansible_collections.morpheus.core.instance_info_module__attribute-platform:

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
        <div class="ansibleOptionAnchor" id="return-morpheus_instances"></div>

      .. _ansible_collections.morpheus.core.instance_info_module__return-morpheus_instances:

      .. rst-class:: ansible-option-title

      **morpheus_instances**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-morpheus_instances" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of instances with info


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"morpheus\_instances": [{"cloud": {"id": 31, "name": "VMWare Cloud", "type": "vmware"}, "connection\_info": [{"ip": "192.168.0.10", "name": null, "port": null}], "date\_created": "2023-06-01T13:37:00Z", "description": "Webserver Instance", "id": 100, "instance\_type": {"code": "win2019", "id": 110, "name": "Windows Server 2019"}, "instance\_version": "2019", "interfaces": [{"id": "network-100", "ip\_address": null, "ip\_mode": null, "network": {"dhcp\_server": false, "group": null, "id": 150, "name": "inside-network-001", "pool": {"id": 30, "name": "inside-network-pool-001"}, "subnet": null}, "network\_interface\_type\_id": null}], "labels": ["production", "webservers"], "name": "WebServ001", "owner": {"username": "patrick.clifton@domain.tld"}, "plan": {"name": "Cheap Plan 001"}, "stats": {"cpu\_usage": 0, "cpu\_usage\_avg": 0, "cpu\_usage\_peak": 0.0, "max\_memory": 4293943296, "max\_storage": 53687091200, "used\_cpu": 0.0, "used\_memory": 2080228608, "used\_storage": 25341928960}, "status": "running", "volumes": [{"name": "root", "resizeable": true, "root\_volume": true, "size": 50}]}]}`


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

