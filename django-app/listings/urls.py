from django.urls import path
from . import views
from rest_framework import routers
from .api import ListingViewSet
from .views import UserCreateView

#router = routers.DefaultRouter()
#router.register('api/listings', ListingViewSet, 'listings')

#urlpatterns = router.urls

urlpatterns = [
    path('', views.ListingListAPIView.as_view(), name='listings_list'),
    path('<int:id>/', views.ListingRetrieveAPIView.as_view(), name='listings_detail'),
    path('create/', views.ListingCreateAPIView.as_view(), name='listings_create'),
    path('update/<int:id>/', views.ListingRetrieveUpdateAPIView.as_view(), name='listings_update'),
    path('delete/<int:id>/', views.ListingDestroyAPIView.as_view(), name='listings_delete'),
    #path('register/', UserCreateView.as_view(), name="create_user")
]