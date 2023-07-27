from . import models
from . import tools
from django.contrib import admin
from api.admin_filters import FilterUser, FilterProjectUser


@admin.register(models.Tag)
class Tag(admin.ModelAdmin):
    list_display = ('name', 'details')
    ordering = ('name', 'details')
    search_fields = ('name', 'details')
    list_per_page = 20


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'redirect', 'user')
    ordering = ('name', 'image', 'redirect', 'user')
    search_fields = ('name', 'image', 'user__name')
    list_filter = [FilterUser]
    list_per_page = 20

    change_form_template = 'admin/change_form_contact.html'
    change_list_template = 'admin/list_render_media.html'

    # Disable user field for developers
    def change_view(self, request, object_id, form_url='', extra_context=None):
        """ deactive user field """

        # Get user group of the user and submit to frontend
        return super(ContactAdmin, self).change_view(
            request, object_id, form_url, extra_context=tools.get_user_data(
                request),
        )

    def add_view(self, request, form_url='', extra_context=None):
        """ deactive user field """

        # Get user group of the user and submit to frontend
        return super(ContactAdmin, self).add_view(
            request, form_url, extra_context=tools.get_user_data(request),
        )

    # Only show contacts of the current developer
    def get_queryset(self, request):

        # Get admin type
        user_data = tools.get_user_data(request)
        user_group = user_data["user_group"]

        if user_group == "developer":

            # Render only contacts of the current user
            return models.Contact.objects.filter(user=request.user)

        # Render all contacts
        return models.Contact.objects.all()


@admin.register(models.Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'redirect')
    ordering = ('name', 'image', 'redirect')
    search_fields = ('name', 'redirect')
    list_per_page = 20

    change_list_template = 'admin/list_render_media.html'
    change_form_template = 'admin/change_form_tool.html'


@admin.register(models.Media)
class MediAdmin(admin.ModelAdmin):
    list_display = ('name', 'source', 'project', 'media_type')
    ordering = ('-project__last_update', 'project__name',
                'name', 'source', 'project', 'media_type')
    search_fields = ('name', 'source', 'project__name')
    list_filter = ('media_type', FilterProjectUser)
    list_per_page = 20

    change_list_template = 'admin/list_render_media.html'
    change_form_template = 'admin/change_form_media.html'

    # Disable project field for developers
    def change_view(self, request, object_id, form_url='', extra_context=None):
        """ deactive user field """

        # Get user group of the user and submit to frontend
        return super(MediAdmin, self).change_view(
            request, object_id, form_url, extra_context=tools.get_user_data(
                request),
        )

    def add_view(self, request, form_url='', extra_context=None):
        """ deactive user field """

        # Get user group of the user and submit to frontend
        return super(MediAdmin, self).add_view(
            request, form_url, extra_context=tools.get_user_data(request),
        )

    # Only show contacts of the current developer's projects
    def get_queryset(self, request):

        # Get admin type
        user_data = tools.get_user_data(request)
        user_group = user_data["user_group"]

        if user_group == "developer":

            # Render only developer's projects media
            user = request.user
            projects = models.Project.objects.filter(user=user)
            return models.Media.objects.filter(project__in=projects)

        # Render all projects media
        return models.Media.objects.all()


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'board', 'user', 'is_done', 'start_date', 'last_update', 'logo',
                    'web_page', 'repo')
    ordering = ('-last_update', 'name', 'board', 'user',
                'start_date', 'web_page', 'repo')
    search_fields = ('name', 'user__username', 'board', 'description', 'details', 'tools__name',
                     'tags__name', 'web_page', 'repo', 'install',
                     'run', 'build', 'test', 'deploy', 'roadmap')
    list_filter = ('is_done', 'project_type', 'start_date',
                   'last_update', FilterUser, 'tags', 'tools')
    list_per_page = 20

    change_form_template = 'admin/change_form_project.html'
    change_list_template = 'admin/list_render_media.html'

    # Disable user field for developers
    def change_view(self, request, object_id, form_url='', extra_context=None):
        """ deactive user field """
        
        if type(object_id) == int:
            markdown_generator = tools.MarkdownGenerator(object_id)
            tags_tools = tools.get_tags_tools(object_id)

            # Get user group of the user and submit to frontend
            return super(ProjectAdmin, self).change_view(
                request, object_id, form_url, extra_context={
                    "markdown": markdown_generator.get_markdown(),
                    "tags_tools": tags_tools
                },
            )
        else:
            return super(ProjectAdmin, self).change_view(
                request, object_id, form_url,
            )

    # Only show contacts of the current developer
    def get_queryset(self, request):

        # Get admin type
        user_data = tools.get_user_data(request)
        user_group = user_data["user_group"]

        if user_group == "developer":

            # Render only projects of the current user
            return models.Project.objects.filter(user=request.user)

        # Render all projects
        return models.Project.objects.all()
