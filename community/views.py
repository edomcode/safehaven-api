from rest_framework import viewsets, permissions
from .models import CommunityPost
from .serializers import CommunityPostSerializer

class CommunityPostViewSet(viewsets.ModelViewSet):
 
    queryset = CommunityPost.objects.all().order_by('-created_at') 
    serializer_class = CommunityPostSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
    
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
          
            serializer.save(user=None)