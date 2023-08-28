from django.urls import path
from .views import *

urlpatterns = [
    path('students/', get_students, name='get_students'),
    path('students/register/', register_student, name="register_student"),
    path('students/<str:student_id>/', get_student, name="get_student"),
    path('students/update/<str:student_id>/', update_student, name="update_student"),
    path('students/delete/<str:student_id>/', delete_student, name="delete_student"),
    
]
