from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GratitudeEntryViewSet

router = DefaultRouter()
router.register(r'entries', GratitudeEntryViewSet, basename='GratitudeEntry')

urlpatterns = [
    path('', include(router.urls)),
]