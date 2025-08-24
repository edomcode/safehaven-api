from rest_framework import serializers
from .models import CommunityPost

class CommunityPostSerializer(serializers.ModelSerializer):

    author_name = serializers.CharField(source='user.username', read_only=True, allow_null=True)

    class Meta:
        model = CommunityPost
        
        fields = ['id', 'author_name', 'message', 'created_at']

        read_only_fields = ['id', 'author_name', 'created_at']

    def to_representation(self, instance):
      
        representation = super().to_representation(instance)
        if representation['author_name'] is None:
            representation['author_name'] = 'Anonymous'
        return representation