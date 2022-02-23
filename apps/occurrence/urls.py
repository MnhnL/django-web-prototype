from django.urls import path, include

from .views import OccurrenceListView

app_name = 'occurrence'
urlpatterns = [
    path('', OccurrenceListView.as_view(), name='index')
]
