from django.contrib import admin
from django.contrib.auth.models import Group, User
from api import models

def get_is_admin (request) -> str:
    """ Check if current user is admin

    Returns:
        str: _description_
    """

    user = request.user
    user_group = Group.objects.get(user=user).name if Group.objects.filter(user=user) else ""
    return user_group == "admin"

class FilterUser (admin.SimpleListFilter):
    """ Enable Users filter only for admin users """
    
    title = 'User'
    parameter_name = 'user'
    
    def lookups(self, request, model_admin):
        
        is_admin = get_is_admin(request)
        if is_admin:
            users = User.objects.all().order_by('username')
            user_names = [(user.id, user.username) for user in users]
            return user_names
        
        return []
    
    def queryset (self, request, queryset):
        
        is_admin = get_is_admin(request)
        if is_admin:
            
            if self.value():
                # Return filtered queryset
                return queryset.filter(user=self.value())
            else:
                # return all suers data 
                return queryset
        
        else:
            # Return only current user data
            return queryset.filter(user=request.user)
            
        
class FilterProjectUser (admin.SimpleListFilter):
    """ Allow to developers filter only their projects """
    
    title = 'Project'
    parameter_name = 'project'
    
    def lookups(self, request, model_admin):
        
        is_admin = get_is_admin(request)
        projects = models.Project.objects.all().order_by('name')
        if is_admin:
            project_names = [(project.id, project.name) for project in projects]
            return project_names
        
        projects_user = projects.filter(user=request.user)
        projects_user_names = [(project.id, project.name) for project in projects_user]
        return projects_user_names
    
    def queryset (self, request, queryset):
        
        is_admin = get_is_admin(request)
        if is_admin:
            
            if self.value():
                # Return filtered queryset
                return queryset.filter(project=self.value())
            else:
                # return all suers data 
                return queryset
        
        else:
            # Return only current user data
            return queryset.filter(project__user=request.user)
            