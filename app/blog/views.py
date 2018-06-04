from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def post_list(request):

    # cur_file_path = os.path.abspath(__file__)
    # dir_name = os.path.dirname(cur_file_path)
    # app_dir_name = os.path.dirname(dir_name)
    # second_dir = os.path.join(app_dir_name, 'templates')
    # third_dir = os.path.join(second_dir, 'blog', 'post_list.html')
    # html = open(third_dir, 'rt').read()

    # 경로에 해당하는 HTML파일을 문자열로 로드
    # html = render_to_string('blog/post_list.html')
    # 가져온 문자열 돌려주기
    # return HttpResponse(html)

    # result = '글 목록<br>'
    #
    # for post in Post.objects.all():
    #     result += '{}<br>'.format(post.title)
    #
    # return HttpResponse(result)
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    # render는 주어진 1,2번째 인수를 사용해서
    # 1번째 인수: HttpRequest 인스턴스
    # 2번째 인수: 문자열 (TEMPLATE['DIRS']를 기준으로 탐색할 템플릿 파일의 경로)
    # 3번쨰 인수: 템플릿을 렌더링 할때 사용할 객체 모음
    return render(request, 'blog/post_list.html', context)


