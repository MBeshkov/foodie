from django.db import models
from django.conf import settings

# Create your models here.
class Event(models.Model):
    communal_cooking = 'cmn'
    meet_swap = 'swp'
    cooking_class = 'cng'

    tag_choices = [
        (communal_cooking, 'Communal Cooking'),
        (meet_swap, 'Mass swap'),
        (cooking_class, 'Cooking Class'),
    ]
    event_name = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=3, choices=tag_choices, default=communal_cooking)
    logo_image = models.ImageField(upload_to='eventImages', blank=True, default="eventImages/default.jpg")
    location = models.CharField(max_length=100, null=True)
    details = models.TextField(null=True, verbose_name="Tell us more about the event")
    created_at = models.DateTimeField(auto_now_add=True)
    vegetarian = models.BooleanField(null=True)
    vegan = models.BooleanField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='events', null=True)

    def __str__(self):

        return "{}. {}".format(self.event_name, self.category)

    def get_test(self):
        return self.event_name + ' which is a ' + self.category

class Image(models.Model):
	listing = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_images',blank=True, null=True)
	image = models.ImageField(upload_to='eventImages',blank=True)
	image_title = models.CharField(max_length=120, blank=True)
	uploded_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-uploded_at']

