# Generated by Django 4.2.4 on 2023-09-05 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_student_passoword'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='passoword',
            new_name='password',
        ),
    ]
