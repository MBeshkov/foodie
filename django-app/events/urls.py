from django.urls import path
from . import views
from rest_framework import routers
from .api import EventViewSet

#router = routers.DefaultRouter()
#router.register('api/listings', ListingViewSet, 'listings')

#urlpatterns = router.urls

urlpatterns = [
    path('', views.EventListAPIView.as_view(), name='events_list'),
    path('<int:id>/', views.EventRetrieveAPIView.as_view(), name='eventss_detail'),
    path('create/', views.EventCreateAPIView.as_view(), name='events_create'),
    path('update/<int:id>/', views.EventRetrieveUpdateAPIView.as_view(), name='events_update'),
    path('delete/<int:id>/', views.EventDestroyAPIView.as_view(), name='events_delete'),
]