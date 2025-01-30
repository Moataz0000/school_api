from django.urls import path
from .views import (
    SubjectListView,
)

app_name = 'subjects'


urlpatterns = [
    path('subjects', SubjectListView.as_view(), name='subjects')
]