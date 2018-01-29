# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]

'''
only an empty string will match.In Django URL resolvers,
'http://127.0.0.1:8000/' is not a part of the URL.
name='post_list', is the name of the URL that will be used to
identify the view.
'''
