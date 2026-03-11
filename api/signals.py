from django.db.models.signals import post_save,post_delete
from django.db import transaction
from django.dispatch import receiver
from .utils import notify_nextjs
from .models import (
    Header, Menu,
    Hero_content,
    Hero_CTA_button,
    Hero_features,
    Hero_video_section,
    Partner_logos,
    Service_section,
    Service_category,
    Testimonials_section,
    Testimonials,
    Whychoose_section,
    Whychoose_Counter,
    WhyChoose_Points,
    Whychoose_us_cards,
    Achievements,
    Accredited_members,
    Insights_section,
    Insights_video,
    Home_calculator_section,
    Contact_card_section,
    Office_timings,
    About_first_section,
    Mission_vission_items,
    Mission_vission_section,
    Our_core_values_section,
    Core_value_items,
    Team_members,
    Team_section,
    Blog,
    Services,
    Service_faq,
    Category_faq,
    Footer,
    Footer_emails,
    Footer_links,
    Privacy_policy,
    Disclosure_statement,
    Contact,
    Social_media,
    CareerPage,
    Terms_and_conditions,
    Important_information
    
)

def handle_footer(sender,instance,signal,**kwargs):
    if signal == post_delete:
        transaction.on_commit(lambda: notify_nextjs('footer'))
    else:
        notify_nextjs('footer')

def handle_privacy_policy(sender,instance,signal,**kwargs):
    if signal == post_delete:
        transaction.on_commit(lambda: notify_nextjs('privacyPolicy'))
    else:
        notify_nextjs('privacyPolicy')

@receiver([post_save,post_delete],sender=Privacy_policy)
def handle_privacy(sender,instance,signal,**kwargs):
    handle_privacy_policy(sender,instance,signal,**kwargs)


def handle_disclosure_statement(sender,instance,signal,**kwargs):
    if signal == post_delete:
        transaction.on_commit(lambda: notify_nextjs('disclosure'))
    else:
        notify_nextjs('disclosure')

@receiver([post_save,post_delete],sender=Disclosure_statement)
def handle_disclosure(sender,instance,signal,**kwargs):
    handle_disclosure_statement(sender,instance,signal,**kwargs)

        
@receiver([post_save,post_delete],sender=Footer)
def handle_footer_section(sender,instance,signal,**kwargs):
    handle_footer(sender,instance,signal,**kwargs)
    
@receiver([post_save,post_delete],sender=Footer_emails)
def handle_footer_section(sender,instance,signal,**kwargs):
    handle_footer(sender,instance,signal,**kwargs)
    
@receiver([post_save,post_delete],sender=Footer_links)
def handle_footer_section(sender,instance,signal,**kwargs):
    handle_footer(sender,instance,signal,**kwargs)


def handle_service(sender,instance,signal,**kwargs):
    if signal == post_delete:
        transaction.on_commit(lambda: notify_nextjs('services'))
    else:
        notify_nextjs('services')
        

@receiver([post_save,post_delete],sender=Service_category)
def handle_service_category(sender,instance,signal,**kwargs):
    handle_service(sender,instance,signal,**kwargs)  
    
    
@receiver([post_save,post_delete],sender=Category_faq)
def handle_service_category_faq(sender,instance,signal,**kwargs):
    handle_service(sender,instance,signal,**kwargs)  
    

@receiver([post_save,post_delete],sender=Services)
def handle_service_category_faq(sender,instance,signal,**kwargs):
    handle_service(sender,instance,signal,**kwargs)  
    
    
@receiver([post_save,post_delete],sender=Service_faq)
def handle_service_category_faq(sender,instance,signal,**kwargs):
    handle_service(sender,instance,signal,**kwargs)        
        

def handle_blogs(sender, instance, signal, **kwargs):
    if signal == post_delete:
        transaction.on_commit(lambda: notify_nextjs('blogs'))
    else:
        notify_nextjs('blogs')
        

@receiver([post_save,post_delete],sender=Blog)
def handle_blog_page(sender,instance,signal,**kwargs):
    handle_blogs(sender,instance,signal,**kwargs)


@receiver([post_save,post_delete],sender=Header)
def handle_header(sender,instance,**kwargs):
    notify_nextjs('header')
    
@receiver([post_save,post_delete],sender=Menu)
def handle_menu(sender,instance,**kwargs):
    notify_nextjs('menu')
    
    
def handle_homepage(sender, instance, signal, **kwargs):
    if signal == post_delete:
        transaction.on_commit(lambda: notify_nextjs('homepage'))
    else:
        notify_nextjs('homepage')

@receiver([post_save, post_delete], sender=Hero_content)
def handle_hero_content(sender, instance, signal, **kwargs):
    handle_homepage(sender, instance, signal, **kwargs)

@receiver([post_save, post_delete], sender=Hero_CTA_button)
def handle_hero_cta(sender, instance, signal, **kwargs):
    handle_homepage(sender, instance, signal, **kwargs)

@receiver([post_save, post_delete], sender=Hero_features)
def handle_hero_features(sender, instance, signal, **kwargs):
    handle_homepage(sender, instance, signal, **kwargs)

@receiver([post_save, post_delete], sender=Hero_video_section)
def handle_hero_video(sender, instance, signal, **kwargs):
    handle_homepage(sender, instance, signal, **kwargs)

@receiver([post_save, post_delete], sender=Partner_logos)
def handle_partners(sender, instance, signal, **kwargs):
    handle_homepage(sender, instance, signal, **kwargs)

@receiver([post_save, post_delete], sender=Service_section)
def handle_service_section(sender, instance, signal, **kwargs):
    handle_homepage(sender, instance, signal, **kwargs)

