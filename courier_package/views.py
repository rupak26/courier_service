from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework import status
from rest_framework.permissions import IsAuthenticated , AllowAny
from .serializers import PackageSerializer
from .models import User , Package
from django.utils import timezone
from rest_framework.pagination import LimitOffsetPagination

class PackageView(APIView):
    permission_classes = [IsAuthenticated]
    
    #If Logged user want to create a package
    def post(self,request):
        try:
            serializer = PackageSerializer(data = request.data)
            if not serializer.is_valid():
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
            validate_data = dict(serializer.data)
            new_package = Package.objects.create(
                sender_name = User(request.user.id),
                recipient_name = validate_data['recipient_name'] ,
                recipient_address = validate_data['recipient_address'] ,
            )
            new_package.save()
            full_Package = PackageSerializer(new_package)
            return Response(full_Package.data,status=status.HTTP_200_OK)  
        except Exception as error:
            return Response({
                'message' : 'Error on fetching',
                'Error' : error.__str__()
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    #If Logged user want to update full a package 
    def put(self,request):
        try:
            package = Package.objects.filter(
                id = request.query_params.get('id') ,
                sender_name = request.user.id ,
                is_deleted = False
            ).last()
            if not package:
               return Response({'msg':'Package Does Not Matched'},status=status.HTTP_404_NOT_FOUND)
            serializer = PackageSerializer(package ,data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
            serializer.save(updated_at = timezone.now())
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as error:
            return Response({
                'message' : 'Error on fetching',
                'Error' : error.__str__()
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    #If Logged user want to update Part of a package 
    def patch(self,request):
        try:
            package = Package.objects.filter(
                id = request.query_params.get('id') ,
                sender_name = request.user.id ,
                is_deleted = False
            ).last()
            if not package:
               return Response({'msg':'Package Does Not Matched'},status=status.HTTP_404_NOT_FOUND)
            serializer = PackageSerializer(package,data=request.data,partial=True)
            
            if not serializer.is_valid():
                return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
            
            serializer.save(updated_at = timezone.now())
            
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as error:
            return Response({
                'message' : 'Error on fetching',
                'Error' : error.__str__()
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    #If Logged user want to soft delete a package
    def delete(self,request):
        try:
            package = Package.objects.filter(
                    id = request.query_params.get('id') ,
                    sender_name = request.user.id ,
                    is_deleted = False
                ).last()
            if not package:
               return Response({'msg':'Package Does Not Matched'},status=status.HTTP_404_NOT_FOUND)
            
            #package.delete()
            package.is_deleted = True 
            package.save()
            return Response({'msg' : 'Content Deleted'},status=status.HTTP_200_OK)
        except Exception as error:
            return Response({
                'message' : 'Error on fetching',
                'Error' : error.__str__()
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
    #If Logged user want to Track all his/her package 
    def get(self, request):
        try:
            created_by = request.user.id
            package = Package.objects.filter(
                sender_name = created_by
            ).values()
            if not package:
                return Response({
                    'message':'Package Not Found'}
                    ,status=status.HTTP_404_NOT_FOUND)
            
            return Response(package , status=status.HTTP_200_OK)
            
        except Exception as error:
            return Response({
                'message' : 'Error on fetching',
                'Error' : error.__str__()
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    