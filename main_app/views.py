from urllib import request

from django.core.paginator import Paginator
from django.shortcuts import render, redirect

# Create your views here.
from main_app.models import User, A02


def login_page(request):
    return render(request, 'login.html')


def register_page(request):

    return render(request, 'register.html')


def main_page(request):
    return render(request, 'main.html')


def login_logic(request):
    post_info = request.POST
    name = post_info.get('username')
    pwd = post_info.get('psw')
    users = User.objects.filter(username=name, password=pwd)
    if users:
        request.session['name'] = User.objects.get(username=name).username
        return redirect('main_page')
    else:
        request.session['error_msg'] = '用户名密码错误！'
        return redirect('login_page')


def register_logic(request):
    info = request.GET
    username = info.get('username')
    psw = info.get('psw')
    User(username=username, password=psw).save()
    return redirect('login_page')


count_ip = 0
count_ip = 0




def menu(request):
    ip = request.META.get('REMOTE_ADDR')
    num = request.GET.get('num')
    max_page = request.GET.get('max_page')
    if not num or int(num) < 0:
        num = 1
    if max_page:
        if int(num) > int(max_page):
            num = int(max_page)
    page = Paginator(A02.objects.values('id', 'name', 'anno', 'partycardnum'), per_page=10).page(int(num))
    return render(request, 'menu.html', {'page': page})


def introduce(request):
    return render(request, 'introduce.html')