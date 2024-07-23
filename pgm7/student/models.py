# student/models.py

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    students = models.ManyToManyField(Student, related_name='courses')

    def __str__(self):
        return self.title
    
class Project(models.Model):
    topic=models.CharField(max_length=70)
    language_used=models.CharField(max_length=200)
    duration=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.topic
