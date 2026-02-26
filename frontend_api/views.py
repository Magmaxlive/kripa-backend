from django.shortcuts import render
from rest_framework import generics
from api.models import *
from api.serializers import *

# Create your views here.

class Hero_content_view(generics.RetrieveAPIView):
    serializer_class = Hero_content_serializer
    
    def get_object(self):
        queryset = Hero_content.objects.first()
        return queryset
    
    
class Hero_video_section_view(generics.RetrieveAPIView):
    serializer_class = Hero_video_section_serializer
    
    def get_object(self):
        queryset = Hero_video_section.objects.first()
        return queryset
    

class Partner_logos_view(generics.ListAPIView):
    queryset = Partner_logos.objects.all()
    serializer_class = Partner_logos_serializer
    
    
class Service_section_view(generics.RetrieveAPIView):
    serializer_class = Service_section_serializer
    
    def get_object(self):
        queryset = Service_section.objects.first()
        return queryset
    
    
class Whychoose_us_section_view(generics.RetrieveAPIView):
    serializer_class = Whychoose_us_section_serializer
    
    def get_object(self):
        queryset = Whychoose_section.objects.first()
        return queryset
    
    
class Insights_section_view(generics.RetrieveAPIView):
    serializer_class = Insights_section_serializer
    
    def get_object(self):
        queryset = Insights_section.objects.first()
        return queryset
    
    
class Testimonials_section_view(generics.RetrieveAPIView):
    serializer_class = Testimonial_section_serializer
    
    def get_object(self):
        queryset = Testimonials_section.objects.first()
        return queryset
    
    
class Home_calculator_section_view(generics.RetrieveAPIView):
    serializer_class = Home_calculator_serializer
    
    def get_object(self):
        queryset = Home_calculator_section.objects.first()
        return queryset


class Contact_section_view(generics.RetrieveAPIView):
    serializer_class = Contact_card_serializer
    
    def get_object(self):
        queryset = Contact_card_section.objects.first()
        return queryset
    
    
class About_section_view(generics.RetrieveAPIView):
    serializer_class = About_first_Section_serializer
    
    def get_object(self):
        queryset = About_first_section.objects.first()
        return queryset
    
    
    
class Mission_vission_section_view(generics.RetrieveAPIView):
    serializer_class = Mission_vission_section_serializer
    
    def get_object(self):
        queryset = Mission_vission_section.objects.first()
        return queryset
    
    
class Core_values_section_view(generics.RetrieveAPIView):
    serializer_class = Core_values_section_serializer
    
    def get_object(self):
        queryset = Our_core_values_section.objects.first()
        return queryset
    
    
class Team_section_view(generics.RetrieveAPIView):
    serializer_class = Team_section_serializer
    
    def get_object(self):
        queryset = Team_section.objects.first()
        return queryset
    
    
    
class Blog_section_view(generics.RetrieveAPIView):
    serializer_class = Blog_section_serializer
    
    def get_object(self):
        queryset = Blog_section.objects.first()
        return queryset
    
class Menu_view(generics.ListAPIView):
    serializer_class = Menu_serializer
    
    def get_queryset(self):
        return Menu.objects.filter(parent__isnull=True)