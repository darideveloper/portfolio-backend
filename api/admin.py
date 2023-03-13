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