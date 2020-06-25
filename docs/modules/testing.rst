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
    * Data gets added to database (Subject to browser support see :ref:`requirements-browser` and :ref:`compatibility-testing`)

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
- functional forms (see compatibility testing and requiremtns...)

Cookies
~~~~~~~
- test cookies for login details


-----------------


Usability Testing
-----------------

**Is the website user-friendly? Has the content been verified?**

User testing
~~~~~~~~~~~~

- website used by devs + external tester (student/team)
- site navigation and controls...
- Check for user intuition.

Content
~~~~~~~

- content checked


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


Operating system
~~~~~~~~~~~~~~~~


Device
~~~~~~
d

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

