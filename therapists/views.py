from rest_framework import viewsets, permissions
from .models import TherapistEntry
from .serializers import TherapistEntrySerializer

class TherapistEntryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TherapistEntry.objects.all()
    serializer_class = TherapistEntrySerializer
    permission_classes = [permissions.IsAuthenticated] 
