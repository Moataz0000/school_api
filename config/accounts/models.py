from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from polymorphic.models import PolymorphicModel
from django.utils import timezone
from .other.model_manager import CustomUserManager
from subject.choices import ClassNumber, TeacherPosition



class User(PolymorphicModel, AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)
    
    USERNAME_FIELD = "username"
    objects = CustomUserManager()
    
    
    def __str__(self):
        return self.get_username()




class Student(User):
    class_number = models.CharField(max_length=2, choices=ClassNumber.choices)
    
    def __str__(self):
        return self.username


class Teacher(User):
    position = models.CharField(max_length=2, choices=TeacherPosition.choices)
    
    def __str__(self):
        return self.username