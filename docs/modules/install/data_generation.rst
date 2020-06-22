########
Commands
########


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


Generate location data (Centre dataset)
---------------------------------------

Overview
~~~~~~~~


Usage
~~~~~


Code
~~~~

.. automodule:: dashboard.management.commands.fill_location
    :members:


Generate pseudorandom locations
-------------------------------

Overview
~~~~~~~~


Usage
~~~~~


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
