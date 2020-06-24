##################################
Sources of code and resources used
##################################

.. contents::
    :depth: 1
    :local:


--------------


Python
------

See :ref:`python-packages-list` for a full list of python packages used.


-----------------

.. _geographical-data:

Geographical data and resources
-------------------------------

Country boundaries
~~~~~~~~~~~~~~~~~~

Made with Natural Earth. Free vector and raster map data @ naturalearthdata.com.

`Country boundaries <https://www.naturalearthdata.com/downloads/50m-cultural-vectors/50m-admin-0-countries-2/>`_

Region Boundaries
~~~~~~~~~~~~~~~~~

**Source:** Office for National Statistics licensed under the Open Government Licence v.3.0

Contains OS data © Crown copyright and database right [2020]

`Region boundaries <https://geoportal.statistics.gov.uk/datasets/nuts-level-1-january-2018-full-clipped-boundaries-in-the-united-kingdom/data>`_

County boundaries
~~~~~~~~~~~~~~~~~

**Source:** Office for National Statistics licensed under the Open Government Licence v.3.0

Contains OS data © Crown copyright and database right [2020]

`County boundaries <http://geoportal.statistics.gov.uk/datasets/b216b4c8a4e74f6fb692a1785255d777_0>`_

Postcode Sector boundaries
~~~~~~~~~~~~~~~~~~~~~~~~~~

Accessed through the ArcGIS portal.

`Sector Boundaries <https://services.arcgis.com/dvWpUrMTxKmay5qM/arcgis/rest/services/PCSector%20with%20Regions/FeatureServer>`_


Postcode reverse geo-coding
---------------------------

Reverse geo-coding from coordinates to UK postcodes was done using `Postcodes.io <http://api.postcodes.io/>`_.


---------------


Javascript
----------

Ajax loading gif
~~~~~~~~~~~~~~~~

**Version:** N/A

**Link:** http://cdnjs.cloudflare.com/ajax/libs/semantic-ui/0.16.1/images/loader-large.gif

Loading gif used in dataUpload template.


ArcGIS
~~~~~~

**Version:** 4.15 (Javascript API)

**Link:** https://developers.arcgis.com/javascript/latest/api-reference/

Used to provide the map in the dashboard (dash.html).
Provides the basemaps and a series of additional features and widgets through the API.


Chart.js
~~~~~~~~

**Version:** 2.8.0

**Link:** https://www.chartjs.org/

Used to plot graphs and charts in the dashboard (dash.html)


Datatables
~~~~~~~~~~

**Version:** 1.10.21

**Link:** https://datatables.net/

Used to present data in a tabular format.
Add sorting and search to HTML tables.
Used in the dashboard (dash.html) for the overview diagnostic data and the detailed data
in the patient specific view.


Datatables buttons plugin
~~~~~~~~~~~~~~~~~~~~~~~~~

**Version:** 1.6.2

**Link:** https://datatables.net/extensions/buttons/

Plugin to add column selection to Datatables.


Datatables datetime-moment plugin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Version:** 1.10.21

**Link:** https://datatables.net/plug-ins/sorting/datetime-moment

Plugin to support better Date-Time sorting and support in Datatables.


Datatables responsive plugin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Version:** 2.2.4

**Link:** https://datatables.net/extensions/responsive/

Plugin to make Datatable resize dynamically with the window.


Jquery
~~~~~~

**Version:** 3.5.1

**Link:** https://jquery.com/

Used in the dashboard and upload templates. (Makes JS more versatile and extendable)


JSZIP
~~~~~

**Version:** 3.3.0

**Link:** https://stuk.github.io/jszip/

Used in the dataUpload template to unzip archives.


JSZipUtils
~~~~~~~~~~

**Version:** N/A

**Link:** https://github.com/Stuk/jszip-utils

Extends JSZip.


Moment.JS
~~~~~~~~~

**Version:** 2.22.2

**Link:** https://momentjs.com/

Used to extend Date-Time support in Javascript.
Used throughout the dashboard (dash.html) to convert between time formats.
(e.g. Unix time to human readable date)
