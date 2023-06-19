"""
URL configuration for Demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
#urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from django.contrib import admin
from django.urls import include, path

from . import views

admin.site.site_header = "ADMIN CUSTOMIZATION"

admin.site.index_title = "CUSTOMIZATION APP"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name='index'),
    path("index.html", views.index, name='home'),
    path("index/", views.index, name='home'),
    path("about.html", views.about, name='about'),
    path("blog/", views.blog, name='blog'),
    path('blog.html', views.blog,name='blog'),
    path("contact.html", views.contact,name='contact'),
    path("detail.html", views.detail,name='detail'),
    path("feature.html", views.feature,name='feature'),
    path("quote.html", views.quote,name='quote'),
    path("team.html", views.team,name='team'),
    path("service.html", views.service,name='service'),
    path("testimonial.html", views.testimonial,name='testimonial'),
    path("price.html", views.price, name="price"),
    path("form.html", views.form),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
   
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
