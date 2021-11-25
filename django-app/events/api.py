from rest_framework.decorators import permission_classes
from .models import Event
from .serializers import EventListSerializer
from rest_framework import generics, viewsets, permissions

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EventListSerializer