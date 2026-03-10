from django.contrib import admin
from .models import *
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


# Register your models here.

class Hero_content_admin(admin.ModelAdmin):
    
    list_display = ("badge_text","main_heading","short_description","badge_icon")
    
    def has_add_permission(self, request):
        return not Hero_content.objects.exists()
    
    def has_delete_permission(self, request, obj = None):
        return False
    
admin.site.register(Hero_content,Hero_content_admin)


class Hero_features_admin(admin.ModelAdmin):
    list_display = ("feature",)
    
    def has_add_permission(self, request):
        return Hero_content.objects.count() < 8
    
admin.site.register(Hero_features,Hero_features_admin)


class Hero_CTA_button_admin(admin.ModelAdmin):
    list_display = ("button_text","link")
    
    def has_add_permission(self, request):
        return not Hero_CTA_button.objects.exists()
    
    def has_delete_permission(self, request, obj = None):
        return False
    
admin.site.register(Hero_CTA_button,Hero_CTA_button_admin)
    
class Hero_video_admin(admin.ModelAdmin):
    list_display = ("video_link","card_icon","card_title","card_description")
    
    def has_add_permission(self, request):
        return not Hero_video_section.objects.exists()
    
    def has_delete_permission(self, request, obj = None):
        return False
    
admin.site.register(Hero_video_section,Hero_video_admin)
    
class Partner_logos_admin(admin.ModelAdmin):
    list_display = ("name","logo")
admin.site.register(Partner_logos,Partner_logos_admin)




class Service_section_admin(admin.ModelAdmin):
    list_display = ('minor_heading','main_heading','paragraph',)
    
    
    def has_add_permission(self, request):
        return not Service_section.objects.exists()
    
    def has_delete_permission(self, request, obj = None):
        return False
    
admin.site.register(Service_section,Service_section_admin)



class Whychoose_section_admin(admin.ModelAdmin):
    list_display = ('minor_heading','main_heading','paragraph','button_icon','button_text','button_link')
    
    def has_add_permission(self, request):
        return not Whychoose_section.objects.exists()
    
    def has_delete_permission(self, request, obj = None):
        return False
    
admin.site.register(Whychoose_section,Whychoose_section_admin)
admin.site.register(Whychoose_Counter)
admin.site.register(WhyChoose_Points)
admin.site.register(Whychoose_us_cards)
admin.site.register(Achievements)
admin.site.register(Insights_video)


class Insights_section_admin(admin.ModelAdmin):
    list_display = ('minor_heading','main_heading','paragraph')
    
    def has_add_permission(self, request):
        return not Insights_section.objects.exists()
    
    def has_delete_permission(self, request, obj = None):
        return False
    
admin.site.register(Insights_section,Insights_section_admin)
admin.site.register(Testimonials)
admin.site.register(Accredited_members)





class Testimonials_section_admin(admin.ModelAdmin):
    list_display = ('minor_heading','main_heading')
    
    def has_add_permission(self, request):
        return not Testimonials_section.objects.exists()
    
    def has_delete_permission(self, request, obj = None):
        return False
    
admin.site.register(Testimonials_section,Testimonials_section_admin)


class HomeCalculator_admin(admin.ModelAdmin):
    list_display = ('minor_heading','main_heading','paragraph','button_text','button_link')
    
    def has_add_permission(self, request):
        return not Home_calculator_section.objects.exists()
    
    def has_delete_permission(self, request, obj = None):
        return False
    
admin.site.register(Home_calculator_section,HomeCalculator_admin)

class Contact_admin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return not Contact.objects.exists()
    
    def has_delete_permission(self, request, obj = None):
        return False

admin.site.register(Contact,Contact_admin)

class Social_admin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return not Social_media.objects.exists()
    
    def has_delete_permission(self, request, obj = None):
        return False

admin.site.register(Social_media,Social_admin)


class Office_admin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return not Office_timings.objects.exists()
    
    def has_delete_permission(self, request, obj = None):
        return False

admin.site.register(Office_timings,Office_admin)


class Contact_section_admin(admin.ModelAdmin):
    list_display = ('title','description','button_text','button_link')
    
    
    def has_add_permission(self, request):
        return not Contact_card_section.objects.exists()
    
    def has_delete_permission(self, request, obj = None):
        return False
    
admin.site.register(Contact_card_section,Contact_section_admin)


class AboutForm(forms.ModelForm):
    paragraph = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = About_first_section
        fields = '__all__'


class About_admin(admin.ModelAdmin):
    list_display = ('minor_heading','main_heading','paragraph','button_text','button_link','button_icon')
    form = AboutForm
    
    def has_add_permission(self, request):
        return not About_first_section.objects.exists()
    
    def has_delete_permission(self, request, obj = None):
        return False
    
