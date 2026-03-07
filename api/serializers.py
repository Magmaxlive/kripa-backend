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
        

        
class Services_category_serializer(serializers.ModelSerializer):
    class Meta:
        model = Service_category
        fields = "__all__"
        
        
class Category_faq_serializer(serializers.ModelSerializer):
    class Meta:
        model = Category_faq
        fields = "__all__"      
        
        
class Services_faq_serializer(serializers.ModelSerializer):
    class Meta:
        model = Service_faq
        fields = "__all__"     
        
class Services_serializer(serializers.ModelSerializer):
    category_title = serializers.CharField(source="category.title", read_only=True)
    category_slug = serializers.CharField(source="category.slug", read_only=True)
    faq = Services_faq_serializer(many=True,read_only=True)

    class Meta:
        model = Services
        fields = "__all__"
        
        
class Home_page_service_category(serializers.ModelSerializer):
    class Meta:
        model = Service_category
        fields = "__all__"
        
class Services_category_serializer(serializers.ModelSerializer):
    services = Services_serializer(many=True,read_only=True)
    faq = Category_faq_serializer(many=True,read_only=True)
    class Meta:
        model = Service_category
        fields = "__all__"
        
class Service_section_serializer(serializers.ModelSerializer):
    services = Home_page_service_category(many=True,read_only = True)
    
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
        
class Blog_category_serializer(serializers.ModelSerializer):
    class Meta:
        model = Blog_category
        fields = "__all__"
        
class Blogs_serializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = Blog_category_serializer()
    class Meta :
        model = Blog
        fields = "__all__"
        
# blogs
        
      
      

# menus

class Menu_serializer(serializers.ModelSerializer):
    submenu = serializers.SerializerMethodField()
    
    class Meta:
        model = Menu
        fields = ['id','label','link','submenu']
        
    def get_submenu(self,obj):
        children = obj.submenu.filter(is_active=True).order_by('order')
        return Menu_serializer(children,many=True).data
    
    
class Header_serializer(serializers.ModelSerializer):
    menu = serializers.SerializerMethodField()
    class Meta :
        model = Header
        fields = "__all__"
        
        
    def get_menu(self,obj):
        root_items = obj.menu.filter(parent=None,is_active=True).order_by('order')
        return Menu_serializer(root_items,many=True).data
        
     
# footer section

class Footer_email_serializer(serializers.ModelSerializer) :
    class Meta :
        model = Footer_emails
        fields = "__all__"  
        

class Footer_links_serializer(serializers.ModelSerializer):
    class Meta:
        model = Footer_links
        fields = "__all__"
        
        
class Footer_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = "__all__"
