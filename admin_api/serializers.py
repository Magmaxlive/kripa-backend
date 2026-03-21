from rest_framework import serializers
from api.models import *
from django.contrib.auth.models import User

class Hero_content_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Hero_content
        fields = "__all__"

class Hero_Video_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Hero_video_section
        fields = "__all__"

class Hero_Feature_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Hero_features
        fields = "__all__"

class Partner_serializer(serializers.ModelSerializer):
    class Meta:
        model = Partner_logos
        fields = "__all__"

class Service_section_serializer(serializers.ModelSerializer):
    class Meta:
        model = Service_section
        fields = "__all__"


class Service_category_serializer(serializers.ModelSerializer):
    class Meta:
        model = Service_category
        fields = "__all__"


class Whychose_serializer(serializers.ModelSerializer):
    class Meta:
        model = Whychoose_section
        fields = "__all__"

class Points_serializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChoose_Points
        fields = "__all__"


class Cards_serializer(serializers.ModelSerializer):
    class Meta:
        model = Whychoose_us_cards
        fields = "__all__"


class Counter_serializer(serializers.ModelSerializer):
    class Meta:
        model = Whychoose_Counter
        fields = "__all__"


class Achievments_serializer(serializers.ModelSerializer):
    class Meta:
        model = Achievements
        fields = "__all__"


class Insights_serializer(serializers.ModelSerializer):
    class Meta:
        model = Insights_section
        fields = "__all__"

class Insight_video_serializer(serializers.ModelSerializer):
    class Meta:
        model = Insights_video
        fields = "__all__"


class Testimonial_section_serializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials_section
        fields = "__all__"

class Testimonials_serializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = "__all__"


class Accredited_serializer(serializers.ModelSerializer):
    class Meta:
        model = Accredited_members
        fields = "__all__"


class About_first_serializer(serializers.ModelSerializer):
    class Meta:
        model = About_first_section
        fields = "__all__"


class Mission_vission_Section_serializer(serializers.ModelSerializer):
    class Meta:
        model = Mission_vission_section
        fields = "__all__"


class Mission_vission_items_serializer(serializers.ModelSerializer):
    class Meta:
        model = Mission_vission_items
        fields = "__all__"



class Core_values_Section_serializer(serializers.ModelSerializer):
    class Meta:
        model = Our_core_values_section
        fields = "__all__"


class Core_values_serializer(serializers.ModelSerializer):
    class Meta:
        model = Core_value_items
        fields = "__all__"


class Category_faq_serializer(serializers.ModelSerializer):
    class Meta:
        model = Category_faq
        fields = "__all__"


class Team_Section_serializer(serializers.ModelSerializer):
    class Meta:
        model = Team_section
        fields = "__all__"


class Team_Member_serializer(serializers.ModelSerializer):
    class Meta:
        model = Team_members
        fields = "__all__"


class Contact_card_Section_serializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_card_section
        fields = "__all__"


class Contact_serializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class Social_media_serializer(serializers.ModelSerializer):
    class Meta:
        model = Social_media
        fields = "__all__"


class Office_time_serializer(serializers.ModelSerializer):
    class Meta:
        model = Office_timings
        fields = "__all__"


class Services_serializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"



class Service_faq_serializer(serializers.ModelSerializer):
    class Meta:
        model = Service_faq
        fields = "__all__"



class Blogs_serializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class User_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"




class ThemeSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ThemeSettings
        fields = "__all__"



class Career_page_Seriazlizer(serializers.ModelSerializer):
    class Meta:
        model = CareerPage
        fields = "__all__"
