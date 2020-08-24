from django.shortcuts import render

# Create your views here.
from utils import pagination

LIST = []
for i in range(1000):
    LIST.append(i)


def user_list(request):
    # 获取当前页
    current_page = request.GET.get('p', 1)
    current_page = int(current_page)

    page_obj = pagination.Page(current_page, len(LIST))

    start_page = page_obj.start
    end_page = page_obj.end

    # 每页的数据
    data = LIST[start_page:end_page]

    page_str = page_obj.page_str('/user_list/')
    return render(request, 'user_list.html', {'li': data, 'page_list': page_str})
