
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('api/journal/', include('journal.urls')),
    path('api-auth/', include('rest_framework.urls')), 
    path('api/mood/', include('mood.urls')),
    path('api/gratitude/', include('gratitude.urls')),
    path('api/groundung/', include('grounding.urls')),
    path('api/therapists/', include('therapists.urls')), 
    path('api/affirmations/', include('affirmations.urls')), 
    path('api/community/', include('community.urls')),
    path('api/summary/', include('summary.urls')),

]
