import uuid
from django.db import models
from courses.models import Course

from instructors.models import Instructor

# Create your models here.
class Department(models.Model):
    class Meta:
        db_table = 'departments'
        
    department_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    parent_department = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    courses = models.ManyToManyField(Course, related_name='departments')
    instructors = models.ManyToManyField(Instructor, related_name='departments')