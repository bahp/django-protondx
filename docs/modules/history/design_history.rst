##############
Design History
##############


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
  data needs to be stored in cases where a patient has had several diagnostics or when a testing centre is used several
  times.

.. figure:: pictures/DB_ER_diagram.png

   Database schema possibilities with advantages and drawbacks


---------------

.. _query-function:

06 May 2020
-----------

Start working on the back-end implementation. A django application named ``dashboard`` is added to the ``protondx``
project. The database models are created based on the three-table schema described previously.

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

A REST API was created to make these queries possible. All information from this point onwards which comes from the
server is accessed using this REST API and extensions made to it.


---------------


10 May 2020 - 11 May 2020
-------------------------

Edit the database schema to store coordinates as a point and not separate longitude and latitude.


For example:

.. code-block::

    SRID=4326;POINT(-123.365556 48.428611)

as opposed to:

.. code-block::

    longitude = -123.365556
    latitude = 48.428611


Storing the coordinates in this manner allows us to keep track of what spatial reference system is being used and
to use the data directly with geo-spatial libraries.

The dot density renderer is replaced by a heatmap. This allows us to only need coordinates when plotting data. We don't
need to query the database separately for the data displayed by the dot renderer and the heatmaps.
The dot density renderer needed the database to be queried for each geographical region displayed on the map.

A toggle option is added which allows users to not display postcode boundaries. This allows a user to reduce the
amount of data loaded when the page is accessed. It also reduces the computational load on the client machine.


---------------

.. _12-05-2020:

12 May 2020
-----------

The dashboard layout is changed to include a table on the right side. The idea is to display information in a way where
it can easily be sorted or aggregated.

**Issue:** The data loaded in the map and table do not use the same format. All the data therefore needs to be
loaded twice using different formats. This impacts loading speeds and data usage for the client. It also affects the
server as the data needs to be serialised twice. **Unresolved**

**Issue:** Unable to serialise data in tables linked by a foreign key when the table contains geographical data such as
points (used for coordinates) and polygons.

**Temporary solution:** Combine ``testing_centre`` model with ``diagnostic_test`` model to avoid serialisation issues.

.. figure:: pictures/dash-2.PNG

   Add table to initial design


---------------


13 May 2020
-----------
Add a feature where selecting data in the table highlights it on the map and zooms onto that point.

**Fix:** Issue where data is loaded twice is resolved by using a `Javascript blob <https://javascript.info/blob>`_ and
serialising data into GeoJSON which can be used for both the table and map.

**Fix:** The temporary solution described on :ref:`12-05-2020` is replaced by a more definitive one. The
``testing_centre`` and ``diagnostic_test`` models are separated again. A custom GeoJSON serialiser is written to
serialise data into a GeoJSON format, even when there are some columns linked to by a foreign key.


---------------


14 May 2020
-----------
The dot renderer now displays positive and negative diagnostics using different colours:

* Green: Negative - patient does not have the virus
* Red: Positive - patient has the virus
* Orange: Data not available or inconclusive

.. figure:: pictures/dot-render-key.PNG

   Differentiate between positive and negative diagnostics


---------------


15 May 2020
-----------
An error message is added for cases when the dashboard is accessed from a web-browser which does not have support for
WebGL. WebGL is a JavaScript API which is used by ArcGIS to render the map.


---------------


16 May 2020
-----------
The dashboard layout is edited for the map to take up the full height of the screen on the left side.
The radio buttons and other features which were displayed on the bottom-left are now displayed in collapsible menus,
directly on the map.

Searching for an address or location now shows general statistics for the nearest postcode sector (number of tests,
number of cases, number of patients...). This search also filters the data in the table.

**Issue:** This search works at anything lower thant postcode level but is an issue when a user searches for a country,
for example. The postcode closest to the centroid of the country will be selected which is not desired.

**Solution (implemented later on):** Drop a pin on the map at the desired location. The user can then select the
location manually. If the user is zoomed out, the country layer will be selected, when further in then the region layer
is selected and if even further in, the postcode layer.


---------------


17 May 2020 - 18 May 2020
-------------------------
Functions are written to create sample data. They can be used to create any number of diagnostic test objects but there
are a limited number of different patient and testing centre objects which can be created.

