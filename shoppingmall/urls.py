# from django.conf.urls import url
from django.urls import path
# from shoppingmall.views import BoardViewSet
# from shoppingmall.views import CommentViewSet
from . import views

app_name = "shoppingmall"

urlpatterns = [
    path('healthcheck', views.health_check),
    path('login', views.login),
    path('post', views.post),
    path('comment', views.commnet),
    path('posts', views.board_list),
    path('postdetail', views.board_detail)
    # url('board', BoardViewSet({'get':'list', 'post':'create'})),
    # url('comment', CommentViewSet({'get':"list", 'post':'create'})),
] 