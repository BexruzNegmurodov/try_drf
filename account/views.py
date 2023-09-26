from django.shortcuts import render
from django.contrib.auth import authenticate

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def token(request):
    # http://127.0.0.1:8000/api/account/token/
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    print(user)
    if user:
        auth_token, create = Token.objects.get_or_create(user=user)
        return Response(auth_token.key)
    return Response({'detail': 'user not fount'})
