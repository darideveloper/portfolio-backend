from . import models
from django.contrib.auth.models import Group, User


class MarkdonGenerator ():

    def __init__(self, project_id: int):
        """ Generate markdown file from project instance

        Args:
            project_id (int): project id
        """

        # Get project instance
        self.project = models.Project.objects.get(id=project_id)

        # Filter markdown text fields
        markdown_text_fields_base = [
            "details",
            "install",
            "settings",
            "run",
            "build",
            "test",
            "deploy",
            "roadmap",
        ]

        self.markdown_text_fields = []
        for field in markdown_text_fields_base:
            if getattr(self.project, field):
                self.markdown_text_fields.append(field)

    def __get_contacts__(self) -> str:
        """ Return contact icons of the project, in markdown format

        Returns:
            str: markdown formatted data
        """

        markdown = "<div>"

        # Add license shell
        repo_name = self.project.repo.split("/")[-2]
        repo_user = self.project.repo.split("/")[-3]
        user = self.project.user
        markdown += f"""<a href='https://github.com/{repo_user}/{repo_name}/blob/master/LICENSE' target='_blank'>
            <img src='https://img.shields.io/github/license/{repo_user}/{repo_name}.svg?style=for-the-badge' alt='MIT License' height='30px'/>
        </a>"""

        # Add contact shells
        contacts = models.Contact.objects.filter(user=user)
        for contact in contacts:
            markdown += f"""<a href='{contact.redirect}' target='_blank'>
                <img src='{contact.image}' alt='{contact.name.title()}' height='30px'/>
            </a>"""

        markdown += "</div>"

        return markdown

    def __get_header__(self) -> str:
        """ Return header part of markdown: logo, projects name, dtart date, end date, project type

        Returns:
            str: markdown formatted data
        """

        markdown = "<div align='center'><br><br>"

        # Logo
        if self.project.logo:
            markdown += f"<img src='{self.project.logo}' alt='{self.project.name}' height='80px'/>\n\n"

        # Name
        markdown += f"# {self.project.name}\n\n"

        # Web page
        if self.project.web_page:
            clean_link = self.project.web_page.replace("http://", "").replace("https://", "").replace("www.", "")
            if clean_link[-1] == "/":
                clean_link = clean_link[:-1]
            markdown += f"Visit at: **[{clean_link}]({self.project.web_page})**\n\n"

        # Description
        markdown += f"{self.project.description}\n\n"

        # General data
        markdown += f"Start date: **{self.project.start_date}**\n\n"
        markdown += f"Last update: **{self.project.last_update}**\n\n"
        markdown += f"Project type: **{self.project.project_type}'s project**\n\n"

        markdown += "</div>"

        return markdown

    def __get_menu__(self) -> str:
        """ Return dtnamic table of contents based in project data, in markdown format

        Returns:
            str: markdown formatted data
        """

        markdown = ""

        # Create and filter menu items
        menu_items = ["Build width", "Related Projects",
                      "Media"] + self.markdown_text_fields
        if self.project.related_projects.count() == 0:
            menu_items.remove("Related Projects")

        # Create menu
        menu_links = ""
        for menu_item in menu_items:
            menu_links += f"\n<li><a href='#{menu_item.lower().replace(' ', '')}'>{menu_item.title()}</a></li>"

        markdown += f"""<br><details>
            <summary>Table of Contents</summary>
            <ol>{menu_links}</ol>
        </details><br>\n\n"""

        return markdown

    def __get_medias__(self) -> str:
        """ Return project media (like images and videos) in markdowjnn format

        Returns:
            str: markdown formatted data
        """

        markdown = ""

        # Get project and medias
        medias = models.Media.objects.filter(project=self.project)

        if medias.count() > 0:
            markdown += f"# Media\n\n"

            # Save each media
            for media in medias:
                markdown += f"![{media.name}]({media.source})\n\n"

        return markdown

    def __get_text_fields__(self) -> str:
        """ Return project text fields (description, details, install, settings, run,
        buld, deploy, roadmap) in markdown format

        Args:
            project (models.Project): project instance

        Returns:
            str: markdown formatted data
        """

        markdown = ""

        # Save markdown fields
        for field in self.markdown_text_fields:
            markdown += f"# {field.capitalize()}\n\n{getattr(self.project, field)}\n\n"

        return markdown

    def __get_related_projects__(self) -> str:
        """ Return related projects in markdown format

        Args:
            project (models.Project): project instance

        Returns:
            str: markdown formatted data
        """

        related_projects = self.project.related_projects.all()

        if related_projects.count() == 0:
            return ""

        markdown = "# Related projects\n\n"

        markdown += "<div align='center'>"

        for project in related_projects:
            markdown += f"<a href='{project.repo}' target='_blank'> <img src='{project.logo}' alt='{project.name}' title='{project.name}' height='50px'/> </a>"

        markdown += "</div>\n\n"

        return markdown

    def __get_build_with__(self) -> str:
        """ Return build width section in markdown format

        Returns:
            str: markdown formatted data
        """

        markdown = "# Build with\n\n"

        markdown += "<div align='center'>"

        build_tools = self.project.tools.all()

        for tool in build_tools:
            markdown += f"<a href='{tool.redirect}' target='_blank'> <img src='{tool.image}' alt='{tool.name}' title='{tool.name}' height='50px'/> </a>"

        markdown += "</div>\n\n"

        return markdown

    def get_markdown(self) -> str:
        """ Format full project instance and return as markdown

        Returns:
            str: markdown formatted data
        """

        markdown = ""
        markdown += f"{self.__get_contacts__()}"
        markdown += f"{self.__get_header__()}"
        markdown += f"{self.__get_menu__()}"
        markdown += f"{self.__get_build_with__()}"
        markdown += f"{self.__get_related_projects__()}"
        markdown += f"{self.__get_medias__()}"
        markdown += f"{self.__get_text_fields__()}"

        # Scape quotes
        markdown = markdown.replace('"', '\\"').replace(
            "'", "\\'").replace("`", "\\`")

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
