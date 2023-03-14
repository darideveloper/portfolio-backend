from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Badge (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    name = models.CharField(max_length=50, unique=True)
    badge_link = models.URLField (max_length=200)
    redirect_link = models.URLField (max_length=200)
    
    def __str__(self):
        return self.name
        
class Tool (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    name = models.CharField(max_length=50, unique=True)
    version = models.CharField(max_length=20)
    image = models.FileField(upload_to='imgs/tools', null=True)
    
    def __str__(self):
        return f"{self.name} ({self.version})"
        
class Command (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    name = models.CharField(max_length=50, unique=True)
    command = models.TextField(null=True)
    details = models.TextField(null=True)
    
    def __str__(self):
        return f"{self.name} ({self.version})"
        
class RoadMap (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return f"{self.name}"

class User (AbstractUser):
    web_page = models.URLField (max_length=200, blank=True)
    
    def __str__(self):
        return f"{self.username}"
    
class UserBadge (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE) 
    
    def __str__(self):
        return f"{self.user__username} - {self.badge__name}"

class Project (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    name = models.CharField(max_length=80, unique=True)
    start_date = models.DateField(default=timezone.now)
    last_update = models.DateField(default=timezone.now)
    logo = models.FileField(upload_to='imgs/project', null=True)
    desciption = models.TextField()
    details = models.TextField()
    clone_repo = models.BooleanField(default=False)
    license = models.CharField(max_length=20, default='MIT')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.name}"

class ProjectBadge (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.project__name} - {self.badge__name}"   
    
class ProjectTool (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.project__name} - {self.tool__name}"   

class ProjectCommand (models.Model):
    CHOICES = [
        ('build', 'Build'), 
        ('test', 'Test'), 
        ('deploy', 'Deploy'),
        ('run', 'Run'),
        ('install', 'Install'),
    ]
    
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    command = models.ForeignKey(Command, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    step = models.IntegerField(default=1)
    command_type = models.CharField(
        max_length = 8,
        choices = CHOICES,
        default = 'install'    
    )
    
    def __str__(self):
        return f"{self.project__name} - {self.command__name}"   
    
    # unique "step" for each project
    def save(self, *args, **kwargs):
        if self.step is None:
            self.step = ProjectCommand.objects.filter(project=self.project).count() + 1
        super(ProjectCommand, self).save(*args, **kwargs)

class ProjectRoadMap (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    road_map = models.ForeignKey(RoadMap, on_delete=models.CASCADE)
    done = models.BooleanField(default=True)


    