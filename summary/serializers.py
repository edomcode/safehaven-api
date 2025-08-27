
from rest_framework import serializers
from .models import WeeklySummary

class WeeklySummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklySummary
        fields = ['week_start', 'mood_average', 'gratitude_count', 'journal_count']