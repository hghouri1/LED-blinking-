from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hi, name="homepage"),
    path('on',views.on, name="on"),
    path('off',views.off,name="off"),
]
