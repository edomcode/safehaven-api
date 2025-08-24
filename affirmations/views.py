from rest_framework import viewsets, permissions
from .models import AffirmationEntry
from .serializers import AffirmationEntrySerializer

class AffirmationEntryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=AffirmationEntry.objects.all()
    serializer_class=AffirmationEntrySerializer
    permission_classes = [permissions.IsAuthenticated]
                          

    
