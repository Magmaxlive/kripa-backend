from django.shortcuts import render
from rest_framework import generics,permissions
from api.models import *
from api.serializers import *

# Create your views here.

class Hero_content_view(generics.ListCreateAPIView):
    queryset = Hero_content.objects.all()
    serializer_class = Hero_content_serializer
    permission_classes = [permissions.IsAuthenticated]
    
    
class Hero_features_view(generics.ListCreateAPIView):
    queryset = Hero_features.objects.all()
    serializer_class = Hero_features_serializer
    permission_classes = [permissions.IsAuthenticated]
    
    
class Hero_CTA_button_view(generics.ListCreateAPIView):
    queryset = Hero_CTA_button.objects.all()
    serializer_class = Hero_CTA_button_serializer
    permission_classes = [permissions.IsAuthenticated]
    
    

