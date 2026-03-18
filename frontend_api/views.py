from django.shortcuts import render
from rest_framework import generics
from api.models import *
from api.serializers import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings



@api_view(['GET'])
def homepage(request):
    context = {'request': request}
    
    hero = Hero_content.objects.first()
    hero_video = Hero_video_section.objects.first()
    partners = Partner_logos.objects.all()
    services = Service_section.objects.first()
    testimonials = Testimonials_section.objects.first()
    why_choose = Whychoose_section.objects.first()
    insights = Insights_section.objects.first()
    estimator = Home_calculator_section.objects.first()
    contact = Contact_card_section.objects.first()
    
    data = {
        "hero_section": Hero_content_serializer(hero).data if hero else None,
        "hero_video_section": Hero_video_section_serializer(hero_video).data if hero_video else None,
        "partners_section": Partner_logos_serializer(partners, many=True,context=context).data,
        "services_section": Service_section_serializer(services,context=context).data,
        'whyChooseUs_section': Whychoose_us_section_serializer(why_choose,context=context).data,
        'insight_section': Insights_section_serializer(insights).data,
        'estimator_section':Home_calculator_serializer(estimator).data,
        "testimonials": Testimonial_section_serializer(testimonials).data,
        'contact': Contact_card_serializer(contact).data
    }

    return Response(data)




@api_view(['GET'])
def aboutpage(request):
    context = {'request': request}
    
    firstSection = About_first_section.objects.first()
    mission_vission = Mission_vission_section.objects.first()
    core_Values = Our_core_values_section.objects.first()
    team = Team_section.objects.first()
    
    
    data = {
        "firstSectionData": About_first_Section_serializer(firstSection,context=context).data if firstSection else None,
        "mission_vission_Data": Mission_vission_section_serializer(mission_vission).data if mission_vission else None,
        "core_Values_Data": Core_values_section_serializer(core_Values).data,
        "teamData": Team_section_serializer(team,context=context).data,
    }

    return Response(data)

@api_view(['GET'])
def contact_page(request):
    context = {'request': request}
    
    contact = Contact_card_section.objects.first()
    services = Service_category.objects.all()
    data = {
        'contact' : Contact_card_serializer(contact,context=context).data,
        'service' : Home_page_service_category(services,many=True).data
    }
    return Response(data)
    


    
class BlogPagination(PageNumberPagination):
    page_size = 6
    
class Blog_section_view(generics.ListAPIView):
    serializer_class = Blogs_serializer
    pagination_class = BlogPagination
    
    def get_queryset(self):
        queryset = Blog.objects.filter(status='published')
        return queryset
    
class Menu_view(generics.ListAPIView):
    serializer_class = Menu_serializer
    
    def get_queryset(self):
        return Menu.objects.filter(parent__isnull=True)
    
    
class Header_view(generics.RetrieveAPIView):
    serializer_class = Header_serializer
    
    def get_object(self):
        return Header.objects.first()
    
class Service_category_detail_view(generics.RetrieveAPIView):
    queryset = Service_category.objects.all()
    serializer_class = Services_category_serializer
    lookup_field = 'slug'
    

class Service_detail_view(generics.RetrieveAPIView):
    queryset = Services.objects.all()
    serializer_class = Services_serializer
    lookup_field = 'slug'
    
    
class Blog_detail_view(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = Blogs_serializer
    lookup_field = 'slug'
    
    

    
@api_view(['GET'])
def footer(request):
    context = {'request': request}
    
    footer = Footer.objects.first()
    emails = Footer_emails.objects.all()
    links = Footer_links.objects.all()
    contact = Contact_card_section.objects.first()
    
    data = {
        'footer' : Footer_Serializer(footer,context=context).data,
        'emails' : Footer_email_serializer(emails,many=True).data,
        'links' : Footer_links_serializer(links,many=True).data,
        'contact' : Contact_card_serializer(contact).data
    }
    
    return Response(data)


class Privacy_policy_view(generics.RetrieveAPIView):
    serializer_class = Privacy_policy_serializer

    def get_object(self):
        return Privacy_policy.objects.first()



class Disclosure_view(generics.RetrieveAPIView):
    serializer_class = Disclosure_serializer

    def get_object(self):
        return Disclosure_statement.objects.first()
    

class Career_view(generics.RetrieveAPIView):
    serializer_class = Career_Serializer
    
    def get_object(self):
        return CareerPage.objects.first()
    
class Job_Application_view(generics.CreateAPIView):
    serializer_class = Job_application_Serializer
    queryset = JobApplication.objects.all()
    

class Enquiry_form_view(generics.CreateAPIView):
    serializer_class = Enquiry_Serializer
    queryset = EnquiryForm.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        self.send_enquiry_email(instance)

    def send_enquiry_email(self,instance):
        context = {
            'name' : instance.full_name,
            'email' : instance.email,
            'service' : instance.service,
            'phone' : instance.phone,
            'message' : instance.message
        }

        html_content = render_to_string('emails/enquiry.html',context)
        text_content = f"New enquiry from {instance.full_name} - {instance.email}"

        email = EmailMultiAlternatives(
            subject=f"New enquiry from {instance.full_name}",
            body=text_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.DEFAULT_FROM_EMAIL],
            reply_to=[instance.email],
        )

        email.attach_alternative(html_content,"text/html")
        email.send(fail_silently=False)


class Terms_view(generics.RetrieveAPIView):
    serializer_class = Terms_serializer

    def get_object(self):
        return Terms_and_conditions.objects.first()
    

class Important_view(generics.RetrieveAPIView):
    serializer_class = Important_information_serializer

    def get_object(self):
        return Important_information.objects.first()
    

class Subsribe_view(generics.CreateAPIView):
    serializer_class = Subsribers_serializer
    queryset = Subscriber.objects.all()


class General_faq_view(generics.ListAPIView):
    serializer_class = General_faq_serializer
    queryset = General_faqs.objects.all()

class Service_category_list(generics.ListAPIView):
    serializer_class = Services_category_serializer
    queryset = Service_category.objects.all()