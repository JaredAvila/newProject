from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.login.urls')),
    url(r'^wish', include('apps.wish.urls')),
    url(r'^admin/', admin.site.urls)
]
