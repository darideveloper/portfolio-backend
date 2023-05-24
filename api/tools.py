from . import models
from django.contrib.auth.models import Group, User

def get_markdown (project_id:int) -> str:
    """ Format project instance and return as markdown

    Args:
        project_id (int): project id

    Returns:
        str: markdown formatted project
    """
    
    markdown = ""
    
    # Get project and medias
    project = models.Project.objects.get(id=project_id)
    medias = models.Media.objects.filter(project=project)
    
    # Name
    markdown += f"# {project.name}\n\n"    
    
    # Description
    markdown += f"{project.description}\n\n"
    
    # General data
    markdown += f"Start date: **{project.start_date}**\n\n"
    markdown += f"Last update: **{project.last_update}**\n\n"
    markdown += f"Project type: **{project.project_type}'s project**\n\n"
    
    # Logo
    if project.logo:
        markdown += f"![Logo]({project.logo})\n\n"
    
    # Web page
    if project.web_page:
        markdown += f"Visit at: **[{project.web_page}]({project.web_page})**\n\n"
        
    if medias.count() > 0:
        markdown += f"## Media\n\n"
        
        for media in medias:
            markdown += f"![{media.name}]({media.source})\n\n"
    
    # Markdown fields
    markdown_fields = [
        "details",
        "install",
        "settings",
        "run",
        "build",
        "test",
        "deploy",
        "roadmap",
    ]
    
    for field in markdown_fields:
        if getattr(project, field):
            markdown += f"# {field.capitalize()}\n\n{getattr(project, field)}\n\n"
    
    # Scape quotes
    markdown = markdown.replace('"', '\\"').replace("'", "\\'").replace("`", "\\`")
    
    return markdown        
    

def get_user_data(request) -> dict:
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
    user_group = Group.objects.get(
        user=user).name if Group.objects.filter(user=user) else ""
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
     