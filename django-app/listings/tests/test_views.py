import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Listing
from ..serializers import ListingListSerializer, ListingDetailSerializer
from users.models import CustomUser


# initialize the APIClient app
client = Client()

class GetAllListingsTest(TestCase):
    
    def setUp(self):
        Listing.objects.create(
            product_name = 'Cashew', 
            category = 'nts', 
            logo_image = 'blank', 
            details = "Lidl branded", 
            created_at = "2021-11-25T03:18:58.402791Z", 
            vegetarian = True, 
            vegan = True, 
            author = CustomUser.objects.create(email='foo2@bar', password = 'bar'))
        Listing.objects.create(
            product_name = 'Pringles', 
            category = 'snk', 
            logo_image = "blank", 
            details = "A promotional bundle of 5", 
            created_at = "2021-11-25T03:17:58.402791Z", 
            vegetarian = True, 
            vegan = False, 
            author = CustomUser.objects.create(email='foo@bar', password = 'bar'))

    def test_get_all_listings(self):
        # get API response
        response = client.get(reverse('get_post_listings'))
        # get data from db
        listings = Listing.objects.all()
        serializer = ListingListSerializer(listings, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)