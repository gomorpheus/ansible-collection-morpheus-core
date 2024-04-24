

.. meta::
  :antsibull-docs: 2.9.0


.. _plugins_in_morpheus.core:

Morpheus.Core
=============

Collection version 0.7.1

.. contents::
   :local:
   :depth: 1

Description
-----------

Ansible collection for interacting with Morpheus

**Authors:**

* Nick Celebic (https://www.github.com/tryfan)
* James Riach (https://github.com/McGlovin1337)

**Supported ansible-core versions:**

* 2.9 or newer

.. ansible-links::

  - title: "Repository (Sources)"
    url: "https://www.github.com/gomorpheus/ansible-collection-morpheus-core"
    external: true




.. toctree::
    :maxdepth: 1


Plugin Index
------------

These are the plugins in the morpheus.core collection:


Modules
~~~~~~~

* :ansplugin:`appliance_facts module <morpheus.core.appliance_facts#module>` -- Gather Morpheus Appliance Facts
* :ansplugin:`appliance_maintenance_mode module <morpheus.core.appliance_maintenance_mode#module>` -- Toggle Maintenance Mode of the target Morpheus Appliance
* :ansplugin:`appliance_settings module <morpheus.core.appliance_settings#module>` -- Configure Morpheus Appliance Settings
* :ansplugin:`azure_cloud module <morpheus.core.azure_cloud#module>` -- Manage an Azure Cloud
* :ansplugin:`cloud_datastore module <morpheus.core.cloud_datastore#module>` -- Configure Cloud Datastores
* :ansplugin:`cloud_datastore_info module <morpheus.core.cloud_datastore_info#module>` -- Datastore information for a specified cloud
* :ansplugin:`cloud_info module <morpheus.core.cloud_info#module>` -- Retrieves Cloud Info
* :ansplugin:`cloud_type_info module <morpheus.core.cloud_type_info#module>` -- Return available Cloud types
* :ansplugin:`cypher module <morpheus.core.cypher#module>` -- Manage items stored in Cypher
* :ansplugin:`cypher_info module <morpheus.core.cypher_info#module>` -- Return Cypher Information
* :ansplugin:`group module <morpheus.core.group#module>` -- Manage Groups
* :ansplugin:`group_info module <morpheus.core.group_info#module>` -- Retrieves Group Info
* :ansplugin:`instance module <morpheus.core.instance#module>` -- Basic Management of Morpheus Instances
* :ansplugin:`instance_info module <morpheus.core.instance_info#module>` -- Gather information about instances
* :ansplugin:`instance_snapshot module <morpheus.core.instance_snapshot#module>` -- Manage Instance Snapshots
* :ansplugin:`instance_snapshot_info module <morpheus.core.instance_snapshot_info#module>` -- Gather Snapshot information for instances
* :ansplugin:`integration_info module <morpheus.core.integration_info#module>` -- Retrieves Integration Info
* :ansplugin:`key_pair module <morpheus.core.key_pair#module>` -- Create and Remove Key Pairs
* :ansplugin:`key_pair_info module <morpheus.core.key_pair_info#module>` -- Gather Key Pair Information
* :ansplugin:`role_info module <morpheus.core.role_info#module>` -- Retrieves Role Information
* :ansplugin:`ssl_certificate module <morpheus.core.ssl_certificate#module>` -- Manage SSL Certificates
* :ansplugin:`ssl_certificate_info module <morpheus.core.ssl_certificate_info#module>` -- Gather information about SSL Certificates
* :ansplugin:`standard_cloud module <morpheus.core.standard_cloud#module>` -- Manage a Standard Morpheus Cloud
* :ansplugin:`tenant module <morpheus.core.tenant#module>` -- Manage Tenants
* :ansplugin:`tenant_info module <morpheus.core.tenant_info#module>` -- Retrieves Tenant Info
* :ansplugin:`vcenter_cloud module <morpheus.core.vcenter_cloud#module>` -- Manage a VMware VCenter Cloud
* :ansplugin:`virtual_image module <morpheus.core.virtual_image#module>` -- Manage Morpheus Virtual Images
* :ansplugin:`virtual_image_info module <morpheus.core.virtual_image_info#module>` -- Gather Virtual Image information

.. toctree::
    :maxdepth: 1
    :hidden:

    appliance_facts_module
    appliance_maintenance_mode_module
    appliance_settings_module
    azure_cloud_module
    cloud_datastore_module
    cloud_datastore_info_module
    cloud_info_module
    cloud_type_info_module
    cypher_module
    cypher_info_module
    group_module
    group_info_module
    instance_module
    instance_info_module
    instance_snapshot_module
    instance_snapshot_info_module
    integration_info_module
    key_pair_module
    key_pair_info_module
    role_info_module
    ssl_certificate_module
    ssl_certificate_info_module
    standard_cloud_module
    tenant_module
    tenant_info_module
    vcenter_cloud_module
    virtual_image_module
    virtual_image_info_module


Httpapi Plugins
~~~~~~~~~~~~~~~

* :ansplugin:`morpheus httpapi <morpheus.core.morpheus#httpapi>` -- Httpapi Plugin for Morpheus

.. toctree::
    :maxdepth: 1
    :hidden:

    morpheus_httpapi


Inventory Plugins
~~~~~~~~~~~~~~~~~

* :ansplugin:`morpheus_inventory inventory <morpheus.core.morpheus_inventory#inventory>` -- Returns Ansible inventory from Morpheus

.. toctree::
    :maxdepth: 1
    :hidden:

    morpheus_inventory_inventory


