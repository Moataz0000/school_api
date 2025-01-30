from django.urls import path
from .views import (
    SubjectListView,
    SubjectUpdateRetrieve,
)

app_name = 'subjects'


urlpatterns = [
    path('subjects', SubjectListView.as_view(), name='subjects'),
    path('subjects/<int:id>', SubjectUpdateRetrieve.as_view(), name='update_retrieve')
]