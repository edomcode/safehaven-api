from rest_framework import serializers
from .models import TherapistEntry

class TherapistEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TherapistEntry
        fields = ['id','name','specialization','contact_info']
