from django.urls import path
from .views import *

urlpatterns = [
    path('', get_instructors, name='get_instructors'),
    path('register/', register_instructor, name="register_instructor"),
    path('<str:instructor_id>/', get_instructor, name="get_instructor"),
    path('update/<str:instructor_id>/', update_instructor, name="update_instructor"),
    path('delete/<str:instructor_id>/', delete_instructor, name="delete_instructor"),
    
]