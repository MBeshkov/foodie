from .models import Listing
from .serializers import (ListingListSerializer, ListingDetailSerializer, UserSerializer)
from rest_framework import generics
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import permissions


class ListingListAPIView(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingListSerializer

class ListingRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Listing.objects.all()
    serializer_class = ListingDetailSerializer

class ListingCreateAPIView(generics.CreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingDetailSerializer

class ListingRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = "id"
    queryset = Listing.objects.all()
    serializer_class = ListingDetailSerializer

class ListingDestroyAPIView(generics.DestroyAPIView):
    lookup_field = "id"
    queryset = Listing.objects.all()

class UserCreateView(generics.CreateAPIView):
 model = get_user_model()
 permission_classes = [permissions.AllowAny]
 serializer_class = UserSerializer