from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TherapistEntryViewSet

router = DefaultRouter()
router.register(r'entries', TherapistEntryViewSet, basename='TherapistEntry')

urlpatterns = [
    path('', include(router.urls)),
]