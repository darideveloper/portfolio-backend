from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Tag (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    name = models.CharField(max_length=50, unique=True)
    image = models.URLField (max_length=200)
    redirect = models.URLField (max_length=200)
    
    def __str__(self):
        return self.name
        
class Tool (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    name = models.CharField(max_length=50, unique=True)
    version = models.CharField(max_length=20)
    image = models.URLField (max_length=200, null=True)
    
    def __str__(self):
        return f"{self.name} ({self.version})"
        
class User (AbstractUser):
    web_page = models.URLField (max_length=200, blank=True)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return f"{self.username}"

class Media (models.Model):
    CHOICES = [
        ("video", "Video"),
        ("image", "Image"),
    ]
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    name = models.CharField(max_length=80, unique=True)
    link = models.URLField(max_length=200)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    media_type = models.CharField(max_length=10, choices=CHOICES, default="image")
    
    def __str__(self):
        return f"{self.name} - {self.project} ({self.link})"

class Project (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    name = models.CharField(max_length=80, unique=True)
    start_date = models.DateField(default=timezone.now)
    last_update = models.DateField(auto_now_add=True)
    logo = models.URLField(max_length=200, null=True)
    description = models.TextField()
    details = models.TextField()
    repo = models.URLField(max_length=200, null=True)
    clone_repo = models.BooleanField(default=False)
    license = models.CharField(max_length=20, default='MIT')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)
    tools = models.ManyToManyField(Tool)
    install = models.TextField(null=True)
    run = models.TextField(null=True)
    build = models.TextField(null=True)
    test = models.TextField(null=True)
    deploy = models.TextField(null=True)
    roadmap = models.TextField(null=True)
    web_page = models.URLField(max_length=200, null=True)
    
    def __str__(self):
        if self.web_page:
            return f"{self.name} ({self.web_page})"
        else:
            return f"{self.name} ({self.repo})"
    

    