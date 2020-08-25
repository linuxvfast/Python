from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from django.conf import settings
import json
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import cache_page
import time
from app import models
from utils.sg import pizza_done
from django.forms import fields, widgets
from django import forms


def login(request):
    # obj = settings.CSRF_HEADER_NAME
    # return HttpResponse(json.dumps(obj))
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == 'root' and pwd == "123":
            # session中设置值
            request.session['username'] = user
            request.session['is_login'] = True
            if request.POST.get('rmb', None) == '1':
                # 超时时间(秒)
                request.session.set_expiry(10)
            return redirect('/index/')
        else:
            return render(request, 'login.html')


@csrf_protect
def index(request):
    if request.session.get('is_login', None):
        return render(request, 'index.html', {'username': request.session['username']})
    else:
        return HttpResponse('gun')


def logout(request):
    request.session.clear()
    return redirect('/login/')


@cache_page(10)  # 缓存10秒钟结果
def cache(request):
    ctime = time.time()
    return render(request, 'cache.html', {'ctime': ctime})


def signal(request):
    # 信号
    obj = models.UserInfo(user='root')
    print('end')
    obj.save()

    obj = models.UserInfo(user='root')
    obj.save()

    obj = models.UserInfo(user='root')
    obj.save()

    pizza_done.send(sender="asdfasdf", toppings=123, size=456)
    pizza_done.disconnect()
    return HttpResponse('ok')


class FM(forms.Form):
    # 通过form生成HTML页面
    user = fields.CharField(
        error_messages={'required': '用户名不能为空'},
        widget=widgets.Textarea(attrs={'class': 'c1'}),
        label='用户名',
    )
    pwd = fields.CharField(
        max_length=32,
        min_length=6,
        error_messages={'required': '密码不能为空', 'min_length': '密码最少为6个字符',
                        'max_length': '密码最多为32个字符'},
        widget=widgets.PasswordInput(attrs={'class': 'c2'})
    )
    email = fields.EmailField(error_messages={'required': '邮箱不能为空.', 'invalid': "邮箱格式错误"})

    f = fields.FileField(allow_empty_file=True)

    city1 = fields.ChoiceField(
        choices=[(0, '上海'), (1, '广州'), (2, '东莞')]
    )
    city2 = fields.MultipleChoiceField(
        choices=[(0, '上海'), (1, '广州'), (2, '东莞')]
    )


def fm(request):
    if request.method == 'GET':
        # 从数据库中吧数据获取到
        dic = {
            "user": 'r1',
            'pwd': '123123',
            'email': 'sdfsd',
            'city1': 1,
            'city2': [1, 2]
        }

        obj = FM(initial=dic)
        # print(obj)
        return render(request, 'fm.html', {'obj': obj})
    elif request.method == 'POST':
        # 获取用户所有数据
        # 每条数据请求的验证
        # 成功：获取所有的正确的信息
        # 失败：显示错误信息
        obj = FM(request.POST)
        # 验证form
        r1 = obj.is_valid()
        if r1:
            print(obj.cleaned_data)
            # models.UserInfo.objects.create(**obj.cleaned_data)
        else:
            return render(request, 'fm.html', {'obj': obj})
        return render(request, 'fm.html')
