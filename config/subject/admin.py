from django.contrib import admin
from .models import Subject, Course, Module, Content, Enrollment

class ModuleInline(admin.TabularInline):  
    model = Module
    extra = 1  # Number of empty forms

class ContentInline(admin.TabularInline):
    model = Content
    extra = 1


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_active')  
    list_filter = ('is_active', 'created_at')  
    search_fields = ('title',)  

    @admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_active')  
    list_filter = ('is_active', 'created_at') 
    search_fields = ('title',) 
    ordering = ('-created_at',)
    fieldsets = (
        ("Basic Info", {"fields": ("title", "is_active")}),
        ("Timestamps", {"fields": ("created_at",)}),
    )

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'total_hour', 'created_at')
    list_filter = ('subject', 'created_at')
    search_fields = ('title',)
    ordering = ('-created_at',)
    fieldsets = (
        ("Course Details", {"fields": ("title", "subject", "total_hour")}),
        ("Students & Teachers", {"fields": ("student", "teacher")}),
        ("Status", {"fields": ("is_active",)}),
    )
    inlines = [ModuleInline]  

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'created_at')
    search_fields = ('name',)
    list_filter = ('course', 'created_at')
    ordering = ('-created_at',)
    inlines = [ContentInline]  


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('module', 'created_at')
    search_fields = ('module__name',)
    ordering = ('-created_at',)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['course', 'student', 'created_at', 'is_active']