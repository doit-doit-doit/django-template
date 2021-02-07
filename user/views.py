import json

from django.views import View
from django.http import JsonResponse

from .models import User

class CreateView(View):
    def post(self, request):
        data = json.loads(request.body)
        User(
            email       = data['email'],
            password    = data['password'],
        )

        if User.objects.filter(email = data['email']).exists() == True:
            return JsonResponse({"message" : "이미 존재하는 아이디입니다."}, status = 401)

        else:
            User.objects.create(email = data['email'], password = data['password'])
            return JsonResponse({"message" : "회원으로 가입되셨습니다."}, status = 200)

    def get(self, request):
        users = User.objects.values()
        return JsonResponse({"data" : list(users)}, status = 200)