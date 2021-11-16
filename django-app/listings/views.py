from .models import Listing
from .serializers import ListingSerializer
from rest_framework import generics

class ListingsListCreate(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

