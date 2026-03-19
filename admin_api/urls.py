from django.urls import path
from .views import *

urlpatterns = [
    path('hero_content/',Hero_content_view.as_view(),name="admin_hero_content"),
    path('hero_content_update/<int:pk>/',Hero_content_update_view.as_view(),name="admin_hero_content_update"),

    path('hero_video/',Hero_video_view.as_view(),name="admin_hero_video"),
    path('hero_video_update/<int:pk>/',Hero_video_update_view.as_view(),name="admin_hero_video_update"),

    path('hero_features/',Hero_features_view.as_view(),name="admin_hero_features"),
    path('hero_feature_update/<int:pk>/',Hero_features_update_view.as_view(),name="admin_hero_feature_update"),

    path('partners/',Partner_view.as_view(),name='partners'),
    path('partners/<int:pk>/',Partner_detail_view.as_view(),name='partners_detail'),

    path('service-section/',Service_section_view.as_view(),name='service-section'),
    path('service-section/<int:pk>/',Service_section_Detail_view.as_view(),name='service_detail'),

    path('service-categories/',Service_category_view.as_view(),name='service-category'),
    path('service-categories/<int:pk>/',Service_category_detail_view.as_view(),name='service_category_detail'),

    path('whychoose/',Whychoose_section_view.as_view(),name='whychoose'),
    path('whychoose/<int:pk>/',Whychoose_section_Detail_view.as_view(),name='whychoose'),

    path('whychoose-cards/',Whychoose_cards_view.as_view(),name='whychoose-cards'),
    path('whychoose-cards/<int:pk>/',Whychoose_cards_detail_view.as_view(),name='whychoose-cards_detail'),

    path('whychoose-points/',Whychoose_points_view.as_view(),name='whychoose-points'),
    path('whychoose-points/<int:pk>/',Whychoose_Points_detail_view.as_view(),name='whychoose-points_detail'),

    path('whychoose-counters/',Whychoose_counter_view.as_view(),name='whychoose-counter'),
    path('whychoose-counters/<int:pk>/',Whychoose_counter_detail_view.as_view(),name='whychoose-counter_detail'),

    path('achievements/',Achievments_view.as_view(),name='achievments'),
    path('achievements/<int:pk>/',Achievments_detail_view.as_view(),name='achievments'),

    path('insights-section/',Insights_section_view.as_view(),name='insights'),
    path('insights-section/<int:pk>/',Insights_section_Detail_view.as_view(),name='insights'),

    path('insights-videos/',insight_video_view.as_view(),name='insights-videos'),
    path('insights-videos/<int:pk>/',insight_video_detail_view.as_view(),name='insights-videos'),

    path('testimonials-section/',Testimonial_section_view.as_view(),name='testimonials_section'),
    path('testimonials-section/<int:pk>/',Testimonial_section_Detail_view.as_view(),name='testimonials_section'),

    path('testimonials/',Testimonial_view.as_view(),name='testimonials'),
    path('testimonials/<int:pk>/',Testimonials_detail_view.as_view(),name='testimonials'),

    path('accredited-members/',Accredited_view.as_view(),name='accredited'),
    path('accredited-members/<int:pk>/',Accredited_detail_view.as_view(),name='accredited'),

    path('about-first-section/',About_section_view.as_view(),name='about-section'),
    path('about-first-section/<int:pk>/',About_section_Detail_view.as_view(),name='about-section'),

    path('mission_vission_section/',Mission_vission_section_view.as_view(),name='mission-vission-section'),
    path('mission_vission_section/<int:pk>/',Mission_vission_section_Detail_view.as_view(),name='mission-vission-section'),

    path('mission_vission_items/',Mission_vission_view.as_view(),name='mission-vission-items'),
    path('mission_vission_items/<int:pk>/',Mission_vission_detail_view.as_view(),name='mission-vission-items'),

    path('core_values_section/',Core_values_section_view.as_view(),name='core-values-section'),
    path('core_values_section/<int:pk>/',Core_values_section_Detail_view.as_view(),name='core-values-section'),

    path('core_values_items/',Core_values_view.as_view(),name='core-values-items'),
    path('core_values_items/<int:pk>/',Core_values_detail_view.as_view(),name='core-values-items'),

    path('category-faq/',Category_faq_view.as_view(),name='cat-faq'),
    path('category-faq/<int:pk>/',Category_faq_detail_view.as_view(),name='cat-faq'),

    path('team-section/',Team_section_view.as_view(),name='team-section'),
    path('team-section/<int:pk>/',Team_section_Detail_view.as_view(),name='team-section'),

    path('team-members/',Team_members_view.as_view(),name='team-members'),
    path('team-members/<int:pk>/',Team_member_detail_view.as_view(),name='team-members'),

    path('contact-card-section/',Contact_card_section_view.as_view(),name='contact-card'),
    path('contact-card-section/<int:pk>/',contact_card_section_Detail_view.as_view(),name='contact-card'),

    path('contact/',Contact_view.as_view(),name='contact'),
    path('contact/<int:pk>/',contact_Detail_view.as_view(),name='contact'),

    path('social-media/',Social_media_view.as_view(),name='social-media'),
    path('social-media/<int:pk>/',Social_media_Detail_view.as_view(),name='social-media'),

    path('office-timings/',Office_time_view.as_view(),name='office-timings'),
    path('office-timings/<int:pk>/',Office_time_Detail_view.as_view(),name='office-timings'),

    path('services/',Services_view.as_view(),name='services'),
    path('services/<int:pk>/',Services_detail_view.as_view(),name='services'),

    path('service-faq/',Service_faq_view.as_view(),name='service-faq'),
    path('service-faq/<int:pk>/',Service_faq_detail_view.as_view(),name='service-faq'),

    path('blogs/',Blogs_view.as_view(),name='blogs'),
    path('blogs/<int:pk>/',Blogs_detail_view.as_view(),name='blogs'),

    path('users/',User_View.as_view(),name='user'),
    path('upload-image/', upload_image),



]
