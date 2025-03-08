from rest_framework import routers, serializers, viewsets

class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()
    
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
        
