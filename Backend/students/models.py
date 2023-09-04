from django.db import models
import uuid

# Create your models here.
class Student(models.Model):
    class Meta:
        db_table = 'students'
    
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )
    MAJOR_CHOICES = (
        ('Computer Science', 'Computer Science'),
        ('Engineering', 'Engineering'),
        ('Business', 'Business'),
        # Add other majors as needed
    )

    student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    major = models.CharField(max_length=100, choices=MAJOR_CHOICES)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=10, unique=True)
    passoword = models.CharField(max_length=100)
    