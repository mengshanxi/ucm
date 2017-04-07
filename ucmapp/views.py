# -*- coding: UTF-8 -*-
from django.shortcuts import render
from ucmapp.models import Employee
from django.contrib import admin


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == 'user01' and password == '123456':
            return render(request, "index.html")
        else:
            return render(request, "login.html", {"status": "用户名密码错误"})
    return render(request, 'login.html')


def welcome(request):
    return render(request, "welcome.html")


def users(request):
    return render(request, 'user-list.html')


def addUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        realname = request.POST['realname']
        employee = Employee(username=username, realname=realname)
        employee.save()
        return render(request, "index.html")
    return render(request, "user-add.html")
