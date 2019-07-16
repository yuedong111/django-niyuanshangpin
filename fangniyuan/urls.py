"""fangniyuan URL Configuration

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
from django.urls import path, re_path
from django.conf.urls import include, url
from login.views import index, find_file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path("mapp/<str:file_name>", find_file),
    re_path(r'user/', include(('protobufdata.urls', "users"), namespace="user")),
    path(r'company/', include(('companys.urls', "companys"), namespace="company")),
    url(r'login/', include('login.urls', namespace="login")),
    url(r"center/", include(("zonghoutai.urls", "centers"), namespace="center"))
    # re_path(r".*$", index)
]
