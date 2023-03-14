from django.contrib import admin
from django.urls import path

admin.site.site_header = "Portfolio 2.0 Admin"
admin.site.site_title = 'Portfolio 2.0 Admin'
admin.site.site_url = '/'
admin.site.index_title = "API Administration"

urlpatterns = [
    path('admin/', admin.site.urls),
]
