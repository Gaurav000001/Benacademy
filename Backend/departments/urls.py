from django.urls import path
from .views import *

urlpatterns = [
    path('', get_departments, name='get_departments'),
    path('create/', create_department, name="create_department"),
    path('<str:department_id>/', get_department, name="get_department"),
    path('update/<str:department_id>/', update_department, name="update_department"),
    path('delete/<str:department_id>/', delete_department, name="delete_department"),
    
]