admin.site.register(About_first_section,About_admin)




class Mission_vission_section_admin(admin.ModelAdmin):
    list_display = ('minor_heading','main_heading','paragraph')
    
    
    def has_add_permission(self, request):
        return not Mission_vission_section.objects.exists()
    
    def has_delete_permission(self, request, obj = None):
        return False
    
admin.site.register(Mission_vission_section,Mission_vission_section_admin)



class Core_values_Section_admin(admin.ModelAdmin):
    list_display = ('minor_heading','main_heading','paragraph')
    
    def has_add_permission(self, request):
        return not Our_core_values_section.objects.exists()
    
    def has_delete_permission(self, request, obj = None):
        return False
    
admin.site.register(Our_core_values_section,Core_values_Section_admin)

class teamMemberForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(),required=False)

    class Meta:
        model = Team_members
        fields = '__all__'

class TeamAdmin(admin.ModelAdmin):
    form = teamMemberForm

class careerForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(),required=False)
    benefits = forms.CharField(widget=CKEditorWidget(),required=False)

    class Meta:
        model = CareerPage
        fields = '__all__'
    
    
class Team_section_admin(admin.ModelAdmin):
    list_display = ('minor_heading','main_heading','paragraph')
    
    def has_add_permission(self, request):
        return not Team_section.objects.exists()
    
    def has_delete_permission(self, request, obj = None):
        return False
    

class CareerAdmin(admin.ModelAdmin):
    form = careerForm

    def has_add_permission(self, request):
        return not CareerPage.objects.exists()
    
    def has_delete_permission(self, request, obj = None):
        return False
    
    
admin.site.register(Team_section,Team_section_admin)
admin.site.register(Core_value_items)
admin.site.register(Team_members,TeamAdmin)
admin.site.register(Mission_vission_items)
admin.site.register(JobApplication)
admin.site.register(CareerPage,CareerAdmin)
admin.site.register(EnquiryForm)





class Menu_admin(admin.ModelAdmin):
    list_display = ('label','link','parent')
    
admin.site.register(Menu,Menu_admin)

class Header_admin(admin.ModelAdmin):
    list_display = ('logo','button_text','button_link')
admin.site.register(Header,Header_admin)

class ServiceCategoryForm(forms.ModelForm):
    brief_description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Service_category
        fields = '__all__'

class Service_category_Admin(admin.ModelAdmin):
    form = ServiceCategoryForm
    fieldsets = (
        ("Basic Info", {
            'fields': ('title', 'slug', 'cover_image', 'short_description')
        }),
        ("Page Settings", {
            'classes': ('collapse',),  # collapsible section
            'fields': ('banner_image', 'minor_heading', 'main_heading', 'brief_description')
        }),

)

admin.site.register(Service_category,Service_category_Admin)

class ServiceForm(forms.ModelForm):
    brief_description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Services
        fields = '__all__'


class Service_admin(admin.ModelAdmin):
    form = ServiceForm
    fieldsets = (
        ("Basic Info", {
            'fields': ('title', 'slug', 'cover_image', 'short_description', 'category')
        }),
        ("Page Settings", {
            'classes': ('collapse',),  # collapsible section
            'fields': ('banner_image', 'minor_heading', 'main_heading', 'brief_description')
        }),

)
    
admin.site.register(Services,Service_admin)
admin.site.register(Category_faq)
admin.site.register(Service_faq)


admin.site.register(Blog_category)

class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget()) 

    class Meta:
        model = Blog
        fields = '__all__'
        
class BlogAdmin(admin.ModelAdmin):
    form = BlogForm
    
    list_display = ('title','slug','author','published_at','status')
    
admin.site.register(Blog,BlogAdmin)

class Footer_Form(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        model = Footer
        fields = "__all__"

class Footer_Admin(admin.ModelAdmin):
    form = Footer_Form

admin.site.register(Footer,Footer_Admin)
admin.site.register(Footer_emails)
admin.site.register(Footer_links)

class Privacy_form(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Privacy_policy
        fields = "__all__"


class Privacy_policy_admin(admin.ModelAdmin):
    form = Privacy_form

    def has_add_permission(self, request):
        return not Privacy_policy.objects.exists()
    
    def has_delete_permission(self, request, obj = None):
        return False

admin.site.register(Privacy_policy,Privacy_policy_admin)


class Disclosure_form(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Disclosure_statement
        fields = "__all__"


class Disclosure_admin(admin.ModelAdmin):
    form = Disclosure_form

    def has_add_permission(self, request):
        return not Disclosure_statement.objects.exists()
    
    def has_delete_permission(self, request, obj = None):
        return False

admin.site.register(Disclosure_statement,Disclosure_admin)
