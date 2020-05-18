# django-protondx

Short introduction or overview that explains **what** the project is. This description should match descriptions added for package managers (Gemspec, package.json, etc.)

You can also add some badges/states next to Project Name, e.g,
+ [Travis CI](https://travis-ci.org/)
+ [AppVeyor](http://www.appveyor.com/)
+ [Coveralls](https://coveralls.io/)
+ [Gitter](https://gitter.im/)
+ [Shields.io](http://shields.io/)
+ Others (python versions...)

## Features or Example

## Motivation

## Requirements

See requirements.txt

+ Django
+ django-admin
+ django-rest-framework
+ django-rest-swagger
+ django-import-export
+ django-filter

## Installation


First, ensure that you have python installed

    $ which python  # python 2
    $ which python3 # python 3
   
Then, lets create a virtual environment for our project (e.g. virtualenv)

    $ virtualenv -p <python3-path> <virtualenv-name>  # Create the environment
    $ source <virtualenv-name>/bin/activate           # Activate virtual enviroment

Then, go to the corresponding folder and install the requirements

    $ pip install -r requirements.txt   # Install requirements
    
  

##### Spatial database Linux (Ubuntu) install guide:
Install Spatialite

    $ sudo apt install libsqlite3-mod-spatialite 

Install geospatial libraries

    $ sudo apt install binutils libproj-dev gdal-bin

If getting issues when migrating clear dashboard/migrations directory and then

    $ python manage.py flush
    $ python manage.py makemigrations
    $ python manage.py migrate


## Usage

Remember to do the migrations when altering the database
 
    $ python manage.py makemigrations <appname>
    $ python manage.py migrate
   
If it is the first time, create a superuser (user:cbit, pass:toor)

    $ cd protondx
    $ python manage.py createsu
  
Run the server locally

    $ python manage.py runserver
   
Go to the browser and access the admin localhost:8000/admin

For more information read the django docs

## Reference

+ [jxson](https://gist.github.com/jxson) - [README.md](https://gist.github.com/jxson/1784669)
+ [gistfrojd](https://gist.github.com/gistfrojd) - [README.md](https://gist.github.com/gistfrojd/5fcd3b70949ac6376f66)

Depending on the size of the project, if it is small and simple enough the reference docs can be added to the README. For medium size to larger projects it is important to at least provide a link to where the API reference docs live.

## Contributors

Let people know how they can dive into the project, include important links to things like issue trackers, irc, twitter accounts if applicable.

## License

A short snippet describing the license ([MIT](http://opensource.org/licenses/mit-license.php), [Apache](http://opensource.org/licenses/Apache-2.0), etc.)


## To Do
+ Geo-Location: There are many approaches to address this problem. The first option is to just save the coordinates (latitude and longitude) sent by the phone in the .json. If using this project evaluate 
whether using Float or Decimal models for the database. In addition, have a look to other django libraries that might be way more powerful and the benefits they could bring (e.g. GeoDjango, django-geoposition)

+ Reusability: Remember to follow the reusable app tutorial once the work is done (https://docs.djangoproject.com/en/3.0/intro/reusable-apps/)


https://docs.djangoproject.com/en/3.0/intro/reusable-apps/