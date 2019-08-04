from django.shortcuts import render, redirect, HttpResponse

from user.forms import UserForm, LoginForm
from user.models import User
from functools import wraps


# 针对方法的登录验证（装饰器模式）
def check_login(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        if request.session.get('user_name'):
            return func(request, *args, **kwargs)
        else:
            return redirect('register')
    return inner





# 注册接口
def register(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = (request.POST.get('username')).strip()
            password = (request.POST.get('password')).strip()
            email = (request.POST.get('email')).strip()
            correct_user = User.objects.get(username=username)
            if not correct_user:
                user = User()
                user.username = username
                user.password = password
                user.email = email
                user.save()
                request.session['user_name'] = username
                request.session.set_expiry(0)  # 关闭浏览器就清掉session
                return redirect('home_page')
            else:    # 用户名重复
                error = "用户名已经存在"
        else:
            error = "获取表单信息失败"
    else:   # 不是post方式提交的数据
        error = ""
    userform = UserForm()
    context = {'userform': userform, 'error': error,}
    return render(request, 'user/register.html', context)


# 登录接口
def login(request):
    if request.method == 'POST':
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            username = (request.POST.get('username')).strip()
            password = (request.POST.get('password')).strip()
            correct_user = User.objects.get(username=username)
            if correct_user.password == password:
                request.session['user_name'] = username
                request.session.set_expiry(0)  # 关闭浏览器就清掉session
                return redirect('home_page')
    else:
        context = {
            'loginform': LoginForm()
        }
        return render(request, 'user/login.html', context)


# 登录检查接口
def login_check(request):
    if request.method == 'GET':
        username = (request.GET.get('username')).strip()
        if not username:
            return HttpResponse('no_username')
        password = (request.GET.get('password')).strip()
        correct_user = User.objects.filter(username=username)
        if not correct_user:
            return HttpResponse('no_username')
        elif not correct_user[0].password == password:
            return HttpResponse('no_password')
        else:
            return HttpResponse('success')










def logout(request):
    del request.session['user_name']
    return redirect('home_page')

