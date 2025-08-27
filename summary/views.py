from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import timedelta
from django.utils import timezone
from journal.models import JournalEntry
from mood.models import MoodEntry
from gratitude.models import GratitudeEntry
from django.db.models import Avg


class WeeklySummaryView(APIView):
    def get(self, request):
        user = request.user
        week_start = timezone.now() - timedelta(days=7)

        mood_entries = MoodEntry.objects.filter(user=user, created_at__gte=week_start)
        journal_entries = JournalEntry.objects.filter(user=user, created_at__gte=week_start)
        gratitude_entries = GratitudeEntry.objects.filter(user=user, created_at__gte=week_start)

        mood_average = mood_entries.aggregate(Avg('mood_score'))['mood_score__avg'] or 0
        journal_count = journal_entries.count()
        gratitude_count = gratitude_entries.count()

        return Response({
            "week_start": week_start.date(),
            "mood_average": round(mood_average, 2),
            "journal_count": journal_count,
            "gratitude_count": gratitude_count
        })
