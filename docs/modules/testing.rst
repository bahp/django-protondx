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

Application: Test requests are sent correctly to the Database and output at the client side is displayed correctly. Errors if any must be caught by the application and must be only shown to the administrator and not the end user.
Web Server: Test Web server is handling all application requests without any service denial.
Database Server: Make sure queries sent to the database give expected results.

Test system response when connection between the three layers (Application, Web and Database) cannot be established and appropriate message is shown to the end user.


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

Connection Speed
Tested on various networks like Dial-Up, ISDN, etc.

Load
i. What is the no. of users per time?
ii. Check for peak loads and how the system behaves
iii. A large amount of data accessed by the user

Stress
i. Continuous Load
ii. Performance of memory, CPU, file handling, etc..

Make sure optimization techniques like gzip compression, browser and server side cache enabled to reduce load times


-----------------


Security Testing
----------------

**Does the website have any potential vulnerabilities**

using username and password and browsing internal pages then try changing URL options directly. I.e. If you are checking some publisher site statistics with publisher site ID= 123. Try directly changing the URL site ID parameter to different site ID which is not related to the logged-in user. Access should be denied for this user to view other's stats.
Try some invalid inputs in input fields like login username, password, input text boxes, etc. Check the system's reaction to all invalid inputs.
Web directories or files should not be accessible directly unless they are given download option.
Test the CAPTCHA for automating script logins.
Test if SSL is used for security measures. If it is used, the proper message should get displayed when users switch from non-secure HTTP:// pages to secure HTTPS:// pages and vice versa.
All transactions, error messages, security breach attempts should get logged in log files somewhere on the webserver.
The primary reason for testing the security of a web is to identify potential vulnerabilities and subsequently repair them.

Network Scanning
Vulnerability Scanning
Password Cracking
Log Review
Integrity Checkers
Virus Detection

