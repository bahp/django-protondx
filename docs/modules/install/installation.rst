.. _install-guide:

############
Installation
############

Environment
-----------

First, ensure that you have python installed

.. code-block:: console

   $ which python  # python 2
   $ which python3 # python 3


Then, lets create a virtual environment for our project (e.g. virtualenv)

.. code-block:: console

   $ virtualenv -p <python3-path> <virtualenv-name>  # Create the environment
   $ source <virtualenv-name>/bin/activate           # Activate virtual enviroment

Then, go to the corresponding folder and install the requirements

.. code-block:: console

   $ pip install -r requirements.txt   # Install requirements


.. _install-spatial-db:

Spatial database (Linux)
------------------------

Install Spatialite

.. code-block:: console

    $ sudo apt install libsqlite3-mod-spatialite

Install geospatial libraries

.. code-block:: console

    $ sudo apt install binutils libproj-dev gdal-bin

If getting issues when migrating clear dashboard/migrations directory and then

.. code-block:: console

    $ python manage.py flush
    $ python manage.py makemigrations
    $ python manage.py migrate
