from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Tag (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    name = models.CharField(max_length=50, unique=True, help_text="tag name")
    image = models.URLField (max_length=200, help_text="link of the tag image")
    redirect = models.URLField (max_length=200, help_text="link where the tag redirects")
    
    def __str__(self):
        return f"{self.name} ({self.redirect})"

class Contact (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    name = models.CharField(max_length=50, unique=True, help_text="contact element name")
    image = models.URLField (max_length=200, help_text="link of the contact element image")
    redirect = models.TextField (max_length=200, help_text="link where the contact element redirects")
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='from user', null=True)
    
    def __str__(self):
        return f"{self.name} ({self.redirect})"
        
class Tool (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    name = models.CharField(max_length=50, unique=True, help_text="tool name")
    version = models.CharField(max_length=20, help_text="tool version (e.g. 1.2.5)")
    image = models.URLField (max_length=200, null=True, help_text="link of the tool image")
    
    def __str__(self):
        return f"{self.name} ({self.version})"

class Media (models.Model):
    CHOICES = [
        ("video", "Video"),
        ("image", "Image"),
    ]
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    name = models.CharField(max_length=80, unique=True, help_text="media name")
    link = models.URLField(max_length=200, help_text='link of the media source')
    project = models.ForeignKey('Project', on_delete=models.CASCADE, help_text='from project')
    media_type = models.CharField(max_length=10, choices=CHOICES, default="image", help_text="media type")
    
    def __str__(self):
        return f"{self.name} - {self.project} ({self.link})"

class Project (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    name = models.CharField(max_length=80, unique=True, help_text="project name")
    start_date = models.DateField(default=timezone.now, help_text="project start date")
    last_update = models.DateField(auto_now_add=True, help_text="project last update date")
    logo = models.URLField(max_length=200, null=True, blank=True, help_text="link of the project logo")
    web_page = models.URLField(max_length=200, null=True, blank=True, help_text="link of the project web page")
    description = models.TextField()
    details = models.TextField(blank=True, null=True)
    repo = models.URLField(max_length=200, null=True, blank=True, help_text="link of the project repository")
    license = models.CharField(max_length=20, default='MIT', help_text="project license name (e.g. MIT, GPL-3.0, etc.)")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, help_text="project owner")
    tags = models.ManyToManyField(Tag, help_text="project tags")
    tools = models.ManyToManyField(Tool, help_text="project tools")
    install = models.TextField(null=True, blank=True)
    run = models.TextField(null=True, blank=True)
    build = models.TextField(null=True, blank=True)
    test = models.TextField(null=True, blank=True)
    deploy = models.TextField(null=True, blank=True)
    roadmap = models.TextField(null=True, blank=True)
    
    def __str__(self):
        if self.web_page:
            return f"{self.name} ({self.web_page})"
        elif self.repo:
            return f"{self.name} ({self.repo})"
        else:
            return f"{self.name}"
    

    