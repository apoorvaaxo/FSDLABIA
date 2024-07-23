# student/urls.py

from django.urls import path
from .views import register_student, create_course, project_registration, student_list, course_list, course_detail,project_list

urlpatterns = [
    path('register_student/', register_student, name='register_student'),
    path('create_course/', create_course, name='create_course'),
    path('projectregister/', project_registration, name='project_registration'),
    path('projectslist/', project_list, name='project_list'),
    path('students/', student_list, name='student_list'),
    path('courses/', course_list, name='course_list'),
    path('courses/<int:course_id>/', course_detail, name='course_detail'),
]
