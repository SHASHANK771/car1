"""car URL Configuration

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
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('page', views.formView,name='form'),
    path('login', views.login,name='login'),
    path('about', views.about,name='about'),
    path('about', views.about,name='about'),
    path('services', views.services,name='services'),
    path('reg', views.reg,name='reg'),
    path('ins', views.ins,name='ins'),
    path('student', views.student,name='student'),
    path('from1/',views.from1,name="from1"),
    path('from2/',views.from2,name="from2"),
    path('from3/',views.from3,name="from3"),
    

   

]
