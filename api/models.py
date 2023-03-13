from django.db import models
from django.contrib.auth.models import AbstractUser


class Badge (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    name = models.CharField(max_length=50, unique=True)
    badge_link = models.URLField (max_length=200)
    redirect_link = models.URLField (max_length=200)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Badges"
        
class Tool (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    name = models.CharField(max_length=50, unique=True)
    version = models.CharField(max_length=20)
    image = models.URLField (max_length=200)
    
    def __str__(self):
        return f"{self.name} ({self.version})"

    class Meta:
        verbose_name_plural = "Tools"
        
class Command (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    name = models.CharField(max_length=50, unique=True)
    command = models.TextField()
    details = models.TextField()
    
    def __str__(self):
        return f"{self.name} ({self.version})"

    class Meta:
        verbose_name_plural = "Tools"

class User (AbstractUser):
    web_page = models.URLField (max_length=200, blank=True)
    
class UserBadge (models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE) 
