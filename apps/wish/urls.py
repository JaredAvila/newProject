from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/logout$', views.logout),
    url(r'^/stats/(?P<id>\d+)$', views.stats),
    url(r'^/create$', views.create),
    url(r'^/edit/(?P<id>\d+)$', views.edit),
    url(r'^/editting/(?P<id>\d+)$', views.editting),
    url(r'^/delete/(?P<id>\d+)$', views.delete),
    url(r'^/granted/(?P<id>\d+)$', views.granted),
    url(r'^/like/(?P<id>\d+)$', views.like),
    url(r'^/add$', views.add),
    url(r'^$', views.home)
]