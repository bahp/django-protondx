###################
|project_name| Code
###################

|project_name| is implemented using Python and the Django web framework. The project is located in the `protondx/`
directory of the repository and has the following structure:

.. include:: code_docs/tree.txt
   :literal:

* ``authentication``: Contains the HTML templates used during user authentication.

* ``dashboard``: Contains the ``dashboard`` application. This application is responsible for everything
  related to the |project_name| dashboard which displays diagnostic information on a map along with graphs and
  tabular data.

* ``dataUpload``: Contains the ``dataUpload`` application. This application is used by users when
  they want to upload diagnostic information to the database.

* ``diagnostics``: Contains the ``diagnostics`` application. This application was created by the
  Centre for Bio-Inspired Technology.

* ``protondx``: Contains the settings and configuration options for thw Django project.

* ``static``: Static files are placed in this directory when |project_name| is deployed.

* `` uploads``: Uploaded files are placed in this directory when the server is run locally. When the project is
  deployed they cannot be stored in this directory due to Heroku's ephemeral file system.

.. toctree::
    :maxdepth: 2
    :caption: Contents:
    :glob:

    code_docs/*
