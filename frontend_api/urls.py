from django.urls import path
from .views import *

urlpatterns = [
    path('hero_content/',Hero_content_view.as_view(),name="hero_content"),
    path('hero_video/',Hero_video_section_view.as_view(),name='hero_video'),
    path('partner_logos/',Partner_logos_view.as_view(),name='partner_logos'),
    path('service_section/',Service_section_view.as_view(),name='service_section'),
    path('whychoose_us_section/',Whychoose_us_section_view.as_view(),name='whychoose_us'),
    path('insights_section/',Insights_section_view.as_view(),name="insights_section"),
    path('testimonials_section/',Testimonials_section_view.as_view(),name="testimonial_Section"),
    path('home_calculator_section/',Home_calculator_section_view.as_view(),name="home_calculator"),
    path('contact_section/',Contact_section_view.as_view(),name="contact_section"),
    
    # about page
    
    path('about_first_section/',About_section_view.as_view(),name="about_first_section"),
    path('mission_vission_Section/',Mission_vission_section_view.as_view(),name='mission_vission'),
    path('core_values_section/',Core_values_section_view.as_view(),name="core_values"),
    path('team_section/',Team_section_view.as_view(),name="team_section"),
    
    # blogs
    
    path('blogs_section/',Blog_section_view.as_view(),name='blogs_section'),
    
    # Menu
    path('menus/',Menu_view.as_view(),name='menu')
]
