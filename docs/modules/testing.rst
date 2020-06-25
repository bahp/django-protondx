###############
Product testing
###############

.. contents::
    :depth: 1
    :local:


---------------


Functionality Testing
---------------------

**Does the website operate as specified and does it meet the intended functional requirements?**

The functionality testing was done by verifying all links, forms and pages on the site.

Features
~~~~~~~~

The site features were tested manually by developers.

The features tested included the following:

* Access to dashboard page
* Loading of diagnostic test geographical data
* Use of map and widgets

    * Zoom in/out using widgets, scroll-wheel and [+]/[-] on keyboard when map is selected
    * Rotate map using mouse R-button, [a]/[d] on keyboard
    * Reset map view using 'Home' widget
    * Select basemap, using 'Basemap' widget
    * Collapse map legend and renderer selection
    * Select renderer using radio-buttons (Heatmap or Dot renderer)

        * Proper display of extended feature menu when dot renderer is selected
        * Select which features to display when using dot renderer

    * Enable/disable postcode boundaries
    * Search for an address or location, using map search bar
    * Enter/exit full screen map view using the 'Expand' widget
    * Select Countries, UK regions, UK postcode sector
    * Zoom in on selection
    * Popup statistics for selection

* Charts and statistics

    * Display pie charts and line graph
    * Display country / region / postcode name on map selection
    * Update charts on map selection
    * Graph resizing based on window size
    * Correct Chart.js feature integration

        * Display tooltip on hover
        * Show/hide attributes using legend

* Table

    * Display table using Datatables
    * Display GeoJSON data in table
    * Sort alphabetically or by date
    * Search and filter dataset
    * Set column visibility
    * Resize with window

* Detail view

    * Require user authentication
    * Display when table entry is clicked
    * Display patient information and diagnostic tests
    * Calculate patient age from date of birth
    * Display PCR and comments on diagnostic selection
    * Display table using Datatables
    * Display data in table
    * Sort alphabetically or by date
    * Search and filter dataset

* Upload data

    * Drag and drop or select files
    * Display selected files in list (bottom left)
    * List shows loading progress for each file
    * List can be used to display data for selected file
    * Stop upload of files with incompatible format (Error message)
    * File data is auto-completed into form
    * User can amend form
    * Data gets added to database (Subject to browser support see
      :ref:`requirements-browser` and :ref:`compatibility-testing`)

* Administrator interface

    * Require login
    * Add users and user groups
    * Import / export database data
    * Add, modify, delete individual entries
    * Access audit logs for all database objects


All HTML templates, Javascript files and CSS files were checked for valid syntax.

Links
~~~~~

* All links to external websites were verified as being valid (e.g. 'About' and 'Contact' in menu)
* All internal and anchor links were tested
* Redirects were verified as being correct

    * <hostname> redirects to <hostname>/dashboard
    * <hostname>/dataUpload redirects to <hostname>/accounts/login/?next=/dataUpload/ when user is not logged in

        * User gets redirected to dataUpload page on successful login

Forms
~~~~~

The forms on the dataUpload page get created when a .zip archive which contains a JSON file is uploaded. Checks were
made to ensure forms cannot be submitted with required fields missing. Similarly, that they can be submitted when
optional fields are omitted.


-----------------


Usability Testing
-----------------

**Is the website user-friendly? Has the content been verified?**

User testing
~~~~~~~~~~~~

The website usability was tested by both developers and external users. Site navigation and controls were tested by
using the website as a typical user would.

Having developers use the site makes it possible to determine if all features and functionality operate as intended.
This was found to be the case when the :ref:`requirements-browser` requirements were met.

However, usability and user intuition are better determined when users who have never see the site before are asked to
interact with it. A student who had never used the site before was supplied with a username and password and asked to
use the site. They were able to successfully navigate the site and access all of its features. The dashboard was found
to be intuitive to use with the user quickly figuring out how to use the map to gain information. The user was also able
to display and use the detail view, without having prior knowledge of its existence.


Content
~~~~~~~

The content was checked for spelling and grammatical errors. The legibility of all content on the site was also ensured
by making all text elements have high contrast ratios. The minimum recorded contrast ratio was 8.59:1. This is well
above the minimum of 7.0:1 needed to reach the
`Web Content Accessibility Guidelines 2.0 <https://www.w3.org/TR/WCAG20/>`_ level AAA rating.

