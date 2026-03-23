from django.shortcuts import render
from rest_framework import generics,permissions
from api.models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from api.serializers import *

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


class Core_values_section_view(generics.RetrieveAPIView):
    serializer_class = Core_values_Section_serializer

    def get_object(self):
        queryset = Our_core_values_section.objects.first()
        return queryset
    

class Core_values_section_Detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Core_values_Section_serializer
    queryset = Our_core_values_section.objects.all()
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAuthenticated]


class Core_values_view(generics.ListCreateAPIView):
    serializer_class = Core_values_serializer
    queryset = Core_value_items.objects.all()

class Core_values_detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Core_values_serializer
    queryset = Core_value_items.objects.all()
    lookup_field = 'pk'


class Category_faq_view(generics.ListCreateAPIView):
    serializer_class = Category_faq_serializer
    queryset = Category_faq.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']


class Category_faq_detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Category_faq_serializer
    queryset = Category_faq.objects.all()
    lookup_field = 'pk'



class Team_section_view(generics.RetrieveAPIView):
    serializer_class = Team_Section_serializer

    def get_object(self):
        queryset = Team_section.objects.first()
        return queryset
    

class Team_section_Detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Team_Section_serializer
    queryset = Team_section.objects.all()
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAuthenticated]



class Team_members_view(generics.ListCreateAPIView):
    serializer_class = Team_Member_serializer
    queryset = Team_members.objects.all()
    


class Team_member_detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Team_Member_serializer
    queryset = Team_members.objects.all()
    lookup_field = 'pk'



class Contact_card_section_view(generics.RetrieveAPIView):
    serializer_class = Contact_card_Section_serializer

    def get_object(self):
        queryset = Contact_card_section.objects.first()
        return queryset
    

class contact_card_section_Detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Contact_card_Section_serializer
    queryset = Contact_card_section.objects.all()
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAuthenticated]



class Contact_view(generics.RetrieveAPIView):
    serializer_class = Contact_serializer

    def get_object(self):
        queryset = Contact.objects.first()
        return queryset
    

class contact_Detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Contact_serializer
    queryset = Contact.objects.all()
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAuthenticated]


class Social_media_view(generics.RetrieveAPIView):
    serializer_class = Social_media_serializer

    def get_object(self):
        queryset = Social_media.objects.first()
        return queryset
    

class Social_media_Detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Social_media_serializer
    queryset = Social_media.objects.all()
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAuthenticated]


class Office_time_view(generics.RetrieveAPIView):
    serializer_class = Office_time_serializer

    def get_object(self):
        queryset = Office_timings.objects.first()
        return queryset
    

class Office_time_Detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Office_time_serializer
    queryset = Office_timings.objects.all()
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAuthenticated]



class Services_view(generics.ListCreateAPIView):
    serializer_class = Services_serializer
    queryset = Services.objects.all()

class Services_detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Services_serializer
    queryset = Services.objects.all()
    lookup_field = 'pk'



class Service_faq_view(generics.ListCreateAPIView):
    serializer_class = Service_faq_serializer
    queryset = Service_faq.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['service']


class Service_faq_detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Service_faq_serializer
    queryset = Service_faq.objects.all()
    lookup_field = 'pk'


class Blogs_view(generics.ListCreateAPIView):
    serializer_class = Blogs_serializer
    queryset = Blog.objects.all()


class Blogs_detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Blogs_serializer
    queryset = Blog.objects.all()
    lookup_field = 'pk'


class User_View(generics.ListAPIView):
    serializer_class = User_serializer
    queryset = User.objects.all()



@csrf_exempt
@api_view(['POST'])
def upload_image(request):
    print(">>> upload_image HIT")
    print(">>> FILES:", request.FILES)
    file = request.FILES.get('upload')
    if not file:
        return Response({"error": "No file"}, status=400)
    obj = UploadedImage.objects.create(image=file)
    return Response({"url": request.build_absolute_uri(obj.image.url)})


