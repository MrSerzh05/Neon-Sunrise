"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from first import views as viewsfir
from django.conf.urls import url
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', viewsfir.index2, name = 'mainsh'),
	path('signup', viewsfir.index3, name = 'mainsh2'),
	path('cabinet', viewsfir.index4, name = 'mainsh3'),
	path('registration', viewsfir.index5, name = 'mainsh4'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('moved/', include('mysite.urls')),
    path('accounts/', include('accounts.urls')),
    path('create', viewsfir.create),
]