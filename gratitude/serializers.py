from rest_framework import serializers
from .models import GratitudeEntry

class GratitudeEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = GratitudeEntry
        fields = ['id', 'message', 'category', 'created_at']
