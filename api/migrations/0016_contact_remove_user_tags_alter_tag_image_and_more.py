# Generated by Django 4.0.4 on 2023-03-24 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_rename_redirect_link_tag_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Contact element name', max_length=50, unique=True)),
                ('image', models.URLField(help_text='Link of the contact element image')),
                ('redirect', models.URLField(help_text='Link where the contact element redirects')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='tags',
        ),
        migrations.AlterField(
            model_name='tag',
            name='image',
            field=models.URLField(help_text='Link of the tag image'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(help_text='Tag name', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='redirect',
            field=models.URLField(help_text='Link where the tag redirects'),
        ),
        migrations.AlterField(
            model_name='tool',
            name='image',
            field=models.URLField(help_text='Link of the tool image', null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='name',
            field=models.CharField(help_text='Tool name', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='version',
            field=models.CharField(help_text='Tool version (e.g. 1.2.5)', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='web_page',
            field=models.URLField(blank=True, help_text="Link to the user's web page"),
        ),
        migrations.AddField(
            model_name='user',
            name='contacts',
            field=models.ManyToManyField(help_text='Contact information of the user', to='api.contact'),
        ),
    ]