"""day19 URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from app01 import views


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^servers$',views.servers),
    url(r'^add_user$',views.add_user),
    url(r'^del_user$',views.del_user),
    #url(r'^update_user$',views.update_user),
    url(r'^update_user.html$',views.update_user,name='mmm'),
    #url(r'update_users_(?P<n1>\d+)-(?P<n2>\d+).html',views.update_user_new), #可以取到2个值
    url(r'^update_user_new-(?P<nnid>\d+).html$',views.update_user_new,name='nnn'), #动态的url url把这些值都传入给views视图函数中
    url(r'^groups$',views.groups),
    url(r'^login$',views.login),
    url(r'cmdb/',include('app02.urls')),
    url(r'openstack/',include('app03.urls')),
]
