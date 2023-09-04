import uuid
from django.db import models

from assignments.models import Assignment
from students.models import Student

# Create your models here.
class Submission(models.Model):
    class Meta:
        db_table = 'submissions'
        
    STATUS_CHOICES = (
        ('Submitted', 'Submitted'),
        ('Late', 'Late'),
        ('Graded', 'Graded')
    )
        
    submission_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    submitted_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    remarks = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)