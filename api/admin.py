from django.contrib import admin
from . import models

@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'tag_link', 'redirect_link')
    ordering = ('name',)
    search_fields = ('name', 'redirect_link')

@admin.register(models.Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'image')
    ordering = ('name',)
    search_fields = ('name', 'version')
    
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'last_login', 'web_page')
    ordering = ('username', 'email', 'web_page')
    search_fields = ('username', 'email', 'web_page')
    
@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'start_date', 'last_update', 'logo', 'description')
    ordering = ('name', 'user', 'start_date', 'last_update')
    search_fields = ('name', 'user__username', 'description', 'details')
    list_filter = ('user__username', 'start_date', 'last_update')