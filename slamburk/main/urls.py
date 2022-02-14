"""twoo10 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    ## api interface ##


    ## ##

    ## / Section ##
    path('', views.index, name="index"),
    path('login', views.account_login, name="account_login"),
    path('logout', views.account_logout, name="account_logout"),
    path('registrace', views.account_register, name="account_register"),
    path('ucet', views.account_overview, name="account_overview"),
    path('novy-rytir', views.create_knight, name="create_knight"),
    path('upravit-rytire/<int:id>', views.edit_knight, name="edit_knight"),
    path('rytiri', views.all_knights_overview, name="all_knights_overview"),
    path('process_account_login', views.process_account_login,
         name="process_account_login"),
    path('process_account_register', views.process_account_register,
         name="process_account_register"),
    path('process_create_knight', views.process_create_knight,
         name="process_create_knight")

]

urlpatterns += static(settings.UPLOAD_URL,
                      document_root=settings.UPLOAD_ROOT)
