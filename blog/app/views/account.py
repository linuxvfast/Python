from django.shortcuts import render, HttpResponse, redirect
from io import BytesIO
from utils.check_code import create_validate_code


def check_code(request):
    """
    验证码
    """
    stream = BytesIO()
    img, code = create_validate_code()
    img.save(stream, 'PNG')
    request.session['CheckCode'] = code
    return HttpResponse(stream.getvalue())


def login(request):
    # 用户登陆
    # if request.method == "POST":
    #     if request.session['CheckCode'].upper() == request.POST.get('check_code').upper():
    #         pass
    #     else:
    #         print('验证码错误')
    if request.method == 'POST':
        code = request.POST.get('check_code')
        # print(code)
        # print(request.session['CheckCode'].upper())
        if code.upper() == request.session['CheckCode'].upper():
            print('验证码正确')
        else:
            print('验证码错误')
    return render(request, 'login.html')


def register(request):
    # 注册用户
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        user = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(user, email, password)
        return redirect('/register')


def logout(request):
    request.session.clear()
    return redirect('/')


def jsonp(request):
    pass
