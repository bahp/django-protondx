#####
Usage
#####

Remember to do the migrations when altering the database

.. code-block:: console

    $ python manage.py makemigrations <appname>
    $ python manage.py migrate

If it is the first time, create a superuser (user:cbit, pass:toor)

.. code-block:: console

    $ cd protondx
    $ python manage.py createsu

Development
-----------

Run the server locally

.. code-block:: console

    $ python manage.py runserver

Access the dashboard and relevant pages at:

* localhost:8000/dashboard  or  localhost:8000
* localhost:8000/dataUpload
* localhost:8000/admin

Production
----------

Access the dashboard and relevant pages at:

* <hostname>/dashboard  or  <hostname>
* <hostname>/dataUpload
* <hostname>/admin
