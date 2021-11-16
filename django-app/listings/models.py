from django.db import models

# Create your models here.
class Listing(models.Model):
    name = models.CharField(max_length=35)
    created_at = models.DateTimeField(auto_now_add=True)
    vegan = models.BooleanField()
    username = models.CharField(max_length=25)

