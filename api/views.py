from . import models, serializers, tools
from rest_framework import viewsets
from rest_framework import views
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework import status


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tags to be viewed.
    """
    queryset = models.Tag.objects.all().order_by('name')
    serializer_class = serializers.TagSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'head']
    
class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contacts to be viewed.
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
    API endpoint that allows tools to be viewed.
    """
    queryset = models.Tool.objects.all().order_by('name')
    serializer_class = serializers.ToolSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'head']
    
class MediaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows media to be viewed.
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
    API endpoint that allows projects to be viewed.
    """
    queryset = models.Project.objects.all().order_by('-last_update')
    serializer_class = serializers.ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'head']
    
    def get_queryset(self):
        queryset = self.queryset
        user = self.request.user
        return queryset.filter(user=user.id)
    
class ProjectSumaryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects sumary to be viewed.
    """
    queryset = models.Project.objects.all().order_by('-last_update')
    serializer_class = serializers.ProjectSumarySerializer
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
        project_id = request.GET.get("id")
        if not project_id:
            return Response({
                "status": "error",
                "message": "No id url provided",
                "data": ""
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Get project
        project = models.Project.objects.filter(id=project_id)
        if not project:
            return Response({
                "status": "error",
                "message": "project not found",
                "data": ""
            }, status=status.HTTP_404_NOT_FOUND)
        
        # Get markdown
        markdown_generator = tools.MarkdownGenerator(project_id)
        markdown = markdown_generator.get_markdown()
                        
        return Response({
            "status": "ok",
            "message": "markdown generated",
            "data": markdown
        })
        
@permission_classes((permissions.AllowAny,))
class ProjectUpdateRemote(views.APIView):
    """
    API endpoint change "update_remote" project field
    """
    
    def post(self, request, format=None):
        
        # Get repo url from request
        project_id = request.POST.get("id")
        if not project_id:
            return Response({
                "status": "error",
                "message": "No id url provided",
                "data": ""
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Get project
        project = models.Project.objects.filter(id=project_id)
        if not project:
            return Response({
                "status": "error",
                "message": "project not found",
                "data": ""
            }, status=status.HTTP_404_NOT_FOUND)
        
        # Update project data
        project = project[0]
        project.updated_remote = True
        project.save ()
                        
        return Response({
            "status": "ok",
            "message": "Updated remote saved.",
            "data": ""
        })
    
    