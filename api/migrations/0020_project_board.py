# Generated by Django 4.0.4 on 2023-05-13 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_project_related_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='board',
            field=models.URLField(blank=True, help_text='link of the project manage board', null=True),
        ),
    ]
