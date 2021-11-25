from .models import Event
from .serializers import EventListSerializer, EventDetailSerializer
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework import permissions


class EventListAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer

class EventRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer

class EventCreateAPIView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer

class EventRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = "id"
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer

class EventDestroyAPIView(generics.DestroyAPIView):
    lookup_field = "id"
    queryset = Event.objects.all()