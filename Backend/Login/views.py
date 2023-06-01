from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.authentication import SessionAuthentication
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from rest_framework.authtoken.models import Token

from rest_framework.views import APIView
from .serializer import UserSerializer
from .models import User
import jwt
from django.core.cache import cache


class UserView(APIView):
    # register
    def post(self, request):
        uid = request.data.get('uid')
        password = request.data.get('password')
        username = request.data.get('username')
        uid_check = User.objects.all().filter(uid=uid)
        if uid_check.exists():
            return Response({'status':'occupied'},status=status.HTTP_200_OK)
        else:
            new_user = User()
            new_user.set_user_info(username=username, password=password, uid=uid)
            new_user.save()
            return Response({'status':'true'},status=status.HTTP_200_OK)

# login     
class TokenView(APIView):
    def post(self, request):
        # token = request.headers['token']
        # print(token)
        password = request.data.get('password')
        uid: str = request.data.get('uid')
        
        if not User.check_user_exists(uid):
            return Response({'status':'user-not-exist'}, status=status.HTTP_200_OK)
        else:
            if not User.check_password(uid=uid, password=password):
                return Response({'status':'password-not-correct'}, status=status.HTTP_200_OK)
            else:
                token = {
                    'uid': uid, 
                }
                token = jwt.encode(token, "secret")
                headers = {
                    'token': token,
                    'access-control-expose-headers': 'token'
                }
                cache.add(token, 'logged')
                resp = Response({'status':'true'}, status=status.HTTP_200_OK, headers=headers)
                return resp     

class ListUsersView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
