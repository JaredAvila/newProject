from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^loginValid', views.loginValid),
    url(r'^regValid', views.regValid),
    url(r'^registration', views.registration),
    url(r'^login', views.login),
    url(r'^success', views.success)
]
