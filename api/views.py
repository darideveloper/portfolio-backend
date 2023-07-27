import json
from . import models, serializers, tools
from rest_framework import viewsets
from rest_framework import views
from rest_framework import permissions
from rest_framework import response
from rest_framework.decorators import permission_classes


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tags to be viewed or edited.
    """
    queryset = models.Tag.objects.all().order_by('name')
    serializer_class = serializers.TagSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'head']
    
class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contacts to be viewed or edited.
    """
    # queryset = models.Contact.objects.all().order_by('id')
    queryset = models.Contact.objects.all().order_by('name')
    serializer_class = serializers.ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'head']
    
    def get_queryset(self):
        queryset = self.queryset
        user = self.request.user
        return queryset.filter(user=user.id)

class ToolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tools to be viewed or edited.
    """
    queryset = models.Tool.objects.all().order_by('name')
    serializer_class = serializers.ToolSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'head']
    
class MediaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows media to be viewed or edited.
    """
    queryset = models.Media.objects.all().order_by('-id')
    serializer_class = serializers.MediaSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'head']
    
    def get_queryset(self):
        queryset = self.queryset
        user = self.request.user
        projects = models.Project.objects.filter(user=user.id)
        return queryset.filter(project__in=projects)
    
class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    queryset = models.Project.objects.all().order_by('-last_update')
    serializer_class = serializers.ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'head']
    
    def get_queryset(self):
        queryset = self.queryset
        user = self.request.user
        return queryset.filter(user=user.id)

@permission_classes((permissions.AllowAny,))
class ProjectMarkdown(views.APIView):
    """
    API endpoint to get project data in markdown format
    """
    
    def get(self, request, format=None):
        
        # Get repo url from request
        repo = request.GET.get("repo")
        if not repo:
            return response.Response("No repo url provided")
        
        # Get project
        project = models.Project.objects.get(repo=repo)
        if not project:
            return response.Response("Project not found")
        
        # Get markdown
        markdown_generator = tools.MarkdownGenerator(project.id)
        markdown = markdown_generator.get_markdown()
                        
        return response.Response(markdown)
    