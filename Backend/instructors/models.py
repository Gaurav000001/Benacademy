import uuid
from django.db import models

from departments.models import Department

# Create your models here.
class Instructor(models.Model):
    class Meta:
        db_table = 'instructors'
        
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )

    instructor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=10, unique=True)
    departments = models.ManyToManyField(Department, related_name='instructors')
    passoword = models.CharField(max_length=100)