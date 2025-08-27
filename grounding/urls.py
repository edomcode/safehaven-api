from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GroundingEntryViewSet

router = DefaultRouter()
router.register(r'entries', GroundingEntryViewSet, basename='GroundingEntry')

urlpatterns = [
    path('', include(router.urls)),
]