from .models import Listing
from .serializers import ListingListSerializer, ListingDetailSerializer
from rest_framework import generics
from rest_framework import filters
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class ListingUserWritePermission(BasePermission):
    message = 'Editing listings is restricted to the author only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user

class ListingListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Listing.objects.all()
    serializer_class = ListingListSerializer

class ListingRetrieveAPIView(generics.RetrieveAPIView, ListingUserWritePermission):
    permission_classes = [ListingUserWritePermission]
    lookup_field = "id"
    queryset = Listing.objects.all()
    serializer_class = ListingDetailSerializer

class ListingCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Listing.objects.all()
    serializer_class = ListingDetailSerializer


class ListingRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView, ListingUserWritePermission):
    permission_classes = [ListingUserWritePermission]
    lookup_field = "id"
    queryset = Listing.objects.all()
    serializer_class = ListingDetailSerializer

class ListingDestroyAPIView(generics.DestroyAPIView, ListingUserWritePermission):
    permission_classes = [ListingUserWritePermission]
    lookup_field = "id"
    queryset = Listing.objects.all()

class ListingListSearchFilter(generics.ListAPIView):

    queryset = Listing.objects.all()
    serializer_class = ListingListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['$product_name', '$category']


# everything below is only needed for testing

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_listing(request, pk):
    try:
        listing = Listing.objects.get(pk=pk)
    except Listing.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single listing
    if request.method == 'GET':
        serializer = ListingListSerializer(listing)
        return Response(serializer.data)

    # update details of a single listing
    if request.method == 'PUT':
        serializer = ListingListSerializer(listing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete a single listing
    if request.method == 'DELETE':
        listing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def get_post_listings(request):
    # get all listings
    if request.method == 'GET':
        listings = Listing.objects.all()
        serializer = ListingListSerializer(listings, many=True)
        return Response(serializer.data)
    # insert a new record for a listing
    elif request.method == 'POST':
        return Response({})
