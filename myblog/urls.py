from django.contrib import admin
from django.urls import path
from django.urls import include
from myblog.views import *
from mysecondsite.urls import *

app_name ="myblog"

urlpatterns = [
    path("",view_index,name='index'),
    path("about",view_about,name='about'),
    path("test",view_test,name='test'),
]
