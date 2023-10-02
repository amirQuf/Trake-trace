from django.urls import path, include

urlpatterns = [
   path('trace', include(('trace.urls', 'trace')))
]
