from api import views
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from rest_framework.authtoken import views as auth_views


admin.site.site_header = "Portfolio 2.0 Admin"
admin.site.site_title = 'Portfolio 2.0 Admin'
admin.site.site_url = '/'
admin.site.index_title = "API Administration"
    
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register (r'tags', views.TagViewSet)
router.register (r'contacts', views.ContactViewSet)
router.register (r'tools', views.ToolViewSet)
router.register (r'medias', views.MediaViewSet)
router.register (r'projects', views.ProjectViewSet)
router.register (r'projects-sumary', views.ProjectSumaryViewSet, basename='projects-sumary')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-token-auth/', auth_views.obtain_auth_token, name='api-token-auth'),
    path('project-markdown/', views.ProjectMarkdown.as_view(), name='project-markdown'),
    path('project-update-remote/', views.ProjectUpdateRemote.as_view(), name='project-update-remote'),
]
