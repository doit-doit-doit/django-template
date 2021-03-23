import datetime
import json
import logging

# from rest_framework import viewsets
from shoppingmall.models import Boards
from shoppingmall.models import Comments
from shoppingmall.serializers import BoardsSerializer
from shoppingmall.serializers import CommentsSerializer
from shoppingmall.models.Boards import get_board_list, get_board_detail
from shoppingmall.models.Comments import get_comment_by_id


from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import *
from django.core.serializers import serialize

from datetime import datetime

# TODO : refactoring
logger = logging.Logger("MYLOG")
format = "[%(name)s] (%(filename)s:%(lineno)d/%(message)s"
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(format, datefmt="%Y-%m-%d %H:%M:%S"))
handler.setLevel(logging.INFO)
logger.addHandler(handler)

def hello_word(request):
    return render(request, 'shoppingmall/hello_world.html')

@api_view(['GET'])
def health_check(request) :    
    logger.info("health checked) - health checked")
    return HttpResponse()
    

@api_view(['GET'])
def login(request):
    return render(request, 'shoppingmall/login.html')

# class BoardViewSet(viewsets.ModelViewSet) :
#     queryset = Boards.objects.all()
#     serializer_class = BoardsSerializer

# class CommentViewSet(viewsets.ModelViewSet) :
#     queryset = Comments.objects.all()
#     serializer_class = CommentsSerializer

@api_view(['POST'])
def post(request):
    serializer = BoardsSerializer(data=request.data)
    try:
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    except Exception as e :
        return HttpResponseServerError()

@api_view(['POST'])
def comment(request):
    serializer = CommentsSerializer(data=request.data)
    try:
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    except Exception as e :
        print(e)
        return HttpResponseServerError()

@api_view(['GET'])
def board_list(request):
    response_dict = dict()
    response_dict['board_list'] = dict()
    boards = get_board_list()
    board_list = list()
    board_dict = dict()
    for b in boards:
        board_dict['id'] = b[0]
        board_dict['title'] = b[1]
        board_dict['name'] = b[2]
        board_dict['description'] = b[3]
        board_dict['created_time'] = b[4].strftime("%Y-%m-%d %H:%M:%S")
        board_list.append(board_dict)
        board_dict = dict()
    response_dict['board_list'] = board_list
    response = json.dumps(response_dict)
    return HttpResponse(response, status=200, content_type="application/json")
    

@api_view(['GET'])
def board_detail(request):
    id = request.GET.get("id")
    board = get_board_detail(id)
    board_list = list(board)
    board_dict = dict()
    board_dict['id'] = board[0]
    board_dict['title'] = board[1]
    board_dict['name'] = board[2]
    board_dict['description'] = board[3]
    board_dict['created_time'] = board[4].strftime("%Y-%m-%d %H:%M:%S")

    response = json.dumps(board_dict)
    return HttpResponse(response, status=200, content_type="application/json")