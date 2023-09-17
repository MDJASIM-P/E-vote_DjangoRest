Back_end
--------
@ create an env 
    >py -m pip install virtualenv
    >py -m virtualenv djenv
    Activate the env 
    >djenv\Scripts\activate 
    Install django
    >pip install django 
    >pip install pillow 
    Install RestAPI
    >pip install djangorestframework
@ create django project 
    >django-admin startproject evot 
    Go to setings and add the followings in applications 
    'rest_framework'
    'rest_framework.authtoken'
@ change path to evot
    >cd evot
@ create an applications 'account', 'candidate', 'event' add in settings
    >py manage.py startapp account

Create Models
-------------
CustomUser :

Before making first migration.
Import AbstractUser from django in-build models and created new fields [std_id , voter_id, year and status].
Add AUTH_USER_MODEL = 'account.CustomUser' in settings .
Username considered as phone_number.
@ migrate
    >py manage.py makemigrations 
    >py manage.py migrate 
@ create UserSerializer and UserView using ViewSet
@ make path to 'user' using DefaultRouter class and register method

created superuser 
>py manage.py createsuperuser 
username:admin 
email:admin@gmail.com 
password:Admin@123

Candidate :

Event :





To Get Candidates array sort by votes in dsc order
1. the following Added in View class 
    from rest_framework import filter
    filter_backends = [filters.OrderingFilter]
    ordering_fields= ['votes']
2. in path of get request 
    localhost/candidates?ordering=-votes