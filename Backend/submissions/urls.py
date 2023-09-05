from django.urls import path
from .views import *


urlpatterns = [
    path('<str:assignment_id>/<str:student_id>/', create_submission, name='create_submission'),
    
]