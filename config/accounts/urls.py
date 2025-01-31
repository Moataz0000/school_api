from django.urls import path
from .views import TeacherRegisterView


app_name = 'accounts'



urlpatterns = [
    path('teacher', TeacherRegisterView.as_view(), name='teacher_registration')
]