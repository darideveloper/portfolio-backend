# Generated by Django 4.0.4 on 2023-03-24 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_project_web_page_alter_project_last_update'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='commands',
            new_name='build',
        ),
        migrations.AddField(
            model_name='project',
            name='deploy',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='install',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='run',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='test',
            field=models.TextField(null=True),
        ),
    ]