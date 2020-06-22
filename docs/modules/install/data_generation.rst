########
Commands
########

.. contents::
    :local:

Import Data
-----------

Overview
~~~~~~~~
This command is used to import sample data into the database. It can be used to import ``Patient``,
``Testing Centre`` or ``Diagnostic test`` data.

Usage
~~~~~
What data needs to be imported is specified with a flag:

* Patient
    - :kbd:`--patient`
    - :kbd:`-p`

* Testing Centre
    - :kbd:`--centre`
    - :kbd:`-c`

* Diagnostic test
    - :kbd:`--diagnostic`
    - :kbd:`-d`


The commands can be used as follows:

.. code-block:: console

    python manage.py import --patient
    python manage.py import --centre

Shorthand:

.. code-block:: console

    python manage.py import -p
    python manage.py import -c


For the ``Diagnostic test`` data, the user can optionally specify the number of entries to be created
using the ``--entries`` flag.
The default is 1000.

The commands can be used as follows:

.. code-block:: console

    python manage.py import --diagnostic

    python manage.py import --diagnostic --entries <int>

Shorthand:

.. code-block:: console

    python manage.py import -d

    python manage.py import -d --entries <int>

Sample data is provided but if a user wants to specify their own, they will need to provide the
path to the dataset which must be in a ``csv`` file.

.. code-block:: console

    python manage.py import <import-flag> --path </path/to/file>



Code
~~~~

.. automodule:: dashboard.management.commands.import
    :members:


.. _gen-location-command:

Generate location data
----------------------

Overview
~~~~~~~~
This command is used to add location information to a ``Testing Centre`` dataset.

The provided dataset must be in ``csv`` format and contain the ``center_type`` for each row.

.. csv-table:: Dataset before generating locations
   :file: centre_mock_empty.csv
   :header-rows: 1


The resulting dataset will have location information added.

.. csv-table:: Dataset after generating locations
   :file: centre_mock_full.csv
   :header-rows: 1


Usage
~~~~~

When using the command to fill location information, the path to the dataset must be specified using the ``--path`` flag.

.. code-block:: console

    manage.py fill_location –-path <path/to/file>

Code
~~~~

.. automodule:: dashboard.management.commands.fill_location
    :members:


Generate pseudorandom locations
-------------------------------

Overview
~~~~~~~~
This module is used by the :ref:`gen-location-command` command to generate random coordinates and obtain the
corresponding country, region and county information.

Code
~~~~

.. automodule:: dashboard.fixtures.gen_location
    :members:


Load borders
------------

Overview
~~~~~~~~
This command is used to import geographical data into the database.
It loads country borders as well as region and county borders for the UK.

Usage
~~~~~

All thee border types can be loaded at once or separately by using the designated flags:

    * :kbd:`--country`
    * :kbd:`--region`
    * :kbd:`--county`


.. code-block:: console

    manage.py load_borders [--country] [--region] [--county]

Code
~~~~

.. automodule:: dataUpload.management.commands.load_borders
    :members:
