from django.contrib import admin
from django.urls import path, include
from apnapswrd import views

urlpatterns = [
    path('',views.index, name="index"),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
    path('register',views.registerUser, name="register"),
    path('about',views.about, name="about"),
    path('contact',views.contact, name="contact"),
    path('addnew',views.addnew, name='addnew'),
    path('search',views.search, name='search'),
    path('delete',views.delete, name='delete'),
]
