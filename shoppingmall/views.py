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

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def hello_word(request):
    return render(request, 'shoppingmall/hello_world.html')

@api_view(['GET'])
def health_check(request) :    
    logger.info("health checked.")
    return HttpResponse()
    

@api_view(['GET'])
def login(request):
    return render(request, 'login.html')

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
def commnet(request):
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
    additional = dict()
    additional['count'] = 10
    additional['list'] = ['팁스타운', '구의웰츠', '퓨처플레이']
    boards = get_board_list()
    # serializer = BoardsSerializer(boards, many=True)
    # data = json.loads(serialize('json', boards))
    # additional_j = json.dumps(additional)
    # additional = json.loads(serialize('json', additional_j))
    # return JsonResponse({'additionals': additional,'items': data})
    return HttpResponse(status=200)
    

@api_view(['GET'])
def board_detail(request):
    id = request.GET.get("id")
    board = get_board_detail(id)
    board_dict = dict()
    for b in board.values()[0]:
        if b == "created_time":
            board_dict[b] = board.values()[0][b].strftime('%Y-%m-%d')
            continue
        board_dict[b] = board.values()[0][b]
    
    comments = get_comment_by_id(id)
    comment_list = list()
    for c in comments:
        comment_list.append(c.contents)

    print(comment_list)

    board_dict['attachments'] = comment_list
    print(board_dict)

    response = json.dumps(board_dict)
    return HttpResponse(response, status=200, content_type="application/json")

    # additional = json.loads(serialize('json', board_dict))
    # return JsonResponse({'items': additional})

    # add = board_list + comments_list
    # print(add)
    # serializer = BoardsSerializer(board, many=True)
    # serializer = CommentsSerializer(comments, many=True)
    # return Response(serializer.data, status=200)