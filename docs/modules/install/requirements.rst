############
Requirements
############

Refer to :ref:`install-guide` for a detailed install guide or
:ref:`deploy-guide` for information on deploying |project_name|.


-------------


Python
------

**Python 3.7** is required.

The Python packages below are to be installed on the virtual environment or
machine running the server.

Install using:

.. code-block:: console

   $ pip install -r requirements.txt   # Install requirements


or see :ref:`install-guide` for a complete guide.

.. _python-packages-list:

Packages
~~~~~~~~

.. include:: ../../../requirements.txt
   :literal:


-------------


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


-------------


.. _requirements-browser:

Browser
-------

A browser is needed to access the |project_name| dashboard along with it's associated pages.
This is the case both when in development and when the project has been deployed.
The browser must support WebGL.

Full Support
~~~~~~~~~~~~

* Google Chrome
* Brave
* Other Chromium browsers
* Firefox


Limited Support
~~~~~~~~~~~~~~~

* Edge

    + Logo is not resized correctly
    + Data uploading is not operational

* Safari

    + Logo is not resized correctly
    + Data uploading is not operational


Not supported
~~~~~~~~~~~~~

* Internet explorer