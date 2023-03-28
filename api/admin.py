from . import models
from django.contrib import admin
from django.contrib.auth.models import Group, User

def get_user_data (request) -> dict:
    """ Get user data and return as dictionary

    Args:
        request (django.core.handlers.wsgi.WSGIRequest): user request
        id (bool, optional): True for return user id. Defaults to False.
        group (bool, optional): True for return user group. Defaults to False.
        projects (bool, optional): True for return user projects. Defaults to False.

    Returns:
        dict: user_id, user_group, user_projects
    """
    
    # Get user grup and id
    user = request.user
    user_group = Group.objects.get(user=user).name if Group.objects.filter(user=user) else ""
    user_id = user.id
    
    # Filter projects if user is developer
    if user_group == "developer":
        user_projects = models.Project.objects.filter(user=user)
    else:
        user_projects = models.Project.objects.all()
    user_projects = [str(project.id) for project in user_projects]
    
    return {
        "user_group": user_group,
        "user_id": user_id,
        "user_projects": user_projects
    }
    
@admin.register(models.Tag)
class Tag(admin.ModelAdmin):
    list_display = ('name', 'image', 'redirect')
    ordering = ('name', 'image', 'redirect')
    search_fields = ('name', 'image')    

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'redirect', 'user')
    ordering = ('name', 'image', 'redirect', 'user')
    search_fields = ('name', 'image', 'user__name')
    list_filter = ('user',)
    
    change_form_template = 'admin/change_form_contact.html' 
    change_list_template = 'admin/change_list_render_images.html'
    
    # Disable user field for developers
    def change_view(self, request, object_id, form_url='', extra_context=None):
        """ deactive user field """
            
        # Get user group of the user and submit to frontend
        return super(ContactAdmin, self).change_view(
            request, object_id, form_url, extra_context=get_user_data(request),
        )
        
    def add_view(self, request, form_url='', extra_context=None):
        """ deactive user field """
            
        # Get user group of the user and submit to frontend
        return super(ContactAdmin, self).add_view(
            request, form_url, extra_context=get_user_data(request),
        )
    
    # Only show contacts of the current developer
    def get_queryset(self, request):
        
        # Get admin type
        user_data = get_user_data(request)
        user_group = user_data["user_group"]

        if user_group == "developer":
            
            # Render only contacts of the current user
            return models.Contact.objects.filter (user=request.user)
            
        # Render all contacts
        return models.Contact.objects.all()   

@admin.register(models.Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'image', 'redirect')
    ordering = ('name', 'version', 'image', 'redirect')
    search_fields = ('name', 'version', 'redirect')
    
    change_list_template = 'admin/change_list_render_images.html'
    change_form_template = 'admin/change_form_tool.html'
    
@admin.register(models.Media)
class MediAdmin(admin.ModelAdmin):
    list_display = ('name', 'source', 'project', 'media_type')
    ordering = ('name', 'source', 'project', 'media_type')
    search_fields = ('name', 'source', 'project__name')
    list_filter = ('project', 'media_type')
    
    change_list_template = 'admin/change_list_render_images.html'
    change_form_template = 'admin/change_form_media.html' 
    
    # Disable project field for developers
    def change_view(self, request, object_id, form_url='', extra_context=None):
        """ deactive user field """
            
        # Get user group of the user and submit to frontend
        return super(MediAdmin, self).change_view(
            request, object_id, form_url, extra_context=get_user_data(request),
        )
        
    def add_view(self, request, form_url='', extra_context=None):
        """ deactive user field """
            
        # Get user group of the user and submit to frontend
        return super(MediAdmin, self).add_view(
            request, form_url, extra_context=get_user_data(request),
        ) 
        
    # Only show contacts of the current developer's projects
    def get_queryset(self, request):
        
        # Get admin type
        user_data = get_user_data(request)
        user_group = user_data["user_group"]

        if user_group == "developer":
            
            # Render only developer's projects media
            user = request.user
            projects = models.Project.objects.filter(user=user)
            print (projects)
            return models.Media.objects.filter(project__in=projects)
            
        # Render all projects media
        return models.Media.objects.all()
    
@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'start_date', 'last_update', 'logo', 'web_page', 'repo')
    ordering = ('name', 'user', 'start_date', 'last_update', 'web_page', 'repo')
    search_fields = ('name', 'user__username', 'description', 'details', 'tools__name', 
                     'tools__version', 'tags__name', 'web_page', 'repo', 'install',
                     'run', 'build', 'test', 'deploy', 'roadmap')
    list_filter = ('user__username', 'start_date', 'last_update', 'user', 'tags', 'tools')
    
    change_form_template = 'admin/change_form_project.html' 
    change_list_template = 'admin/change_list_render_images.html'
    
    # Disable user field for developers
    def change_view(self, request, object_id, form_url='', extra_context=None):
        """ deactive user field """
            
        # Get user group of the user and submit to frontend
        return super(ProjectAdmin, self).change_view(
            request, object_id, form_url, extra_context=get_user_data(request),
        )
        
    def add_view(self, request, form_url='', extra_context=None):
        """ deactive user field """
            
        # Get user group of the user and submit to frontend
        return super(ProjectAdmin, self).add_view(
            request, form_url, extra_context=get_user_data(request),
        )
        
    # Only show contacts of the current developer
    def get_queryset(self, request):
        
        # Get admin type
        user_data = get_user_data(request)
        user_group = user_data["user_group"]

        if user_group == "developer":
            
            # Render only projects of the current user
            return models.Project.objects.filter (user=request.user)
            
        # Render all projects
        return models.Project.objects.all()   