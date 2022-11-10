# _e-shop

e-Shop is an online shopping app

Heroku [link](https://e-shop-43rt1q.herokuapp.com/)

### Prerequisites	

First clone repository:
```
git clone 'repository'
```
Then you need to build containers with the following command:
```
docker-compose up --build
```
### Create database and user
```
docker exec -it e-shop_db bash
su postgres
psql
CREATE DATABASE e-shop;
CREATE USER e-shop_admin WITH PASSWORD 'admin';
GRANT ALL PRIVILEGES ON DATABASE e-shop TO e-shop_admin;
```
### Running the migrations
```
docker-compose run --rm eshop python manage.py migrate
```
### Create a superuser
```
docker-compose run --rm eshop python manage.py createsuperuser
```
### Running 
```
docker-compose up
```
### Built With

* [Python](https://www.python.org) - an interpreted high-level general-purpose programming language
* [Django](https://docs.djangoproject.com/en/3.2/) - web framework
* [Django Rest Framework](https://www.django-rest-framework.org) - toolkit for building Web APIs
* [PostgreSQL](https://www.postgresql.org) - open source object-relational database system
* [Postman](https://www.postman.com) - an API platform for building and using APIs
* [Docker](https://www.docker.com) - Docker is an open platform for developing, shipping, and running applications

### Postman Collection

* [Here](https://www.postman.com/science-technologist-34779379/workspace/e-shop/collection/23948712-07902497-b813-4ccc-bae1-313dcba1a670?action=share&creator=23948712) is the project's Postman collection

## Author

* Bek Akmatbek uulu