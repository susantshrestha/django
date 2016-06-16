from django.conf.urls import url
from . import views as posts_views

urlpatterns = [
    url(r'^$', posts_views.post_list,name='list'),
    url(r'^create/$', posts_views.post_create),
    url(r'^(?P<id>\d+)/$', posts_views.detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', posts_views.update,name='update'),
    url(r'^(?P<id>\d+)/delete/$', posts_views.delete),
]
