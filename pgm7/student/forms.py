# student/forms.py

from django import forms
from .models import Student, Course, Project

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'students']

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields=['topic' , 'language_used' , 'duration']
        widgets = {
            'topic': forms.TextInput(attrs={'class': 'form-control'}),
            'languages_used': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
        }
