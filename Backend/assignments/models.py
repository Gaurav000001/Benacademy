import uuid
from django.db import models

from courses.models import Course

# Create your models here.
class Assignment(models.Model):
    class Meta:
        db_table = 'assignments'
        
    assignment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)