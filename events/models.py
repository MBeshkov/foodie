from django.db import models

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
    location = models.CharField(max_length=100, null=True)
    details = models.TextField(null=True, verbose_name="Tell us more about the event")
    created_at = models.DateTimeField(auto_now_add=True)
    vegetarian = models.BooleanField(null=True)
    vegan = models.BooleanField()
    username = models.CharField(max_length=25)
