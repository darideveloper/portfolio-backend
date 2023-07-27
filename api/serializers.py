from django.contrib.auth.models import Group
from . import models
from rest_framework import serializers

class TagSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Tag
        fields = [
            'id', 
            'name', 
            'details'
        ]

class ContactSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Contact
        fields = [
            'id', 
            'name', 
            'image', 
            'svg',
            'redirect', 
        ]

class ToolSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Tool
        fields = [
            'id', 
            'name', 
            'image'
        ]
        
class MediaSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Media
        fields = [
            'id', 
            'name', 
            'source', 
            'project', 
            'media_type'
        ]
  
class ProjectSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Project
        fields = [
            'id', 
            'name', 
            'start_date', 
            'last_update', 
            'logo',
            'web_page', 
            'description', 
            'details', 
            'repo', 
            'license',
            'tags', 
            'tools', 
            'install', 
            'run', 
            'build',
            'test',
            'deploy',
            'roadmap'
        ]