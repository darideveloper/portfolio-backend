from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Tag (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    name = models.CharField(max_length=50, unique=True, help_text="tag name")
    details = models.TextField (max_length=200, help_text="tag details", blank=True)
    image = models.URLField (max_length=200, help_text="link of the tag image", blank=True)
    redirect = models.URLField (max_length=200, help_text="link where the tag redirects", blank=True)
    
    def __str__(self):
        if self.redirect:
            return f"{self.name} ({self.redirect})"
        else:
            return f"{self.name}"
            

class Contact (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    name = models.CharField(max_length=50, unique=True, help_text="contact element name")
    image = models.URLField (max_length=200, help_text="link of the contact element image", blank=True)
    redirect = models.TextField (max_length=200, help_text="link where the contact element redirects")
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='from user', null=True)
    
    def __str__(self):
        if self.redirect:
            return f"{self.name} ({self.redirect})"
        else:
            return f"{self.name}"
        
class Tool (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    name = models.CharField(max_length=50, help_text="tool name")
    version = models.CharField(max_length=20, help_text="tool version (e.g. 1.2.5)", blank=True)
    image = models.URLField (max_length=200, null=True, help_text="link of the tool image")
    redirect = models.URLField (max_length=200, help_text="official page or docs of the tool", blank=True, null=True)
    
    def save (self, *args, **kwargs):
        """ Overwrite Save the model for validate unique name + version"""
        
        tool_found = Tool.objects.filter(name=self.name, version=self.version)
        if tool_found.exists():
            raise ValueError("Tool with same name and version already exists")
        else:
            super(Tool, self).save(*args, **kwargs)
    
    def __str__(self):
        if self.version:
            return f"{self.name} ({self.version})"
        else:
            return f"{self.name}"

class Media (models.Model):
    CHOICES = [
        ("video", "Video"),
        ("image", "Image"),
    ]
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    name = models.CharField(max_length=80, help_text="media name")
    source = models.URLField(max_length=200, help_text='link of the media source')
    project = models.ForeignKey('Project', on_delete=models.CASCADE, help_text='from project')
    media_type = models.CharField(max_length=10, choices=CHOICES, default="image", help_text="media type")
    
    def __str__(self):
        return f"{self.name} - {self.project}"

class Project (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    name = models.CharField(max_length=80, unique=True, help_text="project name")
    start_date = models.DateField(default=timezone.now, help_text="project start date")
    last_update = models.DateField(auto_now_add=True, help_text="project last update date")
    logo = models.URLField(max_length=200, null=True, blank=True, help_text="link of the project logo")
    web_page = models.URLField(max_length=200, null=True, blank=True, help_text="link of the project web page")
    repo = models.URLField(max_length=200, null=True, blank=True, help_text="link of the project repository")
    license = models.CharField(max_length=20, default='MIT', help_text="project license name (e.g. MIT, GPL-3.0, etc.)")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, help_text="project owner")
    tags = models.ManyToManyField(Tag, help_text="project tags")
    tools = models.ManyToManyField(Tool, help_text="project tools")
    description = models.TextField(default="")
    details = models.TextField(blank=True, null=True)
    install = models.TextField(null=True, blank=True)
    settings = models.TextField(null=True, blank=True)
    run = models.TextField(null=True, blank=True)
    build = models.TextField(null=True, blank=True)
    test = models.TextField(null=True, blank=True)
    deploy = models.TextField(null=True, blank=True)
    roadmap = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name}"
    

    