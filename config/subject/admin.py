from django.contrib import admin
from .models import Subject, Course, Module, Content

# ✅ Inline for Module (display modules inside Course)
class ModuleInline(admin.TabularInline):  # Or use `StackedInline`
    model = Module
    extra = 1  # Number of empty forms

# ✅ Inline for Content (display content inside Module)
class ContentInline(admin.TabularInline):
    model = Content
    extra = 1

# ✅ Subject Admin
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_active')  # Show in list
    list_filter = ('is_active', 'created_at')  # Add filters
    search_fields = ('title',)  # Search by title
    ordering = ('-created_at',)
    fieldsets = (
        ("Basic Info", {"fields": ("title", "is_active")}),
        ("Timestamps", {"fields": ("created_at",)}),
    )

# ✅ Course Admin (with inline modules)
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
    inlines = [ModuleInline]  # ✅ Show modules inside courses

# ✅ Module Admin (with inline content)
@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'created_at')
    search_fields = ('name',)
    list_filter = ('course', 'created_at')
    ordering = ('-created_at',)
    inlines = [ContentInline]  # ✅ Show content inside modules

# ✅ Content Admin
@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('module', 'created_at')
    search_fields = ('module__name',)
    ordering = ('-created_at',)
