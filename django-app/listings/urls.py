from django.urls import path
from django.conf.urls import url
from . import views
from rest_framework import routers

#router = routers.DefaultRouter()
#router.register('api/listings', ListingViewSet, 'listings')

#urlpatterns = router.urls

urlpatterns = [
    path('', views.ListingListAPIView.as_view(), name='listings_list'),
    path('<int:id>/', views.ListingRetrieveAPIView.as_view(), name='listings_detail'),
    path('create/', views.ListingCreateAPIView.as_view(), name='listings_create'),
    path('update/<int:id>/', views.ListingRetrieveUpdateAPIView.as_view(), name='listings_update'),
    path('delete/<int:id>/', views.ListingDestroyAPIView.as_view(), name='listings_delete'),
    path('search/', views.ListingListSearchFilter.as_view(), name='listings_search'),
    url(
        r'listings/(?P<pk>[0-9]+)$',
        views.get_delete_update_listing,
        name='get_delete_update_listing'
    ),
    url(
        r'listings/$',
        views.get_post_listings,
        name='get_post_listings'
    )
]