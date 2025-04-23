from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer, UserAuthSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

@api_view(['GET'])
def authorization_api_view(request):
    serializer = UserAuthSerializer(request.user)
    serializer.is_valid(raise_exception=True)

    user = authenticate(**serializer.validated_data)

    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    return Response(status=status.HTTP_401_UNAUTHORIZED,
                    data={'error': 'User credential are wrong!'})

@api_view(['POST'])
def registration_api_view(request):
    serializer = UserRegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data['username']
    password = serializer.validated_data['password']

    user = User.objects.create_user(username=username,
                                    password=password,
                                    is_active=False)

    return Response(status=status.HTTP_201_CREATED,
                    data={'user_id': user.id})