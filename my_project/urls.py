"""
URL configuration for my_project project.

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
from django.contrib import admin
from django.urls import path, include
from comparative_medicine_database.views import index, search_medicines, get_all_medicines, get_medicine_detail

urlpatterns = [
    path('', index, name='index'),  # Home page view
    path('api/search/', search_medicines, name='search_medicines'),  # Search API endpoint
    path('api/medicines/', get_all_medicines, name='get_all_medicines'),  # Get all medicines API
    path('api/medicines/<int:medicine_id>/', get_medicine_detail, name='get_medicine_detail'),  # Get specific medicine API
    path('admin/', admin.site.urls),
]
