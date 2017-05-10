"""untitled3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from .views import *


urlpatterns = [
    url(r'^$', main_page,name='main_page'),
    url(r'^Messages/', Messages_HTML,name='Messages'),
    url(r'^Delete/(?P<id>\d+)/$', Delete_Message,name='Delete'),
    url(r'^Delete_color/(?P<id>\d+)/$', Delete_color, name='Delete_color'),
    url(r'^Colors/', Colors,name='Colors'),
    url(r'^Errors/', Errorlogfunc,name='Errors'),
    url(r'^Restart/', reboot,name='reboot'),
    url(r'^Shutdown/', shutdown, name='Shutdown'),
url(r'^refresh/', refresh, name='refresh'),
url(r'^TurnOn/', turn_on, name='TurnOn'),
url(r'^TurnOff/', turn_off, name='TurnOff'),



 ]
