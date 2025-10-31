"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static

import app.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("get-all",views.AllInfoView.as_view(), name="all-info"),
    path("get-sidebar",views.SideBarView.as_view(), name="sidebar"),
    path('get-home', views.HomeView.as_view(), name="home"),
    path('get-about', views.AboutView.as_view(), name="about"),
    path('get-service', views.ServiceView.as_view(), name="service"),
    path('get-project', views.ProjectView.as_view(), name="project"),
    path('get-blog', views.BlogView.as_view(), name="blog"),
    path('get-contact', views.contact_view, name="contact"),
    path('add-visitor', views.visitor_view, name="visitor"),
    path('get-blog-details', views.blog_details, name="blog-details"),
    path('get-project-details', views.project_details, name="project-details"),

] + static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
