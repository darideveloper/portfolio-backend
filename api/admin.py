from django.contrib import admin
from . import models

@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'redirect')
    ordering = ('name', 'image', 'redirect')
    search_fields = ('name', 'image')
    
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'redirect')
    ordering = ('name', 'image', 'redirect')
    search_fields = ('name', 'image')

@admin.register(models.Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'image')
    ordering = ('name', 'version', 'image')
    search_fields = ('name', 'version')
    
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'last_login', 'web_page')
    ordering = ('username', 'email', 'web_page')
    search_fields = ('username', 'email', 'web_page')
    
@admin.register(models.Media)
class UserMedia(admin.ModelAdmin):
    list_display = ('name', 'link', 'project', 'media_type')
    ordering = ('name', 'link', 'project', 'media_type')
    search_fields = ('name', 'link', 'project__name')
    list_filter = ('project__name', 'media_type')    
    
@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    change_form_template = 'admin/change_form_project.html' 
    list_display = ('name', 'user', 'start_date', 'last_update', 'logo', 'web_page', 'repo', 'description')
    ordering = ('name', 'user', 'start_date', 'last_update', 'web_page', 'repo')
    search_fields = ('name', 'user__username', 'description', 'details', 'tools__name', 
                     'tools__version', 'tags__name', 'web_page', 'repo', 'install',
                     'run', 'build', 'test', 'deploy', 'roadmap')
    list_filter = ('user__username', 'start_date', 'last_update', 'user', 'tags', 'tools')