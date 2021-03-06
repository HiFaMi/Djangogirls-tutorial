from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
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
    posts = Post.objects.order_by('-id')
    context = {
        'posts': posts
    }
    # render는 주어진 1,2번째 인수를 사용해서
    # 1번째 인수: HttpRequest 인스턴스
    # 2번째 인수: 문자열 (TEMPLATE['DIRS']를 기준으로 탐색할 템플릿 파일의 경로)
    # 3번쨰 인수: 템플릿을 렌더링 할때 사용할 객체 모음
    return render(request, 'blog/post_list.html', context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)


def post_create(request):
    if request.method == 'POST':
        new_title = request.POST.get('title')
        new_text = request.POST.get('text')
        user = User.objects.get(username='mingyu')
        new_post = Post.objects.create(author=user, title=new_title, text=new_text)
        return redirect('post-list')

    else:
        return render(request, 'blog/post_create.html')


def post_delete(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        post.delete()

    return redirect('post-list')


def post_edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']

        post.title = title
        post.text = text
        post.save()

        return redirect('post-detail', post.id)


def post_edit_create(request, post_id=None):
    def edit_process(post):
        post.title = title
        post.text = text
        post.save()
        return redirect('post-detail', post.id)

    def create_process(title, text):
        Post.objects.create(
            author=request.user,
            title=title,
            text=text,
        )
        return redirect('post-list')

    context = {}
    if post_id:
        context['post'] = Post.objects.get(id=post_id)

    if request.method == 'POST':
        post = context.get('post')
        title = request.POST['title']
        text = request.POST['text']
        if post:
            return edit_process(post)
        else:
            return create_process(title, text)
    return render(request, 'blog/post_edit_create.html', context)

