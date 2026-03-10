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
    features = serializers.SerializerMethodField()
    CTA = serializers.SerializerMethodField()

    class Meta:
        model = Hero_content
        fields = "__all__"

    def get_features(self, obj):
        features = Hero_features.objects.all()
        return Hero_features_serializer(features, many=True).data

    def get_CTA(self,obj):
        cta = Hero_CTA_button.objects.first()
        if cta:
            return Hero_CTA_button_serializer(cta).data
        return None
        
               
        
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
    services = serializers.SerializerMethodField()
    
    class Meta:
        model = Service_section
        fields = "__all__"

    def get_services(self,obj):
        services = Service_category.objects.all()
        return Home_page_service_category(services,many=True,context=self.context).data

        
        

        

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
    cards = serializers.SerializerMethodField()
    points = serializers.SerializerMethodField()
    counts = serializers.SerializerMethodField()
    achievements = serializers.SerializerMethodField()
    
    class Meta:
        model = Whychoose_section
        fields = "__all__"

    def get_cards(self,obj):
        cards = Whychoose_us_cards.objects.all()
        return Whychooseus_cards_serializer(cards,many=True).data

    def get_points(self,obj):
        points = WhyChoose_Points.objects.all()
        return Whychooseus_points_serializer(points,many=True).data

    def get_counts(self,obj):
        counts = Whychoose_Counter.objects.all()
        return Whychooseus_counter_serializer(counts,many=True).data

    def get_achievements(self,obj):
        achievements = Achievements.objects.all()
        return Achievements_serializer(achievements,many=True,context=self.context).data
        

class Insights_video_serializer(serializers.ModelSerializer):
    class Meta :
        model = Insights_video
        fields = "__all__"    
        
        
class Insights_section_serializer(serializers.ModelSerializer):
    videos = serializers.SerializerMethodField()
    class Meta :
        model = Insights_section
        fields = "__all__" 

    def get_videos(self,obj):
        videos = Insights_video.objects.all()
        return Insights_video_serializer(videos,many=True).data



class Testimonials_serializer(serializers.ModelSerializer):
    class Meta :
        model = Testimonials
        fields = "__all__"
        

class Members_serializer(serializers.ModelSerializer):
    class Meta :
        model = Accredited_members
        fields = "__all__"
        
        
class Testimonial_section_serializer(serializers.ModelSerializer):
    members = serializers.SerializerMethodField()
    testimonials = serializers.SerializerMethodField()
    
    class Meta:
        model = Testimonials_section
        fields = "__all__"
        
    def get_testimonials(self,obj):
        testimonials = Testimonials.objects.all()
        return Testimonials_serializer(testimonials,many=True).data

    def get_members(self,obj):
        members = Accredited_members.objects.all()
        return Members_serializer(members,many=True).data
        
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
    social_media = serializers.SerializerMethodField()
    contacts = serializers.SerializerMethodField()
    office_timings = serializers.SerializerMethodField()

    class Meta:
        model = Contact_card_section
        fields = "__all__"

    def get_social_media(self,obj):
        social_media = Social_media.objects.first()
        return Social_media_serializer(social_media).data

    def get_contacts(self,obj):
        contacts = Contact.objects.first()
        return Contact_items_serializer(contacts).data

    def get_office_timings(self,obj):
        office_timings = Office_timings.objects.first()
        return Office_timings_serializer(office_timings).data


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
    mission_vission_items = serializers.SerializerMethodField()
    class Meta:
        model = Mission_vission_section
        fields = "__all__"

    def get_mission_vission_items(self,obj):
        mission_vission_items = Mission_vission_items.objects.all()
        return Mission_vission_items_serializer(mission_vission_items,many=True).data
  
  
class Core_values_serializer(serializers.ModelSerializer):
    class Meta:
        model = Core_value_items
        fields = "__all__"    
        
class Core_values_section_serializer(serializers.ModelSerializer):
    core_values = serializers.SerializerMethodField()
    class Meta:
        model = Our_core_values_section
        fields = "__all__"

    def get_core_values(self,obj):
        core_values = Core_value_items.objects.all()
        return Core_values_serializer(core_values,many=True).data
        
        
class Team_members_serializer(serializers.ModelSerializer):
    class Meta :
        model = Team_members
        fields = "__all__"
        
        
class Team_section_serializer(serializers.ModelSerializer):
    members = serializers.SerializerMethodField()
    class Meta:
        model = Team_section
        fields = "__all__"

    def get_members(self,obj):
        members = Team_members.objects.all()
        return Team_members_serializer(members,many=True,context=self.context).data
        
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


class Privacy_policy_serializer(serializers.ModelSerializer):
    class Meta:
        model = Privacy_policy
        fields = "__all__"

class Disclosure_serializer(serializers.ModelSerializer):
    class Meta:
        model = Disclosure_statement
        fields = "__all__"



class Career_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CareerPage
        fields = "__all__"


class Job_application_Serializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = "__all__"

class Enquiry_Serializer(serializers.ModelSerializer):
    class Meta:
        model = EnquiryForm
        fields = "__all__"