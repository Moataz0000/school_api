from rest_framework.permissions import BasePermission
from .models import Teacher, Student
from .common.exceptions import InvalidUserTypeException
class IsTeacher(BasePermission):
    
    def has_permission(self, request, view):
        teacher = request.user.teacher
        if not isinstance(teacher, Teacher):
            return InvalidUserTypeException()
        else:
            return True