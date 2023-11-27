from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from auth.serializers import CustomUserCreateSerializer, CustomUserSerializer

class CustomUserViewSet(ModelViewSet):
    queryset = CustomUserSerializer.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'create':
            return CustomUserCreateSerializer
        return CustomUserSerializer
        
        