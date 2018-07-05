# Paranuara Rest API
Assumes Python 2  and MySql installed in system

## Getting started
The Following Commands will need to be run to set up your environment

`pip install -r requirements.txt`

`mysql -u {{admin_db_user}} -p < db_setup.sql // You will be prompted for a password`
`./manage.py migrate`
`./manage.py makemigrations api`
`./manage.py migrate`
`./manage.py loaddata fixtures/food_items.json`
`./manage.py loaddata fixtures/companies.json`
`./manage.py loaddata fixtures/people.json`
`./manage.py runserver`

## The endpoints
The endpoints can be reached at the following addresses
`http://localhost:8000/api/person/1`
`http://localhost:8000/api/company/1`
`http://localhost:8000/api/person/1/common-friends/2`

## The approach
I decided to clean the resources provided such that they could be loaded as standard django fixtures, The script used to clean these can be found in `scripts/clean_fixtures.py`
Many of the fields in the fixtures were excluded as they were unrelated to the requested functionality