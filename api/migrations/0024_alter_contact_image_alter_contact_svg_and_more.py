# Generated by Django 4.0.4 on 2023-07-30 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_alter_project_name_alter_tool_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='image',
            field=models.URLField(blank=True, help_text='link of the contact element image', max_length=600),
        ),
        migrations.AlterField(
            model_name='contact',
            name='svg',
            field=models.URLField(blank=True, help_text='link of the contact element image (in svg format)', max_length=600),
        ),
        migrations.AlterField(
            model_name='media',
            name='source',
            field=models.URLField(help_text='link of the media source', max_length=600),
        ),
        migrations.AlterField(
            model_name='project',
            name='board',
            field=models.URLField(blank=True, help_text='link of the project manage board', max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='logo',
            field=models.URLField(blank=True, help_text='link of the project logo', max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='repo',
            field=models.URLField(blank=True, help_text='link of the project repository', max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='web_page',
            field=models.URLField(blank=True, help_text='link of the project web page', max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='image',
            field=models.URLField(help_text='link of the tool image', max_length=600, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='redirect',
            field=models.URLField(blank=True, help_text='official page or docs of the tool', max_length=600, null=True),
        ),
    ]
