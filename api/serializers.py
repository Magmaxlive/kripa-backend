from rest_framework import serializers
from .models import *

class Hero_features_serializer(serializers.ModelSerializer):
    class Meta:
        model = Hero_features
        fields = "__all__"
        
     
class Hero_CTA_button_serializer(serializers.ModelSerializer):
    class Meta:
        model = Hero_CTA_button
        fields = "__all__"

class Hero_content_serializer(serializers.ModelSerializer):
    features = Hero_features_serializer(many = True,read_only = True)
    CTA = Hero_CTA_button_serializer(read_only = True)
    class Meta:
        model = Hero_content
        fields = "__all__"
        
               
        
class Hero_video_section_serializer(serializers.ModelSerializer):
    class Meta:
        model = Hero_video_section
        fields = "__all__"
        
        
class Partner_logos_serializer(serializers.ModelSerializer):
    class Meta:
        model = Partner_logos
        fields = "__all__"
        
        
class Services_serializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"
        
        
class Service_section_serializer(serializers.ModelSerializer):
    services = Services_serializer(many=True,read_only = True)
    
    class Meta:
        model = Service_section
        fields = "__all__"
        

class Whychooseus_points_serializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChoose_Points
        fields = "__all__"
        
class Whychooseus_counter_serializer(serializers.ModelSerializer):
    class Meta:
        model = Whychoose_Counter
        fields = "__all__"
        
class Whychooseus_cards_serializer(serializers.ModelSerializer):
    class Meta:
        model = Whychoose_us_cards
        fields = "__all__"
        
        
class Achievements_serializer(serializers.ModelSerializer):
    class Meta:
        model = Achievements
        fields = "__all__"
        
        
class Whychoose_us_section_serializer(serializers.ModelSerializer):
    cards = Whychooseus_cards_serializer(many=True,read_only=True)
    points = Whychooseus_points_serializer(many=True,read_only=True)
    counts = Whychooseus_counter_serializer(many=True,read_only=True)
    achievements = Achievements_serializer(many=True,read_only=True)
    
    class Meta:
        model = Whychoose_section
        fields = "__all__"
        

class Insights_video_serializer(serializers.ModelSerializer):
    class Meta :
        model = Insights_video
        fields = "__all__"    
        
        
class Insights_section_serializer(serializers.ModelSerializer):
    videos = Insights_video_serializer(many=True,read_only=True)
    class Meta :
        model = Insights_section
        fields = "__all__" 



class Testimonials_serializer(serializers.ModelSerializer):
    class Meta :
        model = Testimonials
        fields = "__all__"
        

class Members_serializer(serializers.ModelSerializer):
    class Meta :
        model = Accredited_members
        fields = "__all__"
        
        
class Testimonial_section_serializer(serializers.ModelSerializer):
    members = Members_serializer(many=True,read_only=True)
    testimonials = Testimonials_serializer(many=True,read_only=True)
    
    class Meta:
        model = Testimonials_section
        fields = "__all__"
        
        
class Home_calculator_serializer(serializers.ModelSerializer):
    class Meta :
        model = Home_calculator_section
        fields = "__all__"
        

class Contact_items_serializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
        

class Social_media_serializer(serializers.ModelSerializer):
    class Meta:
        model = Social_media
        fields = "__all__"
        
class Office_timings_serializer(serializers.ModelSerializer):
    class Meta:
        model = Office_timings
        fields = "__all__"
        
        
class Contact_card_serializer(serializers.ModelSerializer):
    social_media = Social_media_serializer(read_only=True)
    contacts = Contact_items_serializer(read_only=True)
    office_timings = Office_timings_serializer(read_only=True)
    class Meta:
        model = Contact_card_section
        fields = "__all__"


# about page 

class About_first_Section_serializer(serializers.ModelSerializer):
    class Meta :
        model = About_first_section
        fields = "__all__"
        
class Mission_vission_items_serializer(serializers.ModelSerializer):
    class Meta:
        model = Mission_vission_items
        fields = "__all__"
        
class Mission_vission_section_serializer(serializers.ModelSerializer):
    mission_vission_items = Mission_vission_items_serializer(many=True,read_only=True)
    class Meta:
        model = Mission_vission_section
        fields = "__all__"
  
  
class Core_values_serializer(serializers.ModelSerializer):
    class Meta:
        model = Core_value_items
        fields = "__all__"    
        
class Core_values_section_serializer(serializers.ModelSerializer):
    core_values = Core_values_serializer(many=True,read_only=True)
    class Meta:
        model = Our_core_values_section
        fields = "__all__"
        
        
class Team_members_serializer(serializers.ModelSerializer):
    class Meta :
        model = Team_members
        fields = "__all__"
        
        
class Team_section_serializer(serializers.ModelSerializer):
    members = Team_members_serializer(many=True,read_only=True)
    class Meta:
        model = Team_section
        fields = "__all__"
        
  
        
class Blogs_serializer(serializers.ModelSerializer):
    class Meta :
        model = Blogs
        fields = "__all__"
        
# blogs
        
class Blog_section_serializer(serializers.ModelSerializer):
    blogs = Blogs_serializer(many=True,read_only=True)
    class Meta:
        model = Blog_section
        fields = "__all__"       
      

# menus

class Menu_serializer(serializers.ModelSerializer):
    submenu = serializers.SerializerMethodField()
    
    class Meta:
        model = Menu
        fields = ['id','label','link','submenu']
        
    def get_submenu(self,obj):
        children = obj.submenu.filter(is_active=True)
        return Menu_serializer(children,many=True).data