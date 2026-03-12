from django.urls import path
from .views import *

urlpatterns = [
    path('homepage/',homepage),
    
    # about page
    
    path('aboutpage/',aboutpage),
    
    # blogs
    
    path('blogs_section/',Blog_section_view.as_view(),name='blogs_section'),
    path('blogs/<slug:slug>/',Blog_detail_view.as_view(),name='blog'),
    
    # Menu
    path('menus/',Menu_view.as_view(),name='menu'),
    path('header/',Header_view.as_view(),name='header'),
    
    # service_category
    
    path('service_category/<slug:slug>/',Service_category_detail_view.as_view(),name='category_detail'),
    path('services/<slug:slug>/',Service_detail_view.as_view(),name='service_detail'),
    
    # contact page
    
    path('contact_page/',contact_page),
    path('footer/',footer,name='footer'),
    path('privacy-policy/',Privacy_policy_view.as_view(),name='privacy_policy'),
    path('disclosure/',Disclosure_view.as_view(),name='disclosure'),

    # career

    path('career/',Career_view.as_view(),name='career'),
    path('job_application/',Job_Application_view.as_view(),name='job_application'),

    # enquiry

    path('enquiry/',Enquiry_form_view.as_view(),name='enquiry'),

    # other
    path('terms-and-conditions/',Terms_view.as_view(),name='terms'),
    path('important-information/',Important_view.as_view(),name='important'),

    # subscribe
    path('subscribe/',Subsribe_view.as_view(),name='subscribe'),

    # general faqs
    path('general_faqs/',General_faq_view.as_view(),name='general_faqs')


]
