from typing import List
from django.contrib import admin
from .models import Listing
from .models import Image
# Register your models here.

admin.site.register(Listing)
admin.site.register(Image)