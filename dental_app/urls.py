from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('base_html/',base_html, name="base"),
    ]