#-*- coding: UTF-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect


def login(request):
    if request.method == 'POST':
        input_email = request.POST['email']
        input_pwd = request.POST['pwd']
        if input_email == 'user1@qq.com' and input_pwd == '123':
            return redirect("http://www.etiantian.org")
        else:
            return render(request, "login.html", {"status": "用户名密码错误"})
    return render(request, 'login.html')
