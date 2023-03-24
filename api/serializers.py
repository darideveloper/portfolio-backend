from django.contrib.auth.models import Group
from . import models
from rest_framework import serializers

class TagSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Tag
        fields = ['name', 'tag_link', 'redirect_link']

class ToolSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Tool
        fields = ['name', 'version', 'image']
  
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = ['web_page', 'username', 'email', 'first_name', 'last_name', 'password', 'is_staff', 'is_active', 'date_joined', 'last_login', 'is_superuser', 'groups']
        
class ProjectSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Project
        fields = ['name', 'start_date', 'last_update', 'logo', 'desciption', 'details']
        
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['name']