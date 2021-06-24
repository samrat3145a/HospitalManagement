from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url('home/', views.home, name="home"),
    path('logout/', views.logout, name="logout"),
    path('book_slot/', views.book_slot, name="book_slot"),
    path('hospital_search/', views.hospital_search, name="hospital_search"),
    path('Lab/Register/', views.Lab_Register, name="Lab_Register"),
    path('User/Register/', views.User_Register, name="User_Register"),
    path('Lab/Login/', views.Lab_Login, name="Lab_Login"),


]
