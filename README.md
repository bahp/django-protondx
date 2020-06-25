# django-protondx

# Documentation

The complete documentation can be found [here](https://protondx-documentation.herokuapp.com/).

It can also be found in the repository [here](documentation.zip). Extract the archive and open `index.html`.

## Requirements

See [requirements.txt](requirements.txt) or the
 [documentation](https://protondx-documentation.herokuapp.com/_build/html/modules/install/requirements.html) for more
 details.

+ Django
+ django-admin
+ django-rest-framework
+ django-rest-swagger
+ django-import-export
+ django-filter

## Installation


### Environment


First, ensure that you have Python 3 installed

```
   $ which python3 # python 3
```

Then, lets create a virtual environment for our project (e.g. virtualenv)

```
   $ virtualenv -p <python3-path> <virtualenv-name>  # Create the environment
   $ source <virtualenv-name>/bin/activate           # Activate virtual enviroment
```

Clone the repository.


Then, go to the corresponding folder and install the requirements

```
   $ pip install -r requirements.txt   # Install requirements
```


### Spatial database (Linux)


Install Spatialite

```
    $ sudo apt install libsqlite3-mod-spatialite
```

Install geospatial libraries
```
    $ sudo apt install binutils libproj-dev gdal-bin
```
If getting issues when migrating clear dashboard/migrations directory and then

```
    $ python manage.py flush
    $ python manage.py makemigrations
    $ python manage.py migrate
```
    
  

##### Spatial database Linux (Ubuntu) install guide:
Install Spatialite
```
    $ sudo apt install libsqlite3-mod-spatialite 
```
Install geospatial libraries
```
    $ sudo apt install binutils libproj-dev gdal-bin
```
If getting issues when migrating clear dashboard/migrations directory and then
```
    $ python manage.py flush
    $ python manage.py makemigrations
    $ python manage.py migrate
```

## Usage

Remember to do the migrations when altering the database

```
    $ python manage.py makemigrations <appname>
    $ python manage.py migrate
```

If it is the first time, create a superuser (user:cbit, pass:toor)

```
    $ cd protondx
    $ python manage.py createsu
```

### Development


Run the server locally

```
    $ python manage.py runserver
```
Access the dashboard and relevant pages at:

* localhost:8000/dashboard  or  localhost:8000
* localhost:8000/dataUpload
* localhost:8000/admin

### Production

Access the dashboard and relevant pages at:

* <hostname>/dashboard  or  <hostname>
* <hostname>/dataUpload
* <hostname>/admin
