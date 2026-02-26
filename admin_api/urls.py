from django.urls import path
from .views import *

urlpatterns = [
    path('hero_content/',Hero_content_view.as_view(),name="admin_hero_content"),
    path('hero_features/',Hero_features_view.as_view(),name="admin_hero_features"),
    path('hero_cta_button/',Hero_CTA_button_view.as_view(),name="admin_hero_cta_button")
]
