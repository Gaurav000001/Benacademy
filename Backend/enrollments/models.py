import uuid
from django.db import models

from courses.models import Course
from students.models import Student

# This model will work as Batch

class Enrollment(models.Model):
    class Meta:
        db_table = 'enrollments'
        
    enrollment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)