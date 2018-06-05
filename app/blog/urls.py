from django.conf.urls import url
from .views import post_list, post_detail, post_create, post_delete

urlpatterns = [
    # url의 첫 번째 인자: 매치될 URL정규표현식
    # url의 두 번째 인자: view function
    #   view function
    #   ->  request를 받아서 response를 돌려주는 함수
    url(r'^$', post_list, name='post-list'),
    url(r'^(\d+)/$', post_detail, name='post-detail'),
    url(r'^write/$', post_create, name='post-create'),
    url(r'^\d+/delete/$', post_delete, name='post-delete'),
]
