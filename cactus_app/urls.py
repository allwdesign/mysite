# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

app_name = 'cactus_app'

urlpatterns = [
    # This pattern checks that the URL has an empty path, which will go to
    # the homepage.
    url(r'^$', views.index),
    url(r'^([0-9]+)/$', views.detail, name='detail'),
    url(r'^post_cactus/$', views.post_cactus, name='post_cactus'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),
    ]

# Sends any URL that matches media/ to a built-in Django view called static.serve()
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, }),
    ]
