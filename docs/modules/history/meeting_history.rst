###############
Meeting History
###############

.. contents::
    :depth: 1
    :local:


---------------


04/05/2020
----------

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


11/05/2020
----------

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


18/05/2020
----------

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

3. Adding the updating data function (1) user drags/drop .zip file; (2) display main information on the screen (e.g. files to upload, size, experiment id, patient id, elapsed time, age, gender, ....).


---------------


25/05/2020
----------

Attendees
~~~~~~~~~

* Bernard Hernandez Perez
* Chen Su
* Miguel Cacho Soblechero
* Oliver Stiff


Topics discussed
~~~~~~~~~~~~~~~~

1. Present the draft website that the front-end is almost completed without data available.


Resulting decisions
~~~~~~~~~~~~~~~~~~~

1. Focus on integration and finalising the functionality

2. Reverse-geocoding (from lat-lon to postcode, city, state, country).


---------------


01/06/2020
----------

Attendees
~~~~~~~~~

* Bernard Hernandez Perez
* Chen Su
* Miguel Cacho Soblechero
* Oliver Stiff


Topics discussed
~~~~~~~~~~~~~~~~

1. Present the upload page and drag-file function.

2. Present the reverse-geocoding function

3.  Present draft Leaflet


Resulting decisions
~~~~~~~~~~~~~~~~~~~

1. Finish the integration.

2. Explore transfer to Amazon Web Services

3. Include PCR data

4. Introduce user management roles - mostly for doctors

5. Finalise leaflet - Send by Tuesday for feedback


---------------


08/06/2020
----------

Attendees
~~~~~~~~~

* Bernard Hernandez Perez
* Chen Su
* Miguel Cacho Soblechero
* Oliver Stiff


Topics discussed
~~~~~~~~~~~~~~~~

1. Present the website as whole

2. Discuss the PPT for video demonstration


Resulting decisions
~~~~~~~~~~~~~~~~~~~

1. Keep exploring the AWS

2. Finalise all the functions for the website, particularly PCR data.

3. Keep working the demonstration


---------------


15/06/2020
----------

Attendees
~~~~~~~~~

* Bernard Hernandez Perez
* Chen Su
* Miguel Cacho Soblechero
* Oliver Stiff


Topics discussed
~~~~~~~~~~~~~~~~

1. Finalised all functions for the website that agreed  in 5/18/2020

2. Suggestions for the video demonstration


Resulting decisions
~~~~~~~~~~~~~~~~~~~

1. Preparing the video demonstration and documents


---------------


17/06/2020
----------

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

2. Comments for the product


Resulting decisions
~~~~~~~~~~~~~~~~~~~

Attendess: Bernard Hernandez Perez, Chen Su, Miguel Cacho Soblechero, Oliver Stiff

1. Adding the time evolution function to better understand the development process of the disease.

2. Automatically updating the backend data.


---------------


22/06/2020
----------

Attendees
~~~~~~~~~

* Bernard Hernandez Perez
* Chen Su
* Miguel Cacho Soblechero
* Oliver Stiff


Topics discussed
~~~~~~~~~~~~~~~~

1. Discuss Documentation  format for both pdf and website.


Resulting decisions
~~~~~~~~~~~~~~~~~~~

1. Keep working on the documentation