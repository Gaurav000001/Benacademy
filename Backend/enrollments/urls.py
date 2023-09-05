from django.urls import path
from .views import *


urlpatterns = [
    path('enroll/<str:student_id>/<str:course_id>/', enroll_student_to_course, name='enroll_student_to_course'),
    path('enroll/<str:course_id>/', bulk_enrollment, name="bulk_enrollment"),
    
]