from django.urls import path
from .views import *

urlpatterns = [
    path('', get_students, name='get_students'),
    path('register/', register_student, name="register_student"),
    path('<str:student_id>/', get_student, name="get_student"),
    path('update/<str:student_id>/', update_student, name="update_student"),
    path('delete/<str:student_id>/', delete_student, name="delete_student"),
    
]
