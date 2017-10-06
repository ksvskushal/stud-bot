# Updates API

An API for maintaining updates.

## Getting Started

Install flask, postgreSQL and run the server using the following commands.

### Installing

To install flask and postgreSQL.

Note: Use sudo only if some errors pop up.

```
sudo pip3 install flask
sudo pip3 install flask-sqlalchemy psycopg2 flask-migrate
sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
sudo su - postgres
```

Do the following to make a new user:

Note: The username of postgreSQL should be same as your terminal username.

```
psql
CREATE USER myprojectuser WITH PASSWORD 'password';
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
```
```
sudo -u postgres psql -c 'alter user myprojectuser with createdb' postgres
```
Change postgreSQL settings in instance/config.py accordingly.
```
sudo pip3 install Flask-API
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade
python3 run.py
```

## Testing

If you on IITG network, you can test the API using [this link](172.16.115.46:5000/updatelists). Use curl or [Postman](https://www.getpostman.com/apps) to send GET, POST, PUT and DELETE requests.

E.g Open terminal and type:

curl -H "Content-Type: application/json" -X POST -d '{"data": "New assignments are available"}' http://172.16.115.46:5000/updatelists/

curl -H "Content-Type: application/json" -X POST -d '{"data": "Another update"}' http://172.16.115.46:5000/updatelists/

curl -H "Content-Type: application/json" -X PUT -d '{"data": "New assignment is available"}' http://172.16.115.46:5000/updatelists/1/

curl -H "Content-Type: application/json" -X DELETE http://172.16.115.46:5000/updatelists/1/

curl -H "Content-Type: application/json" -X GET http://172.16.115.46:5000/updatelists/2/


## Built With

* Flask - A microframework for Python based on Werkzeug, Jinja 2 and good intentions
* [PostgreSQL](https://www.postgresql.org/) -  A powerful, open source object-relational database system

## Authors

* **Vivek Raj**
