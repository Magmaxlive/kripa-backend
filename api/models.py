from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils.text import slugify
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .utils import notify_nextjs

# Create your models here.

class Hero_content(models.Model):
    badge_text=models.CharField(max_length=200)
    badge_icon = models.CharField(max_length=200,null=True,blank=True)
    main_heading=models.TextField()
    short_description=models.TextField()
    
    def __str__(self):
        return "hero content"
    
    
    
class Hero_features(models.Model):
    feature = models.CharField(max_length=500)
    
    def __str__(self):
        return self.feature
    
    
class Hero_CTA_button(models.Model):
    button_text = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    
    def __str__(self):
        return self.button_text


class Hero_video_section(models.Model):
    video_link = models.URLField()
    card_icon = models.CharField(max_length=200)
    card_title = models.CharField(max_length=200)
    card_description = models.TextField()
    
    def __str__(self):
        return "Hero video section"
    
    
class Partner_logos(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='partner_logos/')
    
    def __str__(self):
        return self.name
    
    
class Service_section(models.Model):
    minor_heading = models.CharField(max_length=400)
    main_heading = models.CharField(max_length=800)
    paragraph = models.TextField()
    
    def __str__(self):
        return 'Service Section'
    


    
    
    
class Whychoose_section(models.Model):
    minor_heading = models.CharField(max_length=300)
    main_heading = models.CharField(max_length=500)
    paragraph = models.TextField()
    button_icon = models.CharField(max_length=100)
    button_text = models.CharField(max_length=200)
    button_link = models.CharField(max_length=200)
    
    def __str__(self):
        return "why choose us"
    
    
class WhyChoose_Points(models.Model):
    content = models.CharField(max_length=500)
    
    def __str__(self):
        return self.content
    
    
class Whychoose_Counter(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.description

class Whychoose_us_cards(models.Model):
    icon = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
class Achievements(models.Model):
    alt = models.CharField(max_length=400)
    image = models.ImageField(upload_to='achievements/')
    
    def __str__(self):
        return self.alt
    
    
    
class Insights_section(models.Model):
    minor_heading = models.CharField(max_length=300)
    main_heading = models.CharField(max_length=500)
    paragraph = models.TextField()
    
    
    def __str__(self):
        return "Insights Section"
    
    
class Insights_video(models.Model):
    video_link = models.URLField()
    title = models.CharField(max_length=500)
    description = models.TextField()
    button_text = models.CharField(max_length=200)
    button_link = models.CharField(max_length=200)
    button_icon = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    

    
class Testimonials_section(models.Model):
    minor_heading = models.CharField(max_length=200)
    main_heading = models.CharField(max_length=500)
    
    def __str__(self):
        return "Testimonial Section"
    
    
class Testimonials(models.Model):
    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    
    author = models.CharField(max_length=500)
    testimonial = models.TextField()
    
    def __str__(self):
        return self.author
    
class Accredited_members(models.Model):
    name = models.CharField(max_length=200)  
    
    
class Home_calculator_section(models.Model):
    minor_heading = models.CharField(max_length=200)
    main_heading = models.CharField(max_length=300)
    paragraph = models.TextField()
    button_text = models.CharField(max_length=100)
    button_link = models.CharField(max_length=100)
    
    
    def __str__(self):
        return "Home Calculator"
    
    
    
class Contact_card_section(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    button_text = models.CharField(max_length=100)
    button_link = models.URLField()
    
    
    def __str__(self):
        return "Contact card"
    
    
    
class Contact(models.Model):
    phone = models.CharField(max_length=50)
    whatsapp = models.CharField(max_length=50)
    email = models.EmailField()
    location = models.TextField()
    location_link = models.TextField(null=True,blank=True)
    map_embed = models.TextField(null=True,blank=True)

    
    def __str__(self):
        return "Contact"
    

class Social_media(models.Model):
    facebook = models.URLField(null=True,blank=True)
    instagram = models.URLField(null=True,blank=True)
    linkedin = models.URLField(null=True,blank=True)
    youtube = models.URLField(null=True,blank=True)
    twitter = models.URLField(null=True,blank=True)
    
    
    def __str__(self):
        return "Social Media"
    
    
class Office_timings(models.Model):
    mon_fri = models.CharField(max_length=100)
    saturday = models.CharField(max_length=100)
    sunday = models.CharField(max_length=100)
    
    def __str__(self):
        return "Office timings"
    
    
# about page


class About_first_section(models.Model):
    image = models.ImageField(upload_to='about-image/')
    minor_heading = models.CharField(max_length=100)
    main_heading = models.CharField(max_length=400)
    paragraph = models.TextField(null=True,blank=True)
    button_text = models.CharField(max_length=100)
    button_link = models.CharField(max_length=200)
    button_icon = models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return "About Section"
    
    
class Mission_vission_section(models.Model):
    minor_heading = models.CharField(max_length=100)
    main_heading = models.CharField(max_length=400)
    paragraph = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return "Mission Vission Section"
    
    
class Mission_vission_items(models.Model):
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
    
class Our_core_values_section(models.Model):
    minor_heading = models.CharField(max_length=100)
    main_heading = models.CharField(max_length=400)
    paragraph = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return "core values section"
    
    
class Core_value_items(models.Model):
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
    
class Team_section(models.Model):
    minor_heading = models.CharField(max_length=100)
    main_heading = models.CharField(max_length=400)
    paragraph = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return "core values section"
    
    
class Team_members(models.Model):
    options = (
        ('core_member','Core Member'),
        ('mortage_adviser','Mortage Adviser'),
        ('other','Other'),
    )
    image = models.ImageField(upload_to='team_members/')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=200)
    category = models.CharField(choices=options,max_length=100)
    description = models.TextField(null=True,blank=True)
    
    
    def __str__(self):
        return self.name
    
    
# blog page

class Blog_section(models.Model):
    minor_heading = models.CharField(max_length=100)
    main_heading = models.CharField(max_length=400)
    paragraph = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return "blog section"
    


    

# header menu

class Header(models.Model):
    logo = models.FileField(upload_to='logos/')
    button_text = models.CharField(max_length=100)
    button_link = models.CharField(max_length=200)
    button_icon = models.CharField(max_length=100)
    header_version = models.CharField(max_length=50,default="1") 
    menu_version = models.CharField(max_length=50,default="1") 

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        
    
    def __str__(self):
        return "Website Header"

    class Meta:
        verbose_name = "Header"
        verbose_name_plural = "Header"

class Menu(models.Model):
    header = models.ForeignKey(Header,on_delete=models.SET_NULL,null=True,blank=True,related_name='menu')
    label = models.CharField(max_length=100)
    link = models.CharField(max_length=255,blank=True,null=True)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,related_name='submenu')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta :
        ordering = ['order']
        
    def __str__(self):
        return self.label
    
    def save(self, *args, **kwargs):
        if self.header is None:
            self.header = Header.objects.first()
        super().save(*args, **kwargs)
        
        
