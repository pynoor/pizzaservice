# Project: Pizza Ordering Service using the RESTful API concept

## Introduction:
In this repo I will be creating a simple pizza ordering service as a REST (Representational State Transfer) API (Application Programme Interface).

Wait, what actually is an API? Well from my understanding and in really (I mean really) simple terms: an API is the interface that lets other machines use your webservice. Say I want to request information from facebook. Then I can do that through their API's. More specifically. I can do that through Http requests. The response will most likely be in JSON, which is a textual representation of my response.

Great, now that we now what an API is, what is this RESTful stuff? Well, for anything really, you need a specific way to do things. Otherways everyone is just gonna do their own thing and that would create a huge mess. So we need guidelines to create API's. REST is a set of guidelines. It comes with its own framework, which makes a lot of stuff way easier than having to code everything by yourself, from scratch. The main idea of REST is that when you are requesting information from a web service, you are requesting >representational states< of certain objects. Example: if we want to GET information on a widget from a website http://example.com/, we would make the Http request http://example.com/widgets, which will respond with the >state< of the widget expressed in a JSON file.

Cool, now that we know what a REST API is, let's get started.

## The task:
We want to have a simple pizza delivery service with the following functionalities:

- C reate an order (POST request)
- R etrieve an order / See a list of all orders (GET request)
- U pdate an order (PUT request)
- D elete an order (DELETE request)

(CRUD is actually a thing, more about that here: https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)

The Order data should be as follows:
- pizza id
- pizza size
- customer name
- address

## The database:
Starting off this project, I wanted to keep things as simple as possible. So I only had one model, which was 'order'. On further reflection, I think it would make sense to add at least two more models which will be 'Customer' and 'Pizza'. That will allow us to smoothly make more specific requests such as 'How many times a specific pizza has been ordered' or 'Who is our most loyal customer'.

## Tests:
I will be attempting to do TDD (Test driven development) all throughout the project, let's see how this will go.

The tests can be performed by executing the following command from the command line:

>$ python3 manage.py test

Specific tests can be ran by:

>$ python3 manage.py test app_name.tests

## Disclaimers:

This is my second project using Django and my first time ever using the Django REST framework. Don't judge.

Also, Django seems to use Sqlite3 by dhttps://github.com/pynoor/pizzaserviceefault, however I was asked to use PostgreSQL. Therefore, I have configured the DATABASE section in the settings.py file to use my Postgresql database 'pizzaservicedb'.
How I did that and more on how Django handles databases to be found here:
https://docs.djangoproject.com/en/2.0/ref/databases/



## Useful Resources:

http://www.django-rest-framework.org/

https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-1

http://www.andrewhavens.com/posts/20/beginners-guide-to-creating-a-rest-api/

https://docs.djangoproject.com/en/2.0/topics/testing/overview/

https://docs.djangoproject.com/en/2.0/ref/databases/

https://medium.com/@jtpaasch/the-right-way-to-use-virtual-environments-1bc255a0cba7

https://docs.djangoproject.com/en/2.0/releases/1.9/#features-deprecated-in-1-9

https://docs.djangoproject.com/en/2.0/ref/urlresolvers/

https://www.postgresql.org/docs/9.5/static/datatype.html

https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html

https://docs.djangoproject.com/en/2.0/ref/models/fields/