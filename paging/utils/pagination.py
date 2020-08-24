from django.utils.safestring import mark_safe


class Page:
    '''
    分页类
    current_page:当前页
    count:总页数
    pag_view_count:每页显示的数据数量
    page_pagination:每页显示的页码数量
    '''

    def __init__(self, current_page, count, pag_view_count=10, page_pagination=7):
        self.current_page = current_page
        self.count = count
        self.pag_view_count = pag_view_count
        self.page_pagination = page_pagination

    @property
    def start(self):
        # 页开始位置
        return (self.current_page - 1) * self.pag_view_count

    @property
    def end(self):
        # 页结束位置
        return self.current_page * self.pag_view_count

    def count(self):
        # 总页数
        count, y = divmod(self.count, self.pag_view_count)
        if y:
            count += 1
        return count

    def page_str(self, base_url):
        # 定义页码
        page_list = []
        if self.count < self.page_pagination:
            start_index = 1
            end_index = self.count + 1
        else:
            if self.current_page <= (self.page_pagination + 1) / 2:
                start_index = 1
                end_index = self.page_pagination + 1
            else:
                start_index = self.current_page - (self.page_pagination + 1) / 2 + 1
                end_index = self.current_page + (self.page_pagination + 1) / 2
                if self.current_page + (self.page_pagination + 1) / 2 > self.count:
                    start_index = self.count - self.page_pagination + 1
                    end_index = self.count + 1

        if self.current_page == 1:
            prev = '<a class="page" href="javascript:void(0)">上一页</a>'
        else:
            prev = '<a class="page" href="%s?p=%s">上一页</a>' % (base_url, self.current_page - 1,)
        page_list.append(prev)
        for i in range(int(start_index), int(end_index)):
            if i == self.current_page:
                temp = '<a class="page active" href="%s?p=%s">%s</a>' % (base_url, i, i)
            else:
                temp = '<a class="page" href="%s?p=%s">%s</a>' % (base_url, i, i)
            page_list.append(temp)

        if self.current_page == self.count:
            prev = '<a class="page" href="javascript:void(0)">下一页</a>'
        else:
            prev = '<a class="page" href="%s?p=%s">下一页</a>' % (base_url, self.current_page + 1,)
        page_list.append(prev)

        # jump = '''
        # <input type="text" /><a onclick="ToPage(this.'/user_list/?=');">跳转</a>
        # <script>
        #     function ToPage(this,base){
        #         var val = this.previousSibling.value;
        #         location.href = base + val;
        #     }
        # </script>
        # '''
        # page_list.append(jump)
        page_list = ''.join(page_list)
        page_str = mark_safe(page_list)
        return page_str