@receiver([post_save, post_delete], sender=Service_category)
def handle_service_category(sender, instance, signal, **kwargs):
    handle_homepage(sender, instance, signal, **kwargs)

@receiver([post_save, post_delete], sender=Testimonials_section)
def handle_testimonials_section(sender, instance, signal, **kwargs):
    handle_homepage(sender, instance, signal, **kwargs)

@receiver([post_save, post_delete], sender=Testimonials)
def handle_testimonials(sender, instance, signal, **kwargs):
    handle_homepage(sender, instance, signal, **kwargs)

@receiver([post_save, post_delete], sender=Whychoose_section)
def handle_whychoose_section(sender, instance, signal, **kwargs):
    handle_homepage(sender, instance, signal, **kwargs)

@receiver([post_save, post_delete], sender=Whychoose_Counter)
def handle_whychoose_counter(sender, instance, signal, **kwargs):
    handle_homepage(sender, instance, signal, **kwargs)

@receiver([post_save, post_delete], sender=WhyChoose_Points)
def handle_whychoose_points(sender, instance, signal, **kwargs):
    handle_homepage(sender, instance, signal, **kwargs)

@receiver([post_save, post_delete], sender=Whychoose_us_cards)
def handle_whychoose_cards(sender, instance, signal, **kwargs):
    handle_homepage(sender, instance, signal, **kwargs)

@receiver([post_save, post_delete], sender=Achievements)
def handle_achievements(sender, instance, signal, **kwargs):
    handle_homepage(sender, instance, signal, **kwargs)

@receiver([post_save, post_delete], sender=Accredited_members)
def handle_accredited(sender, instance, signal, **kwargs):
    handle_homepage(sender, instance, signal, **kwargs)

@receiver([post_save, post_delete], sender=Insights_section)
def handle_insights_section(sender, instance, signal, **kwargs):
    handle_homepage(sender, instance, signal, **kwargs)

@receiver([post_save, post_delete], sender=Insights_video)
def handle_insights_video(sender, instance, signal, **kwargs):
    handle_homepage(sender, instance, signal, **kwargs)

@receiver([post_save, post_delete], sender=Home_calculator_section)
def handle_calculator(sender, instance, signal, **kwargs):
    handle_homepage(sender, instance, signal, **kwargs)

@receiver([post_save, post_delete], sender=Contact_card_section)
def handle_contact(sender, instance, signal, **kwargs):
    handle_homepage(sender, instance, signal, **kwargs)
    handle_footer(sender, instance, signal, **kwargs)

@receiver([post_save, post_delete], sender=Social_media)
def handle_contact(sender, instance, signal, **kwargs):
    handle_homepage(sender, instance, signal, **kwargs)
    handle_footer(sender, instance, signal, **kwargs)

@receiver([post_save, post_delete], sender=Contact)
def handle_contact(sender, instance, signal, **kwargs):
    handle_homepage(sender, instance, signal, **kwargs)
    handle_footer(sender, instance, signal, **kwargs)

@receiver([post_save, post_delete], sender=Office_timings)
def handle_office_timings(sender, instance, signal, **kwargs):
    handle_homepage(sender, instance, signal, **kwargs)

    
    
def handle_aboutpage(signal, **kwargs):
    if signal == post_delete:
        transaction.on_commit(lambda: notify_nextjs('aboutpage'))
    else:
        notify_nextjs('aboutpage')

@receiver([post_save, post_delete], sender=About_first_section)
def handle_about_first(sender, instance, signal, **kwargs):
    handle_aboutpage(signal)

@receiver([post_save, post_delete], sender=Mission_vission_items)
def handle_mission_items(sender, instance, signal, **kwargs):
    handle_aboutpage(signal)

@receiver([post_save, post_delete], sender=Mission_vission_section)
def handle_mission_section(sender, instance, signal, **kwargs):
    handle_aboutpage(signal)

@receiver([post_save, post_delete], sender=Our_core_values_section)
def handle_core_values(sender, instance, signal, **kwargs):
    handle_aboutpage(signal)

@receiver([post_save, post_delete], sender=Core_value_items)
def handle_core_value_items(sender, instance, signal, **kwargs):
    handle_aboutpage(signal)

@receiver([post_save, post_delete], sender=Team_members)
def handle_team_members(sender, instance, signal, **kwargs):
    handle_aboutpage(signal)

@receiver([post_save, post_delete], sender=Team_section)
def handle_team_section(sender, instance, signal, **kwargs):
    handle_aboutpage(signal)


def handle_career(sender,instance,signal,**kwargs):
    if signal == post_delete:
        transaction.on_commit(lambda: notify_nextjs('career'))
    else:
        notify_nextjs('career')

@receiver([post_save,post_delete],sender=CareerPage)
def handle_careerPage(sender,instance,signal,**kwargs):
    handle_career(sender,instance,signal,**kwargs)



def handle_terms(sender,instance,signal,**kwargs):
    if signal == post_delete:
        transaction.on_commit(lambda: notify_nextjs('terms'))
    else:
        notify_nextjs('terms')

@receiver([post_save,post_delete],sender=Terms_and_conditions)
def handle_termsPage(sender,instance,signal,**kwargs):
    handle_terms(sender,instance,signal,**kwargs)


def handle_imp(sender,instance,signal,**kwargs):
    if signal == post_delete:
        transaction.on_commit(lambda: notify_nextjs('important'))
    else:
        notify_nextjs('important')

@receiver([post_save,post_delete],sender=Important_information)
def handle_impPage(sender,instance,signal,**kwargs):
    handle_imp(sender,instance,signal,**kwargs)