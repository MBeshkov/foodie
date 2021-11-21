from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['event_name', 'category', 'location', 'details', 'created_at', 'vegetarian', 'vegan', 'username']