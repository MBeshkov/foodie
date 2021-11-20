# django api

1) created a new django project
2) created a new django app '**listings**' inside the project
3) import the newly created app and the framework *rest_framework* in our apps into the project (by adding their name to the file **settings.py**)
4) create a model inside **models.py** (a model is a python class that represent some data. model = table in a relational db)
5) create a serializer for the model you just added inside **serializers.py** (a serializer is used to convert your model into json data. Because ur model is a python class, to be used for example in js it needs to be converted into a universal format)
6) next step is creating a view in **views.py** (a view is basically a function or class that processes a specific request and returns the data requested). In this case I used a default view to list all the elements in a model (same as like 'SELECT * FROM table'). This default model requires you to only specify your model and ur serialiser already created (in step 4 & 5)
7) now we need to map the view we just created to a specific url. (basically specify a way for us to call the view we just created). we first go to django_app and add a line to include the file 'listings/urls.py'. in this **'listings/urls.py'** file we map our view to a specific url (*api/listings*)
9) now when we go to http://127.0.0.1:8000/api/listings/ we can create/view all the elements in our model through this page:

(NOTE: by simply calling GET requests from javascript you can get the data you need)

<img src="https://i.imgur.com/dipmV2p.png" width="70%"/>

useful links:<br>
- tutorial I followed: https://www.valentinog.com/blog/drf/#Django_REST_with_React_Django_and_React_together
- understand models: https://docs.djangoproject.com/en/3.2/topics/db/models/
- understand views: https://docs.djangoproject.com/en/3.2/topics/class-based-views/
- understand serialisers: https://docs.djangoproject.com/en/3.2/topics/serialization/
