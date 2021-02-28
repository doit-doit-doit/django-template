import json
import logging
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import *
from shoppingmall.models.Boards import *
from shoppingmall.serializers import BoardsSerializer


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Create your views here.
@api_view(['GET'])
def health_check(request) :    
    logger.info("health checked.")
    return HttpResponse()

@api_view(['GET'])
def login(request):
    return render(request, 'login.html')

@api_view(['POST'])
def post(request):
    serializer = BoardsSerializer(data=request.data)
    try:
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    except Exception as e :
        return HttpResponseServerError()

@api_view(['GET'])
def board_list(request):
    # boards = get_board_list()
    # serializer = BoardsSerializer(boards, many=True)
    # boards_dict = dict(serializer.data)
    response = dict()
    response['title'] = "타이틀"
    response['name'] = "희수"
    response['description'] = "내용"
    response['attachments'] = ["img1", "img2", "img3"]
    json_resposne = json.dumps(response, indent=4, sort_keys=True)
    return Response(json_resposne)