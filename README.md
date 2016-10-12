# Deputy Overwatch #

Supervise our congressmen spendings.

## Features ##

[**API**](wiki/Api) with every congressman indemnifications budget provided in JSON format.
Checkout the api queries documentation: [wiki/Api](wiki/Api)

## Installation ##

**Deputy Overwatch** is built using [Flask](http://flask.pocoo.org/), an open source Python library for interacting with HTTP. The following steps will require to install the tools listed below:

*   [Python](https://www.python.org/)
*   [pip](https://pip.pypa.io/en/stable/installing/)

1. Clone from bitbucket (this will create a deputy-overwatch folder in the current directory)

        git clone https://bitbucket.org/diogolundberg/deputy-overwatch.git

2. [optional] Create a virtual environment. We suggest installing [virtualenv](https://pypi.python.org/pypi/virtualenv) with [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/). This allows python libraries to be installed easily and specifically on a per project basis.

	Once this is complete, run the following to initialize your environment.

        mkvirtualenv deputy-overwatch
        workon deputy-overwatch

3. Install the required Python libraries

        pip install -r requirements.txt

4. Run the site locally!

        python run.py runserver