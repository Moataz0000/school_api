from django.db import models





class SubjectChoices(models.TextChoices):
    HISTORY = 'HT', 'History'
    MATH    = 'MT', 'Math'
    SCIENCE = 'SC', 'Science'
    
    


class ClassNumber(models.TextChoices):
    ONE = 'ON', 'One'
    TWO = 'TW', 'Two'
    THREE = 'TR', 'Three'
    
    

class TeacherPosition(models.TextChoices):
    MATH_TEACHER = 'MA', 'Math Teacher'
    HISTORY_TEACHER = 'HS', 'Histroy Teacher'
    SCIENCE_TEACHER = 'SC', 'Science Teacher'