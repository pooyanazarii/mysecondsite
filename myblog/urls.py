from django.contrib import admin
from django.urls import path
from myblog.views import *
app_name ="myblog"

urlpatterns = [
    path("",view_index,name='index'),
    path("about",view_about,name='about'),
]
