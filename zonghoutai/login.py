from django.shortcuts import render, redirect, HttpResponse, render_to_response
from .models import User
import requests
import random
from functools import reduce
from urllib.parse import urlencode
from fangniyuan.settings import APPKEY, TPL_ID


def check_login(func):
    def wrapper(request, *args, **kwargs):
        if request.session.get("is_center_login", None):
            return func(request, *args, **kwargs)
        else:
            return redirect("center/login")

    return wrapper


def login(request):
    if request.session.get("is_center_login", None):
        return redirect("/index/")
    if request.method == "POST":
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        message = "请填写所有字段"
        if phone and password:
            try:
                user = User.objects.get(phone_number=phone)
                if user.password == password:
                    request.session["is_center_login"] = True
                    request.session["user_id"] = user.id
                    request.session["user_name"] = user.name
                    message = user.name
                    response = render_to_response("index.html", {"username": message})
                    response.set_cookie("Authorization", "Y6GT6rqg6l+jqvcJfKBK9gQehLOBWndYxyknhcUZm/y+aUYIa/UcMA==")
                    return response
                else:
                    message = "密码不正确"
            except:
                message = "用户名不存在"
            return render(request, "center/login.html", {"message": message})
    return render(request, 'center/login.html')