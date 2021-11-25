from rest_framework import serializers
from .models import Event
from .models import Image
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model

class EventListSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['id', 'event_name', 'category', 'logo_image', 'absolute_url']

    def get_absolute_url(self, obj):
        return reverse('listings_detail', args=(obj.pk,))

class ImageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        fields = ['id','image', 'image_title', 'uploded_at']
        model = Image        

class EventDetailSerializer(serializers.ModelSerializer):
    update = serializers.SerializerMethodField()
    delete = serializers.SerializerMethodField()
    event_images = ImageSerializer(many=True,required=False)

    class Meta:
        model = Event
        fields = ['id', 'event_name', 'category', 'logo_image', 'location', 'details', 'created_at', 'vegetarian', 'vegan', 'update', 'delete', 'event_images']

    def get_update(self, obj):
        return reverse('events_update', args=(obj.pk,))

    def get_delete(self, obj):
        return reverse('events_delete', args=(obj.pk,))

