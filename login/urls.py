from django.contrib import admin
from django.urls import path
from login import views


app_name = "login"

urlpatterns = (
    path('index/', views.index),
    path("", views.index),
    path('login/', views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("register/", views.register, name="register"),
    path("send_code/", views.send_check_code, name="send_check_code"),
    path("forget_passwd/", views.passwd_forget, name="passwd_forget"),
    path("change_password/", views.reform_passwd, name="reform_passwd")
)