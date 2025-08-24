from rest_framework import viewsets, permissions
from .models import GratitudeEntry
from .serializers import GratitudeEntrySerializer

class GratitudeEntryViewSet(viewsets.ModelViewSet):
  
    serializer_class = GratitudeEntrySerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        return GratitudeEntry.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
    
        serializer.save(user=self.request.user)
