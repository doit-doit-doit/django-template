import logging
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import *
from .models import Boards
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
    boards = Boards.objects.all()
    serializer = BoardsSerializer(boards, many=True)
    return Response(serializer.data)