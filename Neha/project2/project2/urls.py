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
    path('1', first_views.app1_view1),
    path('2', first_views.app1_view2),
    path('3', first_views.app1_view3),
    path('4', second_views.app2_view1),
    path('5', second_views.app2_view2),
    path('6', second_views.app2_view3),
    path('7', third_views.app3_view1),
    path('8', third_views.app3_view2),
    path('9', third_views.app3_view3),
]
