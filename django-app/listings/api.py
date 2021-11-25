from rest_framework.decorators import permission_classes
from .models import Listing
from .serializers import ListingListSerializer
from rest_framework import generics, viewsets, permissions

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ListingListSerializer