# Generated by Django 4.0.4 on 2023-03-28 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_tag_redirect_alter_tool_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='media',
            old_name='link',
            new_name='source',
        ),
    ]
