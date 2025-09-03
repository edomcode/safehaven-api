from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import JournalEntry


class JournalEntryTests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="eden", password="testpass123")
        self.client.login(username="eden", password="testpass123")
        self.list_url = reverse("journalentry-list")  # from your urls.py router

    def test_create_journal_entry(self):
        """Test creating a journal entry through the API"""
        data = {"content": "My first test entry", "emotion_tags": "happy"}
        response = self.client.post(self.list_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JournalEntry.objects.count(), 1)
        self.assertEqual(JournalEntry.objects.first().content, "My first test entry")

    def test_list_journal_entries(self):
        """Test listing journal entries"""
        JournalEntry.objects.create(user=self.user, content="Entry 1", emotion_tags="hopeful")
        JournalEntry.objects.create(user=self.user, content="Entry 2", emotion_tags="anxious")

        response = self.client.get(self.list_url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
