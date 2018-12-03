# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url, include
from . import views
from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
     url(r'^hello/$', views.index , name='views.index'),
     url(r'^random/$', csrf_exempt(views.random) , name='views.random'),
]