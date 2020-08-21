from django.shortcuts import render

# Create your views here.
from django import views
from django.shortcuts import redirect
from django.utils.decorators import method_decorator

user_info = {
    'dachengzi': {'pwd': "123123"},
    'kanbazi': {'pwd': "kkkkkkk"},
}


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('pwd')
        dic = user_info.get(u)
        if not dic:
            return render(request, 'login.html')
        if dic['pwd'] == p:
            res = redirect('/app/index')
            res.set_cookie('username111', u)
            res.set_cookie('user_type', "asdfjalskdjf", httponly=True)
            return res
        else:
            return render(request, 'login.html')


# 登录cookie验证装饰器函数
def auth(func):
    def inner(request, *args, **kwargs):
        v = request.COOKIES.get('username111')
        if not v:
            return redirect('/app/login')
        return func(request, *args, **kwargs)

    return inner


@auth  # auth(index(request))
def index(request):
    # 获取当前已经登录的用户
    v = request.COOKIES.get('username111')
    return render(request, 'index.html', {'current_user': v})

# method_decorator的作用是为函数视图装饰器补充第一个self参数，以适配类视图方法
@method_decorator(auth, name='dispatch')
class Order(views.View):
    def get(self, request):
        v = request.COOKIES.get('username111')
        return render(request, 'index.html', {'current_user': v})

    def post(self, reqeust):
        v = reqeust.COOKIES.get('username111')
        return render(reqeust, 'index.html', {'current_user': v})
