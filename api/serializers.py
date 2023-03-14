from django.contrib.auth.models import Group
from . import models
from rest_framework import serializers

class BadgeSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Badge
        fields = ['name', 'badge_link', 'redirect_link']

class ToolSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Tool
        fields = ['name', 'version', 'image']
        
class CommandSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Command
        fields = ['name', 'command', 'details']
        
class RoadMapSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.RoadMap
        fields = ['name']
  
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = ['web_page', 'username', 'email', 'first_name', 'last_name', 'password', 'is_staff', 'is_active', 'date_joined', 'last_login', 'is_superuser', 'groups']
        
class UserBadgeSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.UserBadge
        fields = ['user', 'badge']
        
class ProjectSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Project
        fields = ['name', 'start_date', 'last_update', 'logo', 'desciption', 'details']
        
class ProjectBadgeSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ProjectBadge
        fields = ['project', 'badge']
        
class ProjectToolSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ProjectTool
        fields = ['project', 'tool']
        
class ProjectCommandSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ProjectCommand
        fields = ['project', 'command', 'tool', 'step', 'command_type']
        
class ProjectRoadMapSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ProjectRoadMap
        fields = ['project', 'road_map', 'done']
        
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['name']