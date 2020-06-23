.. _deploy-guide:

###################
Deploying to Heroku
###################

Heroku is the platform that was chosen to deploy the |project_name| application.
It's a platform than can be used to build and run applications in the cloud.


Django settings
---------------

The Django project settings are pre-configured for deployment.
They only need to be activated by setting the ``SETTINGS`` environment variable to ``DEPLOY``.
This is done in `protondx/protondx/.env`. The host name may also need to be updated by modifying
the ``WEB_HOST`` environment variable::

    WEB_HOST = protondx.herokuapp.com
    APP_NAME = protondx
    SETTINGS = DEV


The database settings will be configured automatically using the ``dj_database_url`` package.


-------------


Heroku setup
------------

Before deploying, some configuration needs to be done. The ``Runtime``, ``Requirements`` and ``Procfile``
configurations are already present in the repository but are detailed below for further information.


Runtime
~~~~~~~

The runtime to be used by Heroku must be specified in a `runtime.txt`
file placed in the root directory.
For this project the root will be `protondx/`.

The contents of the file must be as follows::

   python-3.7.7


Requirements
~~~~~~~~~~~~

A `requirements.txt` file must be placed in `protondx/`. This file should contain a list of all Python packages needed
to deploy and run the application. In an environment which has the requirements installed, the file can be
generated as follows:

.. code-block:: console

    pip3 freeze > requirements.txt


Procfile
~~~~~~~~
The `Procfile` file must be placed in `protondx/`. It is used to run commands when deploying to Heroku.

The contents of the file must be as follows::

   web: gunicorn protondx.wsgi --log-file=-

Gunicorn (Green Unicorn) is a Python webserver gateway.

Buildpacks
~~~~~~~~~~

The Heroku app needs to be configured with several buildpacks in order to be deployed properly.

1. https://github.com/timanovsky/subdir-heroku-buildpack
    The project to be deployed is in `protondx/` which is not the root of the repository. To make `protondx/`
    the root when deploying this buildpack must be added. The ``PROJECT_PATH`` variable must be set to
    point to `protondx/`
2. https://github.com/heroku/heroku-geo-buildpack
    ``heroku-geo-buildpack`` is used to install all the required spatial libraries when deploying.
    It installs:

    * GEOS
    * GDAL
    * PROJ
3. heroku/python
    This buildpack is needed when deploying a python application on Heroku.


Complete configuration for buildpacks:

.. code-block:: console

    heroku buildpacks:clear
    heroku buildpacks:set https://github.com/timanovsky/subdir-heroku-buildpack
    heroku buildpacks:add https://github.com/heroku/heroku-geo-buildpack
    heroku buildpacks:add heroku/python
    heroku config:set PROJECT_PATH=protondx/


-------------


Database
--------

When following the above steps a free Postgres database, configured with PostGIS will be used.
If another database is to be used, it can be configured in the Heroku dashboard online.

For speed and efficiency static files should be stored separately from the server (e.g. Using Amazon S3).
Whatever platform is used for static files should also be used for storing uploaded files as these will not
be stored on Heroku's ephemeral filesystem.
This will need to be configured following Heroku documentation.
