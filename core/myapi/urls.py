from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('login', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
]