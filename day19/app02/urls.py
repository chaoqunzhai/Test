from django.conf.urls import url,include
from django.contrib import admin
from app02 import views

urlpatterns = [
    url(r'^test$',views.test),
    url(r'^upload.html$',views.upload),
]