############
Requirements
############

Python
------

**Python 3.7** is required.

The Python packages below are to be installed on the virtual environment or
machine running the server.

Install using:

.. code-block:: console

   $ pip install -r requirements.txt   # Install requirements


or see :ref:`install-guide` for a complete guide.


Packages
~~~~~~~~

.. include:: ../../../requirements.txt
   :literal:


Database
--------

Postgres
~~~~~~~~

A spatial database is needed to support the storage of coordinates and polygons.
Postgres using PostGIS is the recommended method and is what is used during deployment.


Spatialite
~~~~~~~~~~

Spatialite is a suitable alternative to Postgres during development. (:ref:`install-spatial-db`)


It should **not** be used for deployment on Heroku. It will not obey the durability characteristic of the ACID
properties. SQLite databases are stored on disk, in the same directory as the source code. Heroku Dynos use an
ephemeral filesystem meaning all uploaded files and data will be **deleted** when the Dyno is shut down.
