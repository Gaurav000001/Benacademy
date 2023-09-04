from django.urls import path
from .views import *

urlpatterns = [
    path('departments/', get_departments, name='get_departments'),
    path('departments/create/', create_department, name="create_department"),
    path('departments/<str:department_id>/', get_department, name="get_department"),
    path('departments/update/<str:department_id>/', update_department, name="update_department"),
    path('departments/delete/<str:department_id>/', delete_department, name="delete_department"),
    
]