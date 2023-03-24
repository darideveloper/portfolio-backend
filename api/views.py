from . import models, serializers
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import Group

class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tags to be viewed or edited.
    """
    queryset = models.Tag.objects.all().order_by('id')
    serializer_class = serializers.TagSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contacts to be viewed or edited.
    """
    queryset = models.Contact.objects.all().order_by('id')
    serializer_class = serializers.ContactSerializer
    permission_classes = [permissions.IsAuthenticated]

class ToolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tools to be viewed or edited.
    """
    queryset = models.Tool.objects.all().order_by('id')
    serializer_class = serializers.ToolSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class MediaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows media to be viewed or edited.
    """
    queryset = models.Media.objects.all().order_by('id')
    serializer_class = serializers.MediaSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    queryset = models.Project.objects.all().order_by('last_update')
    serializer_class = serializers.ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]