A wider range of sample data is created on :ref:`03-06-2020`.


---------------


19 May 2020
-----------
Based on meetings with the team, the decision is made to add another page to the website. The aim is to have a page
where data can easily be uploaded.

The requirements as described by the team are:

* Drag and drop interface
* Extract .zip archives and display data
* Data needs to be visible to the uploader and it must be able to be be edited
* On upload data gets added to the database

The initial design is pictured below. The page is composed of an upload area (top left), data can either be dragged
into that area or selected using the client computers file explorer.
An list area which displays all the files which have been selected (bottom left). It also acts as a way to select which
file is to be displayed.
A display area (right) which shows the contents of the zip archive.


.. figure:: pictures/upload-page-old-1.PNG

   Initial layout for file upload view


---------------


20 May 2020
-----------
Files uploaded through the upload page are opened. A basic form is created for each archive which contains a .json file.
There is a form entry for each key in the JSON object.

.. figure:: pictures/upload-page-old-2.PNG

   Form created based on .json file content


---------------


21 May 2020
-----------
A new layer is added to the map. The layer shows country borders and is only visible when the user is zoomed out.
Upon selection of a country, the database is queried for statistics. This requires the country to be stored in the
database along with the coordinates.


---------------


22 May 2020
-----------

Charts have been added to the ``div`` on the right side. They show testing centre types and gender distributions for the
selected regions. These statistics are calculated on the client side. The ``Multi-Polygon`` data stored in the GeoJSON
layers is used along with the diagnostic coordinates to determine these statistics and demographics.

.. figure:: pictures/graphs.PNG

   Graphs and charts implemented using Chart.js

The table on the right was removed to make space for the graphs. Global statistics are shown in the bottom right.

A new layer is added to the map. The layer shows UK region borders and is visible when the user is zoomed in further
than where the country boundaries are visible, and less than where the postcode boundaries are visible.
Upon selection of a region, the database is queried for statistics. This **does not** require the region to be stored in
the database thanks to the changes made when adding the charts. Countries and postcodes no longer need to be stored as
all statistics are created on the client side, based solely on region boundaries and diagnostic test coordinates.

The addition of a time slider was considered. It would allow users to show diagnostics over a variable time period.
This was deemed to have too many downsides so was not implemented:

* Increased loading times
* More processing needed on both client and server sides
* Not possible with the heatmap, only the dot renderer


---------------


23 May 2020
-----------
Start the transition towards an Imperial College London theme on request from our supervisor.

.. figure:: pictures/dashboard.PNG

   Revised theme on the dashboard


---------------


24 May 2020
-----------

Decision is made to support more patient specific information.

The table on the side is added back, underneath the graphs. It allows for data to be aggregated and filtered.
Clicking on a table entry brings up a modal which will be used ot bring up more information specific to a patient.

The dashboard which was using floating divs for its layout is changed to a css grid.


---------------


25 May 2020
-----------

Country, region, county and postcode fields are added to the ``Testing_centre`` model. These were removed earlier on
as they were no longer needed to obtain statistics. They were added back to support searching by these geographical
areas in the table. They have to be entered manually at upload time.

General patient information (name, date of birth, age, gender...) is now in the detailed analysis page. A table with
all of the patient's diagnostic tests was also added.


---------------


26 May 2020
-----------

The github repository was refactored. Where possible, Javascript and Cascading Style Sheets were removed from
Hypertext Markup Language templates and put into separate JS and CSS files. These files are stored under their
own directory for each app.

.. include:: tree.txt
    :literal:


---------------

.. _27-05-2020:

27 May 2020
-----------

The dataUpload page now has a fixed form which is created for each uploaded archive. The form fields are filled if the
archive contains a JSON file with the required key.

.. figure:: pictures/old-form.PNG

   Auto-filled form

---------------


28 May 2020
-----------

The form created on :ref:`27-05-2020` is styled to fill the display area.

Boundary data is stored in the database. New models are created to store a name along with a
multi-polygon. Reverse geo-coding is used at upload time to obtain geographical information (country, region, county,
postcode). Reverse geo-coding is done using locally stored data
(:ref:`geographical-data`) for the country, region and county, and using `Postcodes.io <http://api.postcodes.io/>`_
for the postcodes.

