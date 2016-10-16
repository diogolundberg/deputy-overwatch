# Deputy Overwatch #

Supervise our congressmen spendings.

## Features ##

[**API**](https://bitbucket.org/diogolundberg/deputy-overwatch/wiki/Api) with every congressman indemnifications budget provided in JSON format.
Checkout the api queries documentation: [wiki/Api](https://bitbucket.org/diogolundberg/deputy-overwatch/wiki/Api#markdown-header-examples)


## Dependencies ##

Various [**3rd Party libraries**](https://bitbucket.org/diogolundberg/deputy-overwatch/wiki/Dependencies) are needed in order to run **Deputy Overwatch**.
Checkout the Dependencies documentation: [wiki/Dependencies](https://bitbucket.org/diogolundberg/deputy-overwatch/wiki/Dependencies)

* [Flask](http://flask.pocoo.org/)
* [SQLAlchemy ](http://www.sqlalchemy.org/)
* [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/)
* [Flask-Runner](http://flask-runner.readthedocs.io/en/latest/)
* [Flask-Runner](http://flask-script.readthedocs.io/en/latest/)
* [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
* [Faker](http://faker.readthedocs.io/en/master/index.html)
* [factory_boy](https://factoryboy.readthedocs.io/en/latest/)
* [inflection](https://inflection.readthedocs.io/en/latest/)
* [xmltodict](https://github.com/martinblech/xmltodict)
* [webargs](https://webargs.readthedocs.io/en/latest/)

## Installation ##

**Deputy Overwatch** is built using [Flask](http://flask.pocoo.org/), an open source Python library for interacting with HTTP. The following steps will require to install the tools listed below:

*   [Python 3.5](https://www.python.org/)
*   [pip](https://pip.pypa.io/en/stable/installing/)

1. Clone from bitbucket (this will create a deputy-overwatch folder in the current directory)

        git clone https://bitbucket.org/diogolundberg/deputy-overwatch.git

2. [optional] Create a virtual environment. We suggest installing [virtualenv](https://pypi.python.org/pypi/virtualenv) with [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/). This allows python libraries to be installed easily and specifically on a per project basis.

	Once this is complete, run the following to initialize your environment.

        mkvirtualenv deputy-overwatch
        workon deputy-overwatch

3. Install the required Python libraries

        pip install -r requirements.txt

4. Create the database

       From the project's folder:

        python run.py db upgrade

4. Scrape data to fill your database

       From the project's folder:

        python run.py scrape

6. Run the site locally!

        python run.py runserver


## Contribution Guide ##

* Make sure to check where the database is being created(project's root) and get a SQLite client to check it! 

* This project is set up to check pep8 offenses in a pipeline, install a good linter to save time 

* Finally, the **most important**, run tests!

## Running tests ##

I strongly recommend you to run:

     nosetests --ignore-files=scraper

This will ignore the scraper tests, saving a lot of time. The scraping can take up to 8 minutes!

But, if you like to check **every single test**:

     python run.py test