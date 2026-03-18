from rest_framework import serializers
from api.models import *

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