-----------------


Interface Testing
-----------------

**Do interactions between the client, server and database operate as desired?**



-----------------

.. _compatibility-testing:

Compatibility Testing
---------------------

**Which browsers, operating systems and devices are supported?**

Browser
~~~~~~~

Browser support is summarised in the :ref:`requirements-browser` requirements.

The browser must support WebGl and CSS grid in order for the page to be displayed properly and have access to the map.

All of the platform's features are supported on Google Chrome and Brave Browser which were used for testing during
development. Firefox and Opera were also found to support all of the website's features. Many Chromium browsers are
likely to be compatible but this has not been tested other than for the browsers mentioned here.

The dashboard has no compatibility issues with Safari and Microsoft Edge. These browsers, however, cannot be used when
uploading data due to different security restrictions.

Internet explorer is not supported due to issues with CSS grids.

Operating system
~~~~~~~~~~~~~~~~

The operating system was not found to have an impact as long as :ref:`requirements-browser` requirements are respected.

Device
~~~~~~

Whilst the dashboard was found to be functional on mobile devices (subject to browser support), it is not recommended as
a method of accessing the |project_name| website.

-----------------


Performance Testing
-------------------

**How are peak and sustained loads handled?**

Performance testing was done in a very limited capacity due to the unavailability of resources needed to carry out
complete tests. The platform, as currently deployed, can support a maximum of 20 concurrent users due to limits on the
number of database connections. The number of rows in the database is also restricted to 10000, limiting the amount of
information which can be uploaded.

The web application, being deployed on Heroku can be scaled easily by adding more
`Dynos <https://www.heroku.com/dynos>`_ which will allow for more concurrent users to be served and more processing
power. The database would also need to be upgraded to support more data storage and simultaneous users. A database with
better hardware (quicker drives, more processing power, more RAM) would reduce query times. This would make reduced
loading times or serving more users a possibility.

The current server is also set to sleep after 30 minutes of inactivity. The dynos then need to be restarted when the
website is next accessed which impacts loading times. A payed Heroku subscription would resolve this issue.

Loading times have already been reduced by introducing compression for static files and other data transferred to
clients. Gzip compression reduced loading times by 22.1% and the amount of data transferred by 5.6%.

.. list-table:: Dashboard loading times and resources transferred
   :header-rows: 1

   * - Compression
     - Requests
     - Data transferred
     - Uncompressed data
     - Loading time
   * - No
     - 195
     - 7.1 MB
     - 19.7 MB
     - 22.81 s
   * - **Yes**
     - 195
     - 6.7 MB
     - 19.7 MB
     - 17.77 s


The differences on the dataUpload page were negligible due to the little amount of data transferred.

As the number of datapoints increases, the benefit of having compression is expected to increase.

-----------------


Security Testing
----------------

**Does the website have any potential vulnerabilities?**

User authentication
~~~~~~~~~~~~~~~~~~~

There are several pages or API requests which require the user to be authenticated. Before access is granted or data is
transferred, the user's login credentials must be checked and validated. It is not enough for the user to be logged-in,
the user must belong to a user group which has access to that specific resource.

Admin page:

    * **Valid administrator credentials**: Access granted
    * **Invalid credentials**: Access rejected
    * **Logged in but not administrator**: Access rejected and display the following:
      "You are authenticated as <Username>, but are not authorized to access this page. Would you like to login to a
      different account?"


Dashboard page:

    * Access granted regardless of user authentication

    * When accessing the detail view, access is requested

        * **Valid credentials**: Access granted to detail view
        * **Invalid credentials**: Access rejected, no data is ever displayed or successfully queried from database


DataUpload page:

    * **Valid credentials and user**: A user who enters correct credentials will be given access to the dataUpload page.
    * **Invalid credentials**: Access rejected and display the following:
      "Your username and password didn't match. Please try again."

Forms and uploads
~~~~~~~~~~~~~~~~~

When data is uploaded, it is first 'cleaned' to remove any malicious entries before it is accessed or added to the
database. This process is handled directly by Django and was therefore not tested.



