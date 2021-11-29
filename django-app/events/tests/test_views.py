import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Event
from ..serializers import EventListSerializer, EventDetailSerializer
from users.models import CustomUser


# initialize the APIClient app
client = Client()

class GetAllEventsTest(TestCase):
    
    def setUp(self):
        Event.objects.create(
            event_name = 'Philosophy Society CookUp', 
            category = 'cmn', 
            logo_image = "listingImages/default.jpg", 
            location = "Hillhead",
            details = "Lorem Ipsum", 
            created_at = "2021-11-25T03:18:38.402791Z", 
            vegetarian = False, 
            vegan = False, 
            author = CustomUser.objects.create(email='foo2@bar', password = 'bar')
        )
        Event.objects.create(
            event_name = 'Bruce demo', 
            category = 'cng', 
            logo_image = "listingImages/default.jpg", 
            location = "Meston",
            details = "Bruce's cooking class", 
            created_at = "2021-11-25T03:17:58.402791Z", 
            vegetarian = True, 
            vegan = False, 
            author = CustomUser.objects.create(email='foo@bar', password = 'bar')
        )

    def test_get_all_events(self):
        # get API response
        response = client.get(reverse('get_post_events'))
        # get data from db
        events = Event.objects.all()
        serializer = EventListSerializer(events, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)