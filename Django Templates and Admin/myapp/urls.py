from django.contrib import admin
from django.urls import path
from . import views

app_name="myapp"
urlpatterns=[
     path('index/', views.index, name='index'),
     path('home/',views.home,name='home')
 ]