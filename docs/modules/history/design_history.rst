##############
Design History
##############


.. contents::
    :depth: 1
    :local:


---------------


04 May 2020
-----------

Establish the project objectives and requirements. The aim is create a single-page dashboard which can be used
to display COVID-19 testing data. That data will be provided by the Lacewing point of care diagnostic device
(pictured below).

The page should allow users to gain information on the spread of the virus and the extent to which testing is being
carried out. The target audience has not yet been decided upon with clinicians, governments and the general population
being possibilities.

The project should be implemented using the Django web-framework on the server side. This framework will be used
to create the database models, serve static files to clients and possibly implement web APIs or do data processing.

.. figure:: pictures/20200413_121845.jpg

   Lacewing point of care device (Centre for Bio-Inspired Technology)

.. figure:: pictures/20200419_164716.jpg

   Lacewing device with sample (Centre for Bio-Inspired Technology)


---------------


05 May 2020
-----------

The diagnostic data must be stored in a database.

Brainstorming session to determine what attributes the database schema should have and how to design it.
Two main options were considered:

* Use one table where each tuple has all the information related to the diagnostic, the patient and the testing
  location. This has the advantage of making accessing data straightforward but does have several considerable
  drawbacks. There is no separation between confidential patient data and publicly available location data. Furthermore,
  if a patient has several tests, or several tests are held at the same location, which is highly likely, there would
  be redundant information being stored in the database.

* Use three separate tables. One for patient information, one for diagnostic information and one for testing location
  related fields. There are one-to-many relationships between the ``Patient`` table and the ``Diagnostic`` table, and
  between the ``Testing_centre`` and ``Diagnostic`` tables. This resolves the issues present in the previous schema.
  Patient data is held in a separate table from all other data. The ``Diagnostic`` table has information which can
  be displayed openly as the only link to a patient is an anonymised patient ID. Having separate tables also means less
  data needs ot be stored in cases where a patient has had several diagnostics or when a testing centre is used several
  times.

.. figure:: pictures/DB_ER_diagram.png

   Database schema possibilities with advantages and drawbacks


---------------

.. _query-function:

06 May 2020
-----------

Start working on the back-end implementation. An django application named ``dashboard`` is added to the ``protondx``
project. The datatable models are created based on the three-table schema described previously.

Work starts on functions which can be used to query the database to obtain general diagnostic information such as
the total number of tests, the number of positive tests and the number of different patients tested.

An administrator interface is added for the ``dashboard`` app based upon Django's 'automatic admin interface'.


---------------


07 May 2020
-----------

An initial layout for the dashboard front-end is created (pictured below). The map is implemented using the ArcGIS
API for Javascript. Basic widgets are added for zoom, search, view reset...

The dot density renderer is considered as a possible option for representing the spread of the virus or the extent of
testing in the UK.


.. figure:: pictures/dash-1.PNG

   Initial dashboard layout


---------------


08 May 2020
-----------

Radio buttons are added to select between two renderers:

* Dot density renderer: randomly placed dots inside a geographic region based on the number of tests in that region.
* Dot renderer: individual dots for each diagnostic.

At this point, the data being plotted is not obtained from the database and is just based on pseudo-random numbers.

.. figure:: pictures/old-render-select-1.PNG

   Renderer selection (Old dashboard layout)


---------------


09 May 2020
-----------
The query functions designed on :ref:`query-function` are used to display data from the database in a popup when a
postcode sector is clicked. The postcode data is hosted by ArcGIS. On click, that postcode is sent to the server which
queries the database and returns statistics for that postcode.


---------------


10 May 2020 - 11 May 2020
-------------------------
"Add: Pointfield (for coordinates) to testing centre model
Replace dot-density renderer with heatmap, allows us to not need fixed boundaries / data for each region, we can use just coordiantes
add toggle for postcode layer: reduce data usage"


---------------


12 May 2020
-----------
"add a table along whole left side using datatables
issue : data need sto be loaded twice due to format issues
Combine testing centre model with diagnostic test to avoid serialisation issues"

.. figure:: pictures/dash-2.PNG

   Add table to initial design


---------------


