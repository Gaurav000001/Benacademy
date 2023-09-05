from django.urls import path
from .views import *


urlpatterns = [
    path('create/<str:course_id>/', create_assignment, name="create_assignment"),
    path('<str:student_id>/', get_student_assignments, name="get_student_assignments"),
    path('delete/<str:assignment_id>/', delete_assignment, name="delete_assignment"),
    
]