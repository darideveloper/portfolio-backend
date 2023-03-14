from django.contrib import admin
from . import models

@admin.register(models.Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'badge_link', 'redirect_link')
    ordering = ('name',)
    search_fields = ('name', 'redirect_link')
    

@admin.register(models.Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'image')
    ordering = ('name',)
    search_fields = ('name', 'version')
    
@admin.register(models.Command)
class CommandAdmin(admin.ModelAdmin):
    list_display = ('name', 'command', 'details')
    ordering = ('name',)
    search_fields = ('name', 'command')
    
@admin.register(models.RoadMap)
class RoadMapAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ('name',)
    
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'last_login', 'web_page')
    ordering = ('username', 'email', 'web_page')
    search_fields = ('username', 'email', 'web_page')
    
@admin.register(models.UserBadge)
class UserBadgeAdmin(admin.ModelAdmin):
    list_display = ('user', 'badge')
    ordering = ('user', 'badge')
    search_fields = ('user__username', 'badge__name')
    list_filter = ('user__username', 'badge__name')
    
@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'start_date', 'last_update', 'logo', 'desciption')
    ordering = ('name', 'user', 'start_date', 'last_update')
    search_fields = ('name', 'user__username', 'desciption', 'details')
    list_filter = ('user__username', 'start_date', 'last_update')
    
@admin.register(models.ProjectBadge)
class ProjectBadgeAdmin(admin.ModelAdmin):
    list_display = ('project', 'badge')
    ordering = ('project', 'badge')
    search_fields = ('project__name', 'badge__name')
    list_filter = ('project__name', 'badge__name')
    
@admin.register(models.ProjectTool)
class ProjectToolAdmin(admin.ModelAdmin):
    list_display = ('project', 'tool')
    ordering = ('project', 'tool')
    search_fields = ('project__name', 'tool__name')
    list_filter = ('project__name', 'tool__name')
    
@admin.register(models.ProjectCommand)
class ProjectCommandAdmin(admin.ModelAdmin):
    list_display = ('project', 'command', 'tool', 'step', 'command_type')
    ordering = ('project', 'command', 'tool', 'command_type')
    search_fields = ('project__name', 'command__name', 'tool__name', 'command__details')
    list_filter = ('project__name', 'command__name', 'tool__name', 'command_type')
    
@admin.register(models.ProjectRoadMap)
class ProjectRoadMapAdmin(admin.ModelAdmin):
    list_display = ('project', 'road_map', 'done')
    ordering = ('project', 'road_map', 'done')
    search_fields = ('project__name', 'road_map__name')
    list_filter = ('project__name', 'road_map__name', 'done')