from django.test import TestCase
from ..models import Event
from users.models import CustomUser

class EventTest(TestCase):

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

    def test_event_str(self):
        event_communal = Event.objects.get(event_name='Philosophy Society CookUp')
        event_class = Event.objects.get(event_name='Bruce demo')
        self.assertEqual(
            event_communal.get_test(), "Philosophy Society CookUp which is a cmn")
        self.assertEqual(
            event_class.get_test(), "Bruce demo which is a cng")