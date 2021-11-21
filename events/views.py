from .models import Event
from .serializers import EventSerializer
from rest_framework import generics


class EventsEventCreate(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

