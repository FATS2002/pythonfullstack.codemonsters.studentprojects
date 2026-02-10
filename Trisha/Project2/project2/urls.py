"""
URL configuration for project2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from firstapp import views as first_views
from secondapp import views as second_views  
from thirdapp import views as third_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('one', first_views.firstapp_v1),
    path('two', first_views.firstapp_v2),
    path('three', first_views.firstapp_v3),
    path('four', second_views.secondapp_v1),
    path('five', second_views.secondapp_v2),
    path('six', second_views.secondapp_v3),
    path('seven', third_views.thirdapp_v1),
    path('eight', third_views.thirdapp_v2),
    path('nine', third_views.thirdapp_v3),
]

