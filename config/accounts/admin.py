from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
from .models import User, Student, Teacher


# ✅ Parent Admin (for User)
@admin.register(User)
class UserAdmin(PolymorphicParentModelAdmin, BaseUserAdmin):
    """Admin panel for the base User model (handles polymorphism)."""
    base_model = User
    child_models = [Student, Teacher]  # Specify child models explicitly
    list_display = ("username", "is_active", "is_staff", "date_joined")
    search_fields = ("username",)
    ordering = ("-date_joined",)
    list_filter = ("is_active", "is_staff", "date_joined")
    fieldsets = (
        ("User Info", {"fields": ("username", "password")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("date_joined",)}),
    )


# ✅ Child Admin (for Student)
@admin.register(Student)
class StudentAdmin(PolymorphicChildModelAdmin):
    """Admin panel for Student model."""
    base_model = Student
    list_display = ("username", "class_number", "is_active", "date_joined")
    search_fields = ("username", "class_number")
    ordering = ("-date_joined",)
    list_filter = ("class_number", "is_active")
    fieldsets = (
        ("Student Info", {"fields": ("username", "class_number")}),
        ("Permissions", {"fields": ("is_active",)}),
        ("Important Dates", {"fields": ("date_joined",)}),
    )


# ✅ Child Admin (for Teacher)
@admin.register(Teacher)
class TeacherAdmin(PolymorphicChildModelAdmin):
    """Admin panel for Teacher model."""
    base_model = Teacher
    list_display = ("username", "position", "is_active", "date_joined")
    search_fields = ("username", "position")
    ordering = ("-date_joined",)
    list_filter = ("position", "is_active")
    fieldsets = (
        ("Teacher Info", {"fields": ("username", "position")}),
        ("Permissions", {"fields": ("is_active",)}),
        ("Important Dates", {"fields": ("date_joined",)}),
    )
