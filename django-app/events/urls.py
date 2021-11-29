from django.urls import path
from django.conf.urls import url
from . import views
from rest_framework import routers
from .api import EventViewSet

#router = routers.DefaultRouter()
#router.register('api/listings', ListingViewSet, 'listings')

#urlpatterns = router.urls

urlpatterns = [
    path('', views.EventListAPIView.as_view(), name='events_list'),
    path('<int:id>/', views.EventRetrieveAPIView.as_view(), name='events_detail'),
    path('create/', views.EventCreateAPIView.as_view(), name='events_create'),
    path('update/<int:id>/', views.EventRetrieveUpdateAPIView.as_view(), name='events_update'),
    path('delete/<int:id>/', views.EventDestroyAPIView.as_view(), name='events_delete'),
    path('search/', views.EventListSearchFilter.as_view(), name='events_search'),
     url(
        r'events/(?P<pk>[0-9]+)$',
        views.get_delete_update_event,
        name='get_delete_update_event'
    ),
    url(
        r'events/$',
        views.get_post_events,
        name='get_post_events'
    )
]