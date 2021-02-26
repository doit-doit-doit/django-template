
from django.urls import path
from . import views

urlpatterns = [
    path('healthcheck', views.health_check),
    path('login', views.login),
    path('post', views.post),
    path('posts', views.board_list)
] 