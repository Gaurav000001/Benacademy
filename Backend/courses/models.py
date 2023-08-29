import uuid
from django.db import models

from instructors.models import Instructor

# Create your models here.
class Course(models.Model):
    class Meta:
        db_table = 'courses'
        
        
    course_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_code = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    credits = models.PositiveIntegerField()
    description = models.TextField()
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True)