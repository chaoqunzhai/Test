from django.conf.urls import url,include
from django.contrib import admin
from app03 import views

urlpatterns = [
    url(r'^test',views.test),
    url(r'^tpl.html$', views.tpl),
]