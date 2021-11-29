from django.test import TestCase
from ..models import Listing
from users.models import CustomUser

class ListingTest(TestCase):

    def setUp(self):
        Listing.objects.create(
            product_name = 'Cashew', 
            category = 'nts', 
            logo_image = "listingImages/default.jpg", 
            details = "Lidl branded", 
            created_at = "2021-11-25T03:18:58.402791Z", 
            vegetarian = True, 
            vegan = True, 
            author = CustomUser.objects.create(email='foo2@bar', password = 'bar')
        )
        Listing.objects.create(
            product_name = 'Pringles', 
            category = 'snk', 
            logo_image = "listingImages/default.jpg", 
            details = "A promotional bundle of 5", 
            created_at = "2021-11-25T03:17:58.402791Z", 
            vegetarian = True, 
            vegan = False, 
            author = CustomUser.objects.create(email='foo@bar', password = 'bar')
        )

    def test_listing_str(self):
        listing_cashew = Listing.objects.get(product_name='Cashew')
        listing_pringles = Listing.objects.get(product_name='Pringles')
        self.assertEqual(
            listing_cashew.get_test(), "Cashew which is a nts")
        self.assertEqual(
            listing_pringles.get_test(), "Pringles which is a snk")