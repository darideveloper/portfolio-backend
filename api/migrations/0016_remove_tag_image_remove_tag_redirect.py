# Generated by Django 4.0.4 on 2023-05-10 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_project_project_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='image',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='redirect',
        ),
    ]
