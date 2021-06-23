from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url('home/', views.home, name="home"),
    path('logout/', views.logout, name="logout"),

    path('Lab/Register/', views.Lab_Register, name="Lab_Register"),
    path('Lab/Login/', views.Lab_Login, name="Lab_Login"),


]
