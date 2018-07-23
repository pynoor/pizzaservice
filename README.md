# Project: Pizza Ordering Service using the RESTful API concept

## Introduction:
In this repo I will be creating a simple pizza ordering service as a REST (Representational State Transfer) API (Application Programme Interface).

Wait, what actually is an API? Well from my understanding, after watching at least 5 videos about it and having my boyfriend explain it to me several times an API is the interface that lets other machines use your webservice. Say I want to request information from facebook. Then I can do that through their API's. More specifically. I can do that through Http requests. The response will most likely be in JSON, which is a data file type for text.

Great, now that we now what an API is, what is this RESTful stuff? Well, for anything really, you need a specific way to do things. Otherways everyone is just gonna do their own thing and that would create a huge mess. So we need guidelines to create API's. REST is a set of guidelines. It comes with its own framework, which makes a lot of stuff way easier than having to code everything by yourself, from scratch. The main idea of REST is that when you are requesting information from a web service, you are requesting >representational states< of certain objects. Example: if we want to GET information on a widget from a website http://example.com/, we would make the Http request http://example.com/widgets, which will respond with the >state< of the widget expressed in a JSON file.

Cool, now that we know what a REST API is, let's get started.

## The task:
We want to have a simple pizza delivery service with the following functionalities:

- C reate an order
- R etrieve an order / See a list of all orders
- U pdate an order
- D elete an order

(CRUD is actually a thing, more about that here: https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)

The Order data should be as follows:
- pizza id
- pizza size
- customer name
- address

I will be attempting to do TDD (Test driven development) all throughout the project, let's see how this will go.

## Disclaimers:

This is my second project using django and my first time ever using the Django REST framework. Don't judge.

Also, Django seems to use Sqlite by Default, however I was asked to use PostgreSQL. I will be starting off by using the default database and will try to find out how to switch to PostgreSQL along the way.
More on how Django handles databases to be found here:
https://docs.djangoproject.com/en/2.0/ref/databases/



## Useful Resources:

http://www.django-rest-framework.org/

https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-1

http://www.andrewhavens.com/posts/20/beginners-guide-to-creating-a-rest-api/

https://docs.djangoproject.com/en/2.0/topics/testing/overview/

https://docs.djangoproject.com/en/2.0/ref/databases/
