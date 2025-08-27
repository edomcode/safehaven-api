from rest_framework import viewsets, permissions
from .models import GroundingEntry
from .serializers import GroundingEntrySerializer

class GroundingEntryViewSet(viewsets.ModelViewSet):
  
    serializer_class = GroundingEntrySerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        return GroundingEntry.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
    
        serializer.save(user=self.request.user)

