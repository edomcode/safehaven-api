from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AffirmationEntryViewSet

router = DefaultRouter()
router.register(r'entries', AffirmationEntryViewSet, basename='AffirmationEntry')

urlpatterns = [
    path('', include(router.urls)),
]