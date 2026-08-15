from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        # Users can only view their own events
        return Event.objects.filter(owner=self.request.user).order_by('target_date')

    def perform_create(self, serializer):
        # Automatically assign logged-in user as owner
        serializer.save(owner=self.request.user)
