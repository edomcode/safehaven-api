from rest_framework import serializers
from .models import GroundingEntry

class GroundingEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = GroundingEntry
        fields = ['id','activity_type','impact','impact']
