# Generated by Django 4.2 on 2023-09-11 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_jobsearch'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobpost',
            old_name='skill',
            new_name='Education',
        ),
        migrations.RenameField(
            model_name='jobsearch',
            old_name='skill',
            new_name='Education',
        ),
    ]