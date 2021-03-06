"""crawlerManagerSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from main_app import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login_page/', views.login_page, name='login_page'),
    path('register_page/', views.register_page, name='register_page'),
    path('main_page/', views.main_page, name='main_page'),
    path('login_logic/', views.login_logic, name='login_logic'),
    path('register_logic/', views.register_logic, name='register_logic'),
    path('menu/', views.menu, name='menu'),
    path('introduce/', views.introduce, name='introduce'),

]