@receiver([post_save,post_delete],sender='api.Menu')
def bump_menu_version(sender,instance,**kwargs):
    header = instance.header
    header.menu_version = str(uuid.uuid4())
    header.save()    
    
    
    
class Service_category(models.Model):
    cover_image = models.ImageField(upload_to='service_images/')
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=800)
    # page settings
    banner_image = models.ImageField(upload_to='service_images/',null=True,blank=True)
    minor_heading = models.CharField(max_length=100)
    main_heading = models.CharField(max_length=400)
    brief_description = models.TextField()
    
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    
   
class Category_faq(models.Model):
    category = models.ForeignKey(Service_category,on_delete=models.CASCADE,related_name='faq')
    question = models.CharField(max_length=500)
    answer = models.TextField()
    
    def __str__(self):
        return self.question
    
    
    

class Services(models.Model):
    category = models.ForeignKey(Service_category,on_delete=models.SET_NULL,related_name='services',blank=True,null=True)
    cover_image = models.ImageField(upload_to='service_images/')
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=800)
    
    # page settings
    banner_image = models.ImageField(upload_to='service_images/',null=True,blank=True)
    minor_heading = models.CharField(max_length=100)
    main_heading = models.CharField(max_length=400)
    brief_description = models.TextField()
    
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
        
class Service_faq(models.Model):
    service = models.ForeignKey(Services,on_delete=models.CASCADE,related_name='faq')
    question = models.CharField(max_length=500)
    answer = models.TextField()
    
    def __str__(self):
        return self.question
    
    
class Blog_category(models.Model):
    title = models.CharField(max_length=800)
    
    def __str__(self):
        return self.title
    

class Blog(models.Model):
    STATUS_CHOICES=(
    ('draft','Draft'),
    ('published','Published')
    )
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True,blank=True,max_length=255)
    video_title = models.CharField(max_length=200,null=True,blank=True)
    video_link = models.URLField(null=True,blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Blog_category, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True,auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title
    
    
class Footer(models.Model):
    logo=models.FileField(upload_to='logos/')
    description=models.TextField()
    
    def __str__(self):
        return "Footer Section"
    
class Footer_emails(models.Model):
    email = models.EmailField()
    
    def __str__(self):
        return self.email
    
    
class Footer_links(models.Model):
    label = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    
    def __str__(self):
        return self.label

class Privacy_policy(models.Model):
    content = models.TextField()

class Disclosure_statement(models.Model):
    content = models.TextField()

class CareerPage(models.Model):
    image = models.ImageField(upload_to='careerimages/')
    description = models.TextField()
    benefits = models.TextField()
    image2 = models.ImageField(upload_to='careerimages/')

class JobApplication(models.Model):
    STATUS_OPTIONS = [
        ('pending','Pending'),
        ('reviewing','Reviewing'),
        ('accepted','Accepted'),
        ('rejected','Rejected'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(blank=True)
    linkedin_url = models.URLField(blank=True)
    position =  models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_OPTIONS, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"


class EnquiryForm(models.Model):
    STATUS_OPTIONS = [
        ('pending','Pending'),
        ('reviewing','Reviewing'),
        ('responded','Responded'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=50)
    message =  models.TextField(null=True,blank=True)
    status = models.CharField(max_length=20, choices=STATUS_OPTIONS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.service}"