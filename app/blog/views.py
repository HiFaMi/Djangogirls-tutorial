import os

from django.http import HttpResponse
from django.template.loader import render_to_string


def post_list(request):

    # cur_file_path = os.path.abspath(__file__)
    # dir_name = os.path.dirname(cur_file_path)
    # app_dir_name = os.path.dirname(dir_name)
    # second_dir = os.path.join(app_dir_name, 'templates')
    # third_dir = os.path.join(second_dir, 'blog', 'post_list.html')
    # html = open(third_dir, 'rt').read()

    # 경로에 해당하는 HTML파일을 문자열로 로드
    html = render_to_string('blog/post_list.html')
    # 가져온 문자열 돌려주기
    return HttpResponse(html)