@api_view(["GET"])
# @permission_classes([AllowAny])
def get_theme(request):
    obj, _ = ThemeSettings.objects.get_or_create(pk=1)
    return Response(ThemeSettingsSerializer(obj).data)
 
@api_view(["PATCH"])
# @permission_classes([IsAuthenticated])
def update_theme(request):
    obj, _ = ThemeSettings.objects.get_or_create(pk=1)
    serializer = ThemeSettingsSerializer(obj, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
 
@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def reset_theme(request):
    obj, _ = ThemeSettings.objects.get_or_create(pk=1)
    for field, value in DEFAULT_THEME.items():
        setattr(obj, field, value)
    obj.save()
    return Response(ThemeSettingsSerializer(obj).data)


class Career_Page_view(generics.RetrieveAPIView):
    serializer_class = Career_page_Seriazlizer

    def get_object(self):
        queryset = CareerPage.objects.first()
        return queryset
    

class Career_page_Detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Career_page_Seriazlizer
    queryset = CareerPage.objects.all()
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAuthenticated]


class General_faq_view(generics.ListCreateAPIView):
    serializer_class = General_faq_serializer
    queryset = General_faqs.objects.all()



class General_faq_detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = General_faq_serializer
    queryset = General_faqs.objects.all()
    lookup_field = 'pk'


class Privacy_policy_view(generics.RetrieveAPIView):
    serializer_class = Privacy_policy_serializer

    def get_object(self):
        queryset = Privacy_policy.objects.first()
        return queryset


class Privacy_policy_detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Privacy_policy_serializer
    queryset = Privacy_policy.objects.all()
    lookup_field = 'pk'


class Terms_and_conditions_view(generics.RetrieveAPIView):
    serializer_class = Terms_serializer

    def get_object(self):
        queryset = Terms_and_conditions.objects.first()
        return queryset


class Terms_and_conditions_detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Terms_serializer
    queryset = Terms_and_conditions.objects.all()
    lookup_field = 'pk'



class Disclosure_view(generics.RetrieveAPIView):
    serializer_class = Disclosure_serializer

    def get_object(self):
        queryset = Disclosure_statement.objects.first()
        return queryset


class Disclosure_detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Disclosure_serializer
    queryset = Disclosure_statement.objects.all()
    lookup_field = 'pk'



class Important_view(generics.RetrieveAPIView):
    serializer_class = Important_information_serializer

    def get_object(self):
        queryset = Important_information.objects.first()
        return queryset


class Important_detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Important_information_serializer
    queryset = Important_information.objects.all()
    lookup_field = 'pk'


class Footer_View(generics.RetrieveAPIView):
    serializer_class = Footer_Serializer

    def get_object(self):
        queryset = Footer.objects.first()
        return queryset
    

class Footer_detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Footer_Serializer
    queryset = Footer.objects.all()
    lookup_field = 'pk'


class Footer_email_View(generics.ListCreateAPIView):
    serializer_class = Footer_email_serializer
    queryset = Footer_emails.objects.all()


class Footer_email_detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Footer_email_serializer
    queryset = Footer_emails.objects.all()
    lookup_field = 'pk'


class Footer_links_View(generics.ListCreateAPIView):
    serializer_class = Footer_links_serializer
    queryset = Footer_links.objects.all()


class Footer_links_detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Footer_links_serializer
    queryset = Footer_links.objects.all()
    lookup_field = 'pk'



class Header_View(generics.RetrieveAPIView):
    serializer_class = Header_serializer

    def get_object(self):
        queryset = Header.objects.first()
        return queryset
    

class Header_detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Header_serializer
    queryset = Header.objects.all()
    lookup_field = 'pk'


class Header_menu_View(generics.ListCreateAPIView):
    serializer_class = Menu_serializer
    queryset = Menu.objects.all()


class Header_Menu_detail_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Menu_serializer
    queryset = Menu.objects.all()
    lookup_field = 'pk'