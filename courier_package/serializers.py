from .models import User , Package
from rest_framework import serializers

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'
        read_only_fields = ['sender_name', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        return Package.create(validated_data)