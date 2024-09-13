"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from appoinment_app.views import *
from django.urls import path
from users.views import CustomAuthToken,register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book-appoinment/',book_appoinment),
    path('view-appoinment/',view_appoinment),
    # path('register/', RegisterUser.as_view(), name='register'),
    path('register/', register, name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
]
