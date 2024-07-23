# student/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course, Project
from .forms import StudentForm, CourseForm, ProjectForm

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student/register_student.html', {'form': form})

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'student/create_course.html', {'form': form})

def project_registration(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_registration')
    else:
        form = ProjectForm()
    return render(request, 'student/project_registration.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'student/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'student/course_detail.html', {'course': course})
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'student/project_list.html', {'projects': projects})
