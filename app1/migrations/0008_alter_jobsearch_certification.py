# Generated by Django 4.2 on 2023-09-12 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_remove_jobsearch_education_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobsearch',
            name='certification',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
