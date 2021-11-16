from django.urls import path
from . import views

urlpatterns = [
    path('api/listings/', views.ListingsListCreate.as_view() ),
]