13 May 2020
-----------
"Selection in table highlights diagnostic on map
fix the data laoded twice issue by using a glob to make it seem as if the laoded data was data which can be queried with a link
write custom geoJSON serializer which works with foreign keys, centre model can be added back"


---------------


14 May 2020
-----------
Add colour sensitive dot renderer (diff colour for pos and neg diagnostics)

.. figure:: pictures/dot-render-key.PNG

   Differentiate between positive and negative diagnostics


---------------


15 May 2020
-----------
Add error msg for cases when WebGL is not enabled


---------------


16 May 2020
-----------
"Edit dashboard layout
seraching for address gives overview data for closest postcode (removed later on)
search in map filters the datatable"


---------------


17 May 2020 - 18 May 2020
-------------------------
Write functions to create sample data (very basic, limited centres/patients)


---------------


19 May 2020
-----------
Start file upload app

.. figure:: pictures/upload-page-old-1.PNG

   Initial layout for file upload view


---------------


20 May 2020
-----------
Open uploaded files, try and create a form based on json content

.. figure:: pictures/upload-page-old-2.PNG

   Form created based on .json file content


---------------


21 May 2020
-----------
Add a country GeoJSON layer + get basic statistics for the country


---------------


22 May 2020
-----------
"Add charts for centre type (chart.js) and gender
consider the addition of a time slider (date format is majot obstacle)
remove datatable and have global stats instead
add a regions layer"

.. figure:: pictures/graphs.PNG

   Graphs and charts implemented using Chart.js


---------------


23 May 2020
-----------
Start transition to an imperial theme (on request from supervisor)

.. figure:: pictures/dashboard.PNG

   Revised theme on the dashboard


---------------


24 May 2020
-----------
"Datatable is added back, clicking on an entry brings up a modal (to be used for patient information)
float divs to grid"


---------------


25 May 2020
-----------
"Add: various location fileds to testing centre model (region, county, country...)
add patient info and history to modal"


---------------


26 May 2020
-----------
Refactor repo, to sperate into js, css, ... static files


---------------


27 May 2020
-----------
Form has  a defualt format and fileds are completed based on data in file


---------------


28 May 2020
-----------
"Style form
Store country data in database. use it for reverse geocoding. Use postcode API to get county and postcode"


.. figure:: pictures/old-form.PNG

   Original form

.. figure:: pictures/form-new.PNG

   Updated form styling


---------------


29 May 2020
-----------
"Imperial theme on upload page
date chart in dashboard"

.. figure:: pictures/upload-page-new.PNG

   Revised theme on upload page


---------------


30 May 2020 - 01 June 2020
--------------------------
Change all code documentation/commetns to restructured text doctrings

.. code-block:: python
    :caption: Document code using reStructuredText docstrings
    :name: docstring-comments

    def get_postcode_total_experiments(postcode):
        """
        Get the number of diagnostic tests made in a certain postcode

        :param string postcode: postcode
        :return: Number of diagnostic tests
        :rtype: int
        """
        return DiagnosticTest.objects.filter(testing_centre__postcode__startswith=postcode).count()


.. code-block:: python
    :caption: Document code using standard Python comments
    :name: standard-comments

    # Get the number of diagnostic tests made in a certain postcode
    def get_postcode_total_experiments(postcode):
        return DiagnosticTest.objects.filter(testing_centre__postcode__startswith=postcode).count()


---------------


02 June 2020
------------
Create the basic structure for documentation using Sphinx


`Sphinx <https://www.sphinx-doc.org/>`_

---------------


03 June 2020
------------
Create patient sample data, add a command to import to DB

:ref:`import-command`

---------------


04 June 2020
------------
Command to load region/country.. boundaries


---------------


05 June 2020 - 11 June 2020
---------------------------
Work on deploying to AWS and later to Heroku

:ref:`deploy-guide`

---------------


12 June 2020
------------
"Compress static files and all data over 200B transferred using GZIP
add login/logout for doctors"


---------------


13 June 2020
------------
"log user who uplaods data
integrate PCR data generation/querying into REST API"

.. figure:: pictures/log.png

   Audit log


---------------


14 June 2020 - 17 June 2020
---------------------------
Add time slider for the dot renderer (seperate branch)


---------------


18 June 2020 - 25 June 2020
---------------------------
document the project based on noted taken throughout

