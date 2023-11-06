from . import models
from rest_framework import serializers

class ProjectSummarySerializer (serializers.ModelSerializer):
    """ Extra serializer for project summary """    
    
    class Meta:
        model = models.Project
        fields = [
            'id', 
            'name', 
            'last_update', 
            'logo',
            'web_page',
            'repo', 
            'description',
            'is_done'
        ]
        
class MediaSummarySerializer (serializers.ModelSerializer):
    """ Extra serializer for media summary """    
    
    class Meta:
        model = models.Media
        fields = [
            'id', 
            'name', 
            'source', 
            'media_type',
        ]

class TagSerializer (serializers.ModelSerializer):
    """ Tag model serializer """
    class Meta:
        model = models.Tag
        fields = [
            'id', 
            'name', 
            'details'
        ]

class ContactSerializer (serializers.ModelSerializer):
    """ Contact model serializer """
    class Meta:
        model = models.Contact
        fields = [
            'id', 
            'name', 
            'image', 
            'svg',
            'redirect', 
        ]

class ToolSerializer (serializers.ModelSerializer):
    """ Tool model serializer """
    class Meta:
        model = models.Tool
        fields = [
            'id', 
            'name', 
            'image'
        ]
        
class MediaSerializer (serializers.ModelSerializer):
    """ Media model serializer """
    
    project = ProjectSummarySerializer(many=False, read_only=True)
    
    class Meta:
        model = models.Media
        fields = [
            'id', 
            'name', 
            'source', 
            'project', 
            'media_type',
        ]
        
class ProjectSerializer (serializers.ModelSerializer):
    """ Project model serializer """
    
    tags = TagSerializer(many=True, read_only=True)
    tools = ToolSerializer(many=True, read_only=True)
    related_projects = ProjectSummarySerializer(many=True, read_only=True)
    media = MediaSummarySerializer(many=True, read_only=True)
    
    class Meta:
        model = models.Project
        fields = [
            'id', 
            'name', 
            'start_date', 
            'last_update', 
            'is_done',
            'updated_remote',
            'location_pc',
            'project_type',
            'logo',
            'web_page',
            'repo', 
            'board', 
            'license', 
            'tags',
            'tools',
            'related_projects',
            'description', 
            'details', 
            'install',
            'settings', 
            'run', 
            'build',
            'test',
            'deploy',
            'roadmap',
            'media',
        ]
        
class ProjectToolsMediasSerializer (serializers.ModelSerializer):
    """ Project model serializer """
    
    tools = ToolSerializer(many=True, read_only=True)
    media = MediaSummarySerializer(many=True, read_only=True)
    
    class Meta:
        model = models.Project
        fields = [
            'id', 
            'name', 
            'logo',
            'tools',
            'media',
        ]