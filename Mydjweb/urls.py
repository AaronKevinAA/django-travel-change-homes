"""Mydjweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.views.static import serve

from Mydjweb.settings import MEDIA_ROOT
from django.conf import settings
from django.conf.urls.static import static

from XXX import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('pinfo/',views.personinfo),
    path('pinfo/modify/',views.modify_personinfo),
    path('pinfo/myhome/',views.myhome_info),
    path('pinfo/myhome/details/', views.mypublish_detail_info),
    path('pinfo/myhome/add/', views.myhome_add_info),
    path('pinfo/mydeal/', views.mydeal_info),
    path('pinfo/mypublish/add/', views.mypublish_add_info),
    path('details/', views.home_detail),
    path('search/',views.search),
    path('pinfo/mypublish/',views.mypublish_info),
    path('post/login/',views.post_login),
    path('post/register/', views.post_register),
    path('post/exit_login/', views.post_exit_login),
    path('post/modify_p_info/',views.post_modify_personinfo),
    path('post/realname/',views.post_realname),
    path('post/home_add/',views.post_home_add),
    path('post/publish_add/', views.post_publish_add),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})
]
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