The above means only coordinates need to be present at upload time. The rest will be filled automatically on the server.

.. figure:: pictures/form-new.PNG

   Updated form styling


---------------


29 May 2020
-----------

The styling of the upload page is changed to be more 'Imperial College oriented'.

.. figure:: pictures/upload-page-new.PNG

   Revised theme on upload page


A chart is added to the dashboard. It shows the number of diagnostics and number of positive tests for the full
available time period.


---------------


30 May 2020 - 01 June 2020
--------------------------

To facilitate writing documentation later on, the comments throughout the code are changed from standard Python comments
to reStructuredText docstrings. An example of the change is given below:

.. code-block:: python
    :caption: Document code using standard Python comments
    :name: standard-comments

    # Get the number of diagnostic tests made in a certain postcode
    def get_postcode_total_experiments(postcode):
        return DiagnosticTest.objects.filter(testing_centre__postcode__startswith=postcode).count()


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


---------------


02 June 2020
------------

The basic structure for the documentation is created using `Sphinx <https://www.sphinx-doc.org/>`_.

`Autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_ is used to take the docstrings in the
code and generate documentation of out them.

---------------

.. _03-06-2020:

03 June 2020
------------

Sample data is generated for patients (3000 entries). Commands are created to make that data easy to import into the
database when deploying the project or running it locally.

:ref:`import-command`

---------------


04 June 2020
------------

Commands are added to load geographical boundaries into the database.

:ref:`import-borders-command`

Sample data is generated for testing centres (3000 entries). Commands are created to make that data easy to import into
the database when deploying the project or running it locally. A command is also added to create ``diagnostic_test``
objects.


---------------


05 June 2020 - 11 June 2020
---------------------------

Following meetings with the team, work starts on deploying the website. During discussions AWS was decided upon.
Due to limited support of spatial databases and Django, the decision was made to use Heroku instead.

The deployment process is described in: :ref:`deploy-guide`.

---------------


12 June 2020
------------

All data transferred from the server to the client is now compressed if the total size is over 200 bytes. This is done
using `Django middleware <https://docs.djangoproject.com/en/3.0/ref/middleware/>`_.

A login page was added. It requires users to be authenticated before they can access the uploadData page. Users must
also login when accessing the detailed patient information on the dashboard. Users are added through the Admin page.
There are separate permissions for clinicians and administrators.

.. figure:: pictures/login-page.PNG

    Login page

---------------


13 June 2020
------------

For auditing and information purposes, the user who uploads data through the upload page is logged. Any changes made
later on through the Admin interface are also logged.

.. figure:: pictures/log.png

   Audit log


Detailed data about individual tests was added to the detailed information modal on the dashboard. The data is a DNA
amplification curve (Polymerase chain reaction graph).

This data is obtained based on additions made to the REST API. The user must be authenticated to access this data.


---------------


14 June 2020 - 17 June 2020
---------------------------
Based on feedback from the team, a time slider is added. It allows users to see how testing and positive diagnostics
evolve over time. The slider can be set to move automatically or the user can control it manually. The data can be
displayed for the whole available period or anything down to a single day.

To achieve this, the diagnostic times need to be serialised into `Unix time <https://en.wikipedia.org/wiki/Unix_time>`_
instead of a human readable format. This means that they then need to be converted back to a human readable format on
the client side, to be displayed in the table.

**Issue:** The data for the time based graph on the right needs date data to be in a standard date format (YYYY-MM-DD
or DD/MM/YY...) and is not functional when Unix time is used. This means that the graph cannot be used as is.

**The time slider branch of the repository was not merged with master for the above reason.**

.. figure:: pictures/time-slider-demo_Moment-1.jpg

   Time slider (All tests)

.. figure:: pictures/time-slider-demo_Moment-2.jpg

   Time slider (positive diagnostic tests)



---------------


18 June 2020 - 25 June 2020
---------------------------

Work on the project is finalised. The documentation is written based on code comments, notes and pictures taken
throughout the project. `Sphinx <https://www.sphinx-doc.org/>`_ is used to write the documentation and it's made
available online using `Heroku <https://www.heroku.com/home>`_.

