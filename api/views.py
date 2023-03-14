from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import permissions
from . import models, serializers

class BadgeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows badges to be viewed or edited.
    """
    queryset = models.Badge.objects.all().order_by('id')
    serializer_class = serializers.BadgeSerializer
    permission_classes = [permissions.IsAuthenticated]

class ToolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tools to be viewed or edited.
    """
    queryset = models.Tool.objects.all().order_by('id')
    serializer_class = serializers.ToolSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class CommandViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows commands to be viewed or edited.
    """
    queryset = models.Command.objects.all().order_by('id')
    serializer_class = serializers.CommandSerializer
    permission_classes = [permissions.IsAuthenticated]

class RoadMapViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows roadmaps to be viewed or edited.
    """
    queryset = models.RoadMap.objects.all().order_by('id')
    serializer_class = serializers.RoadMapSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class UserBadgeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user badges to be viewed or edited.
    """
    queryset = models.UserBadge.objects.all().order_by('id')
    serializer_class = serializers.UserBadgeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    queryset = models.Project.objects.all().order_by('id')
    serializer_class = serializers.ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class ProjectBadgeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows project badges to be viewed or edited.
    """
    queryset = models.ProjectBadge.objects.all().order_by('id')
    serializer_class = serializers.ProjectBadgeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class ProjectToolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows project tools to be viewed or edited.
    """
    queryset = models.ProjectTool.objects.all().order_by('id')
    serializer_class = serializers.ProjectToolSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class ProjectCommandViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows project commands to be viewed or edited.
    """
    queryset = models.ProjectCommand.objects.all().order_by('id')
    serializer_class = serializers.ProjectCommandSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class ProjectRoadMapViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows project roadmaps to be viewed or edited.
    """
    queryset = models.ProjectRoadMap.objects.all().order_by('id')
    serializer_class = serializers.ProjectRoadMapSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAuthenticated]