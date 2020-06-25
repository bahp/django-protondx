###############
Meeting History
###############

.. contents::
    :depth: 1
    :local:


---------------


04 May 2020
-----------

Attendees
~~~~~~~~~

* Chen Su
* Miguel Cacho Soblechero
* Oliver Stiff


Topics discussed
~~~~~~~~~~~~~~~~

1. Github repository

2. What API to use for the map based visualisation - Suggested ArcGIS

3. Brainstorm website design and potential features

4. Consider various database schemas


Resulting decisions
~~~~~~~~~~~~~~~~~~~

1. Research potentially useful APIs for the whole project

2. Design a draft of the website design - present using Powerpoint

3. Potential division of tasks

    * Chen Su: Front-end design
    * Oliver Stiff : Back-end design


---------------


11 May 2020
-----------

Attendees
~~~~~~~~~

* Bernard Hernandez Perez
* Chen Su
* Miguel Cacho Soblechero
* Oliver Stiff


Topics discussed
~~~~~~~~~~~~~~~~

1. Discuss the proposed website design (Powerpoint presentation)

2. Consider libraries for displaying data in a tabular format


Resulting decisions
~~~~~~~~~~~~~~~~~~~

1. Add more information to the detailed patient view - include PCR graph and clinician comments

2. Visualise data on a map. Have the same information present in a table.
   This information can be aggregated by country / region / city / postcode / patient

3. Start developing the website


---------------

.. _18-05-2020:

18 May 2020
-----------

Attendees
~~~~~~~~~

* Bernard Hernandez Perez
* Chen Su
* Miguel Cacho Soblechero
* Oliver Stiff


Topics discussed
~~~~~~~~~~~~~~~~

1. Confirmation of the design of the website

2. Consider two different website designs

    * Static map with three layers: World -> Country -> Patient level

    * Interactive map with further information displayed in tables and graphs

3. How to obtain a functional spatial database - Spatialite, PostGIS, ...


Resulting decisions
~~~~~~~~~~~~~~~~~~~

1. Keep developing the front-end website

2. Work on the REST API used to query data

3. Add a view where users can upload data

    - user drags and drops .zip archives
    - display extracted information on the screen (e.g. files to upload, diagnostic data, patient data...)


---------------


25 May 2020
-----------

Attendees
~~~~~~~~~

* Bernard Hernandez Perez
* Chen Su
* Miguel Cacho Soblechero
* Oliver Stiff


Topics discussed
~~~~~~~~~~~~~~~~

1. Present an initial version of the website
2. Creating sample data for testing purposes


Resulting decisions
~~~~~~~~~~~~~~~~~~~

1. Focus on integration and finalisation of the minimum viable product

2. Reverse-geocoding - obtain country, region, county and postcode from latitude and longitude

3. Add commands to automatically create and load data into the database


---------------


01 June 2020
------------

Attendees
~~~~~~~~~

* Bernard Hernandez Perez
* Chen Su
* Miguel Cacho Soblechero
* Oliver Stiff


Topics discussed
~~~~~~~~~~~~~~~~

1. Present the upload page and drag & drop functionality

2. Present the reverse-geocoding function

3. Present a draft of the leaflet


Resulting decisions
~~~~~~~~~~~~~~~~~~~

1. Finish website integration

2. Explore transfer to Amazon Web Services

3. Include PCR data on the patient specific view

4. Introduce user management roles - administrators and clinicians

5. Finalise leaflet


---------------


08 June 2020
------------

Attendees
~~~~~~~~~

* Bernard Hernandez Perez
* Chen Su
* Miguel Cacho Soblechero
* Oliver Stiff


Topics discussed
~~~~~~~~~~~~~~~~

1. Present the website as a whole

2. Discuss the Powerpoint for the video demonstration and presentation


Resulting decisions
~~~~~~~~~~~~~~~~~~~

1. Keep exploring the deployment to AWS

2. Finalise all the functions for the website, particularly displaying PCR data

3. Keep working on the demonstration


---------------


15 June 2020
------------

Attendees
~~~~~~~~~

* Bernard Hernandez Perez
* Chen Su
* Miguel Cacho Soblechero
* Oliver Stiff


Topics discussed
~~~~~~~~~~~~~~~~

1. Finalised all functions for the website that agreed on :ref:`18-05-2020`.

2. Suggestions for the video demonstration


Resulting decisions
~~~~~~~~~~~~~~~~~~~

1. Prepare the video demonstration and documents

2. Work on bug-fixing and extending code documentation


---------------


17 June 2020
------------

The aim of this meeting was to present our work to the team at the Centre for Bio-Inspired Technology.

Attendees
~~~~~~~~~

* Bernard Hernandez Perez
* Chen Su
* Miguel Cacho Soblechero
* Nicolas Moser
* Oliver Stiff
* Pantelis Georgiou


Topics discussed
~~~~~~~~~~~~~~~~

1. The overview of the website

2. Comments on work so far

3. Possible future work and improvements

    * Time slider to visualise changes over time
    * Different methods for uploading data (automated using API vs drag & drop upload page)


Resulting decisions
~~~~~~~~~~~~~~~~~~~

1. Adding the time evolution function to better understand the development process of the disease.

2. Automatically upload data using an API - already implemented for ``Patient`` and ``Testing_Centre`` database tables


---------------


22 June 2020
------------

Attendees
~~~~~~~~~

* Bernard Hernandez Perez
* Chen Su
* Miguel Cacho Soblechero
* Oliver Stiff


Topics discussed
~~~~~~~~~~~~~~~~

1. Discuss documentation format for both pdf and website


Resulting decisions
~~~~~~~~~~~~~~~~~~~

1. Keep working on the documentation

2. Use a website as the platform for our documentation. Have a PDF version to make it easily accessible offline.