
from rest_framework import serializers
from .models import AffirmationEntry

class AffirmationEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AffirmationEntry
        fields = ['id','quote','author','date']
