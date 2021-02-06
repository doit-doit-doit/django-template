
import logging
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse

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