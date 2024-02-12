from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('signup', views.signup, name="signup"),
    path('login', views.handlelogin, name="login"),
    path('logout', views.handlelogout, name="logout"),
]