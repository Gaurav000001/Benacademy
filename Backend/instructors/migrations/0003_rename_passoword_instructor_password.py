# Generated by Django 4.2.4 on 2023-09-05 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0002_alter_instructor_passoword'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instructor',
            old_name='passoword',
            new_name='password',
        ),
    ]