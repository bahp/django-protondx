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

Run the server locally

.. code-block:: console

    $ python manage.py runserver

Go to the browser and access the admin localhost:8000/admin

For more information read the django docs
