from .models import User
from .serializers import UserRegisterSerializer , LoginSerializer 
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated ,AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken, OutstandingToken
import random
from django.conf import settings
  
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistrationView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        try: 
            serializer = UserRegisterSerializer(data = request.data)
            if serializer.is_valid():
                validated_data = dict(serializer.data)
                if User.objects.filter(email=validated_data['email']).exists():
                    return Response({'msg' : 'User Alredy Exists'},status=status.HTTP_207_MULTI_STATUS)
                else:
                    user = User.objects.create_user(username = validated_data['username'] , email=validated_data['email'], password=validated_data['password'])
                    user.save()
                    return Response({'msg':'Registration Successful'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({
                'message' : 'Error on fetching',
                'Error' : error.__str__()
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class UserLoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                validated_date = dict(serializer.data)
                user = authenticate(email = validated_date['email'],
                                     password = validated_date['password'])
                if user:
                    return Response({"token" : get_tokens_for_user(user)})
                return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response(error,status=status.HTTP_500_INTERNAL_SERVER_ERROR)