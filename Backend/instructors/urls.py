from django.urls import path
from .views import *

urlpatterns = [
    path('instructors/', get_instructors, name='get_instructors'),
    path('instructors/register/', register_instructor, name="register_instructor"),
    path('instructors/<str:instructor_id>/', get_instructor, name="get_instructor"),
    path('instructors/update/<str:instructor_id>/', update_instructor, name="update_instructor"),
    path('instructors/delete/<str:instructor_id>/', delete_instructor, name="delete_instructor"),
    
]