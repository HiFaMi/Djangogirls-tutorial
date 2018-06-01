import os

from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):

    cur_file_path = os.path.abspath(__file__)
    dir_name = os.path.dirname(cur_file_path)
    app_dir_name = os.path.dirname(dir_name)
    second_dir = os.path.join(app_dir_name, 'templates')
    third_dir = os.path.join(second_dir, 'blog', 'post_list.html')
    html = open(third_dir, 'rt').read()
    return HttpResponse(html)
