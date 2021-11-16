# foodie

- create a new django project
- create a new django app inside the project
- import the newly created app into the settings of the project
- create a model inside the models.py (a model is a python class that represent some data. model = table in a relational db)
- create a serializer for the model you just added inside serializers.py (a serializer is used to convert your model into json data. Because ur model is a python class, to be used for example in js it needs to be converted into a universal format)
- next step is creating a view in views.py (a view is basically a function or class that processes a specific request and returns the data requested). In this case I used a default view to list all the elements in a model (same as like 'SELECT * FROM table'). This default model requires you to only specific your model and ur serialiser already created (in step 4 & 5)
- now we need to map the view we just created to a specific url. (basically specific a way for us to call the view we just created). we first go to django_app and add a line to include the file 'listings/urls.py'. in this 'listings/urls.py' file we map our view to a specific url (api/listings)
- finally we add the framework rest_framework in our apps as we did at the beginning with the app we created
- now when we go to http://127.0.0.1:8000/api/listings/ we can create/view all the elements in our model.
