from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'', include('main.urls')),
    url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
]