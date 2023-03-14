from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework import routers

admin.site.site_header = "Portfolio 2.0 Admin"
admin.site.site_title = 'Portfolio 2.0 Admin'
admin.site.site_url = '/'
admin.site.index_title = "API Administration"
    
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]
