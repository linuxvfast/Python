from django.shortcuts import render, HttpResponse
from django import forms
from django.forms import fields as Ffields
from django.forms import widgets as Fwidgets
from . import models
import time
import json
import os
import requests


# Create your views here.
class UserInfoModelForm(forms.ModelForm):
    is_rmb = Ffields.CharField(widget=Fwidgets.CheckboxInput())

    class Meta:
        model = models.UserInfo

        fields = '__all__'
        # fields =  ['username','email']
        # exclude = ['username']
        # 提示信息
        labels = {
            'username': '用户名',
            'email': '邮箱',
        }
        # 帮助信息
        help_texts = {
            'username': '...'
        }
        # 自定义插件
        widgets = {
            'username': Fwidgets.Textarea(attrs={'class': 'c1'})
        }
        error_messages = {
            '__all__': {

            },
            'email': {
                'required': '邮箱不能为空',
                'invalid': '邮箱格式错误..',
            }
        }

        # 自定义字段类
        field_classes = {
            # 'email': Ffields.URLField
        }

        # localized_fields=('ctime',)

    def clean_username(self):
        # 验证用户名
        old = self.cleaned_data['username']
        return old


def index(request):
    '''
    首页
    :param request:
    :return:
    '''
    if request.method == 'GET':
        obj = UserInfoModelForm()
        return render(request, 'index.html', {'obj': obj})
    elif request.method == "POST":
        obj = UserInfoModelForm(request.POST)
        if obj.is_valid():  # 验证数据
            # obj.save()
            instance = obj.save(False)
            instance.save()
            obj.save_m2m()
        return render(request, 'index.html', {'obj': obj})


def user_list(request):
    '''
    列出所有的用户
    :param request:
    :return:
    '''
    li = models.UserInfo.objects.all().select_related('user_type')
    return render(request, 'user_list.html', {'li': li})


def user_edit(request, nid):
    '''
    编辑用户当前的信息
    :param request:
    :param nid: 当前的用户id
    :return:
    '''
    if request.method == 'GET':
        obj = models.UserInfo.objects.filter(id=nid).first()
        mf = UserInfoModelForm(instance=obj)
        return render(request, 'user_edit.html', {'mf': mf, 'nid': nid})
    elif request.method == 'POST':
        user_obj = models.UserInfo.objects.filter(id=nid).first()
        mf = UserInfoModelForm(request.POST, instance=user_obj)
        if mf.is_valid():
            mf.save()
        else:
            print(mf.errors.as_json())
        return render(request, 'user_edit.html', {'mf': mf, 'nid': nid})


def ajax(request):
    return render(request, 'ajax.html')


def ajax_json(request):
    time.sleep(3)
    print(request.POST)
    ret = {'code': True, 'data': request.POST.get('username')}
    return HttpResponse(json.dumps(ret))


def upload(request):
    return render(request, 'upload.html')


def upload_file(request):
    username = request.POST.get('username')
    fafafa = request.FILES.get('fafafa')

    img_path = os.path.join('static/imgs/', fafafa.name)
    with open(img_path, 'wb') as f:
        for item in fafafa.chunks():
            f.write(item)

    ret = {'code': True, 'data': img_path}
    return HttpResponse(json.dumps(ret))


def kind(request):
    return render(request, 'kind.html')


def upload_img(request):
    # request.GET.get('dir')
    # print(request.FILES.get('fafafa'))
    # 获取文件保存
    dic = {
        'error': 0,
        'url': '/static/imgs/20130809170025.png',
        'message': '错误了...'
    }

    return HttpResponse(json.dumps(dic))


def file_manager(request):
    dic = {}
    root_path = 'H:/Python36/source_code/webcode/day30/static/'
    static_root_path = '/static/'
    request_path = request.GET.get('path')
    print('request_path', request_path)
    if request_path:
        abs_current_dir_path = os.path.join(root_path, request_path)
        move_up_dir_path = os.path.dirname(request_path)
        print('move_up_dir_path', move_up_dir_path)
        dic['moveup_dir_path'] = move_up_dir_path + '/' if move_up_dir_path else move_up_dir_path
    else:
        abs_current_dir_path = root_path
        dic['moveup_dir_path'] = ''

    dic['current_dir_path'] = request_path
    dic['current_url'] = os.path.join(static_root_path, request_path)

    file_list = []
    print(abs_current_dir_path)
    for item in os.listdir(abs_current_dir_path):
        print(item)
        abs_item_path = os.path.join(abs_current_dir_path, item)
        # 分离文件名和扩展名
        a, exts = os.path.splitext(item)
        is_dir = os.path.isdir(abs_item_path)
        if is_dir:
            temp = {
                'is_dir': True,
                'has_file': True,
                'filesize': 0,
                'dir_path': '',
                'is_photo': False,
                'filetype': '',
                'filename': item,
                'datetime': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(os.path.getctime(abs_item_path)))
            }
        else:
            temp = {
                'is_dir': False,
                'has_file': False,
                'filesize': os.stat(abs_item_path).st_size,
                'dir_path': '',
                'is_photo': True if exts.lower() in ['.jpg', '.png', '.jpeg'] else False,
                'filetype': exts.lower().strip('.'),
                'filename': item,
                'datetime': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(os.path.getctime(abs_item_path)))
            }

        file_list.append(temp)
    dic['file_list'] = file_list
    return HttpResponse(json.dumps(dic))


def orm(request):
    # models.UserType.objects.create(caption='开发')
    # models.UserType.objects.create(caption='运维')
    # models.UserType.objects.create(caption='销售')
    # models.UserGroup.objects.create(name='第一小组')
    # models.UserGroup.objects.create(name='第二小组')
    # models.UserGroup.objects.create(name='第三小组')
    # models.UserInfo.objects.filter(id__gt=1).delete()
    # str = "     this is string example....wow!!!     ";
    # print(str.rstrip())
    models.Category.objects.create(caption='原创')
    models.Category.objects.create(caption='转载')
    models.Article.objects.create(title='测试标题', content='测试内容', category_id=1, article_type_id=1)
    models.Article.objects.create(title='测试2标题', content='测试内容2222', category_id=2, article_type_id=3)
    return HttpResponse('ok')


def req(request):
    response = requests.get('http://weatherapi.market.xiaomi.com/wtr-v2/weather?cityId=101121301')
    response.encoding = 'utf-8'

    return render(request, 'req.html', {'result': response.text})


def article(request, *args, **kwargs):
    # print(kwargs)
    # print(request.path_info) # 获取当前URL
    # from django.urls import reverse
    # # {'article_type_id': '0', 'category_id': '0'}
    # url = reverse('article',kwargs={'article_type_id': '1', 'category_id': '0'})
    # print(url)
    # print(kwargs) # {'article_type_id': '0', 'category_id': '0'}
    condition = {}
    for k, v in kwargs.items():
        kwargs[k] = int(v)
        if v == '0':
            pass
        else:
            condition[k] = v

    # # article_type_list = models.ArticleType.objects.all()
    article_type_list = models.Article.type_choice
    # print(article_type_list)
    category_list = models.Category.objects.all()
    result = models.Article.objects.filter(**condition)
    # print(result)
    return render(request, 'article.html', {'result': result,
                                            'article_type_list': article_type_list,
                                            'category_list': category_list,
                                            'arg_dict': kwargs
                                            }
                  )
