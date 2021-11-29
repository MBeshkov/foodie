from .models import Event
from .serializers import EventListSerializer, EventDetailSerializer
from rest_framework import generics
from rest_framework import filters
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class EventUserWritePermission(BasePermission):
    message = 'Editing events is restricted to the author only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user

class EventListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Event.objects.all()
    serializer_class = EventListSerializer

class EventRetrieveAPIView(generics.RetrieveAPIView, EventUserWritePermission):
    permission_classes = [EventUserWritePermission]
    lookup_field = "id"
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer

class EventCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer

class EventRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView, EventUserWritePermission):
    permission_classes = [EventUserWritePermission]
    lookup_field = "id"
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer

class EventDestroyAPIView(generics.DestroyAPIView, EventUserWritePermission):
    permission_classes = [EventUserWritePermission]
    lookup_field = "id"
    queryset = Event.objects.all()

class EventListSearchFilter(generics.ListAPIView):

    queryset = Event.objects.all()
    serializer_class = EventListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['$event_name', '$category']

# everything below is only needed for testing

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_event(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single event
    if request.method == 'GET':
        serializer = EventListSerializer(event)
        return Response(serializer.data)

    # update details of a single event
    if request.method == 'PUT':
        serializer = EventListSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete a single event
    if request.method == 'DELETE':
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def get_post_events(request):
    # get all events
    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventListSerializer(events, many=True)
        return Response(serializer.data)
    # insert a new record for a events
    elif request.method == 'POST':
        return Response({})


