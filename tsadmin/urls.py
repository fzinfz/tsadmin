"""tsadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from connection.views import *
from django.conf import settings

urlpatterns = [

    url(r'^$', PostPublicListView.as_view(), name='index'),

    url(r'^post/(?P<slug>[-\w]+)/$', PostPublicDetailView.as_view(), name='post_detail_slug'),
    url(r'^p/(?P<pk>\d+)/$', PostPublicDetailView.as_view(), name='post_detail'),

    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^login/', auth_views.login, name='login'),
    url(r'^accounts/profile/', NodeListView.as_view(), name='profile'),

    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^markdownx/', include('markdownx.urls')),
    url(r'^api/', include('api.urls')),
]