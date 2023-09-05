from django.urls import path
from .views import *


urlpatterns = [
    path('', get_all_courses, name='get_all_courses'),
    path('create/<str:department_id>/', create_course, name="create_course"),
    path('<str:student_id>/', get_student_courses, name="get_student_courses"),
    path('update/<str:course_id>/<str:instructor_id>/', change_course_instructor, name="change_course_instructor"),
    path('delete/<str:course_id>/', delete_course, name="delete_course"),
    
]