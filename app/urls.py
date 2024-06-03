"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    path('company', views.company, name='company'),
    path('projects', views.projects, name='projects'),
    
    path('get_blog_detail/<id>', views.blog_detail, name='blog_detail'),
    path('services', views.services, name='services'),
    path('send_mail', views.send_mail, name='send_mail'),
    path('get_price_list', views.get_price_list, name='get_price_list'),
    path('get_services', views.get_services, name='get_services'),
    path('get_service/<id>', views.get_service, name='get_service'),

    path('add_comment', views.add_comment, name='add_comment'),
    path('get_contacts', views.get_contacts, name='get_contacts'),
]