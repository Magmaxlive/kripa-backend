from django.shortcuts import render
from rest_framework import generics,permissions
from api.models import *
from .serializers import *

# Create your views here.

class Hero_content_view(generics.RetrieveAPIView):
    serializer_class = Hero_content_Serializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        queryset = Hero_content.objects.first()
        return queryset
    
class Hero_content_update_view(generics.UpdateAPIView):
    serializer_class = Hero_content_Serializer
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'
    queryset = Hero_content.objects.all()
    
class Hero_video_view(generics.RetrieveAPIView):
    serializer_class = Hero_Video_Serializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        queryset = Hero_video_section.objects.first()
        return queryset
    
class Hero_video_update_view(generics.UpdateAPIView):
    serializer_class = Hero_Video_Serializer
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'
    queryset = Hero_video_section.objects.all()
    
    
class Hero_features_view(generics.ListCreateAPIView):
    queryset = Hero_features.objects.all()
    serializer_class = Hero_Feature_Serializer
    # permission_classes = [permissions.IsAuthenticated]


class Hero_features_update_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Hero_Feature_Serializer
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'
    queryset = Hero_features.objects.all()


class Partner_view(generics.ListCreateAPIView):
    serializer_class = Partner_serializer
    queryset = Partner_logos.objects.all()
    # permission_classes = [permissions.IsAuthenticated]

class Partner_detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Partner_serializer
    queryset = Partner_logos.objects.all()
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAuthenticated]

class Service_section_view(generics.RetrieveAPIView):
    serializer_class = Service_section_serializer

    def get_object(self):
        queryset = Service_section.objects.first()
        return queryset
    

class Service_section_Detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Service_section_serializer
    queryset = Service_section.objects.all()
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAuthenticated]
    


class Service_category_view(generics.ListCreateAPIView):
    serializer_class = Service_category_serializer
    queryset = Service_category.objects.all()
    # permission_classes = [permissions.IsAuthenticated]

class Service_category_detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Service_category_serializer
    queryset = Service_category.objects.all()
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAuthenticated]


class Whychoose_section_view(generics.RetrieveAPIView):
    serializer_class = Whychose_serializer

    def get_object(self):
        queryset = Whychoose_section.objects.first()
        return queryset
    

class Whychoose_section_Detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Whychose_serializer
    queryset = Whychoose_section.objects.all()
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAuthenticated]
    

class Whychoose_cards_view(generics.ListCreateAPIView):
    serializer_class = Cards_serializer
    queryset = Whychoose_us_cards.objects.all()

class Whychoose_cards_detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Cards_serializer
    queryset = Whychoose_us_cards.objects.all()
    lookup_field = 'pk'


class Whychoose_points_view(generics.ListCreateAPIView):
    serializer_class = Points_serializer
    queryset = WhyChoose_Points.objects.all()

class Whychoose_Points_detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Points_serializer
    queryset = WhyChoose_Points.objects.all()
    lookup_field = 'pk'


class Whychoose_counter_view(generics.ListCreateAPIView):
    serializer_class = Counter_serializer
    queryset = Whychoose_Counter.objects.all()

class Whychoose_counter_detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Counter_serializer
    queryset = Whychoose_Counter.objects.all()
    lookup_field = 'pk'


class Achievments_view(generics.ListCreateAPIView):
    serializer_class = Achievments_serializer
    queryset = Achievements.objects.all()

class Achievments_detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Achievments_serializer
    queryset = Achievements.objects.all()
    lookup_field = 'pk'  
    

class Insights_section_view(generics.RetrieveAPIView):
    serializer_class = Insights_serializer

    def get_object(self):
        queryset = Insights_section.objects.first()
        return queryset
    

class Insights_section_Detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Insights_serializer
    queryset = Insights_section.objects.all()
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAuthenticated]
    

class insight_video_view(generics.ListCreateAPIView):
    serializer_class = Insight_video_serializer
    queryset = Insights_video.objects.all()

class insight_video_detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Insight_video_serializer
    queryset = Insights_video.objects.all()
    lookup_field = 'pk'



class Testimonial_section_view(generics.RetrieveAPIView):
    serializer_class = Testimonial_section_serializer

    def get_object(self):
        queryset = Testimonials_section.objects.first()
        return queryset
    

class Testimonial_section_Detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Testimonial_section_serializer
    queryset = Testimonials_section.objects.all()
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAuthenticated]
    

class Testimonial_view(generics.ListCreateAPIView):
    serializer_class = Testimonials_serializer
    queryset = Testimonials.objects.all()

class Testimonials_detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Testimonials_serializer
    queryset = Testimonials.objects.all()
    lookup_field = 'pk'


class Accredited_view(generics.ListCreateAPIView):
    serializer_class = Accredited_serializer
    queryset = Accredited_members.objects.all()

class Accredited_detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Accredited_serializer
    queryset = Accredited_members.objects.all()
    lookup_field = 'pk'


class About_section_view(generics.RetrieveAPIView):
    serializer_class = About_first_serializer

    def get_object(self):
        queryset = About_first_section.objects.first()
        return queryset
    

class About_section_Detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = About_first_serializer
    queryset = About_first_section.objects.all()
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAuthenticated]


class Mission_vission_section_view(generics.RetrieveAPIView):
    serializer_class = Mission_vission_Section_serializer

    def get_object(self):
        queryset = Mission_vission_section.objects.first()
        return queryset
    

class Mission_vission_section_Detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Mission_vission_Section_serializer
    queryset = Mission_vission_section.objects.all()
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAuthenticated]


class Mission_vission_view(generics.ListCreateAPIView):
    serializer_class = Mission_vission_items_serializer
    queryset = Mission_vission_items.objects.all()

class Mission_vission_detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Mission_vission_items_serializer
    queryset = Mission_vission_items.objects.all()
    lookup_field = 'pk'
