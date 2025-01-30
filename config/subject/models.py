from django.db import models
from django.utils import timezone
from .choices import SubjectChoices
from accounts.models import Student, Teacher, User


class Base(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    is_active  = models.BooleanField(default=True) 
    
    class Meta:
        abstract = True
        
        
class Subject(Base):
    title = models.CharField(max_length=50, unique=True)
    
    class Meta:
        ordering = ['-created_at']
        db_table = 'Subject'
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['-created_at'])
        ]
    
    def __str__(self):
        return self.title
    


    
class Course(Base):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='courses')
    student = models.ManyToManyField(Student, related_name='courses')
    teacher = models.ManyToManyField(Teacher, related_name='courses')
    title = models.CharField(max_length=255, unique=True, help_text='The course name must be unique.')
    total_hour = models.PositiveIntegerField()
    
    class Meta:
        ordering = ['-created_at']
        db_table = 'Course'
        indexes = [
            models.Index(
                fields=['title', 'created_at']
            )
        ]
        constraints = [
            models.UniqueConstraint(fields=['title'], name='unique_course_name')
        ]
    
    def __str__(self):
        return f'{self.subject.title} - {self.title}'
    
    
    

class Module(Base):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')

    def __str__(self):
        return self.name
    
    
class Content(Base):
    module = models.OneToOneField(Module, on_delete=models.CASCADE, related_name='contents')
    content = models.TextField()
    file = models.FileField(upload_to='contents/', blank=True, null=True)
    image = models.ImageField(upload_to='contents/', blank=True, null=True)
    
    
    def __str__(self):
        return self.module.name
    