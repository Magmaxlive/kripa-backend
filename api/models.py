from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Hero_content(models.Model):
    badge_text=models.CharField(max_length=200)
    badge_icon = models.CharField(max_length=200,null=True,blank=True)
    main_heading=models.TextField()
    short_description=models.TextField()
    
    def __str__(self):
        return "Header content"
    
    
    
class Hero_features(models.Model):
    hero = models.ForeignKey(Hero_content,on_delete=models.CASCADE,related_name='features')
    feature = models.CharField(max_length=500)
    
    def __str__(self):
        return self.feature
    
    
class Hero_CTA_button(models.Model):
    hero = models.OneToOneField(Hero_content,on_delete=models.CASCADE,related_name='CTA')
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
    

class Services(models.Model):
    service = models.ForeignKey(Service_section,on_delete=models.CASCADE,related_name='services')
    cover_image = models.ImageField(upload_to='service_images/')
    title = models.CharField(max_length=400)
    description = models.TextField()
    button_link = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
    
    
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
    why_choose = models.ForeignKey(Whychoose_section,on_delete=models.CASCADE,related_name='points')
    content = models.CharField(max_length=500)
    
    def __str__(self):
        return self.content
    
    
class Whychoose_Counter(models.Model):
    why_choose = models.ForeignKey(Whychoose_section,on_delete=models.CASCADE,related_name='counts')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.description

class Whychoose_us_cards(models.Model):
    whychoose_us = models.ForeignKey(Whychoose_section,on_delete=models.CASCADE,related_name="cards")
    icon = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
class Achievements(models.Model):
    whychoose_us = models.ForeignKey(Whychoose_section,on_delete=models.CASCADE,related_name="achievements")
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
    insight = models.ForeignKey(Insights_section,on_delete=models.CASCADE,related_name='videos')
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
    testimonial_section = models.ForeignKey(Testimonials_section,on_delete=models.CASCADE,related_name='testimonials')
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
    testimonial = models.ForeignKey(Testimonials_section,on_delete=models.CASCADE,related_name='members')
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
    contact_card = models.OneToOneField(Contact_card_section,on_delete=models.SET_NULL,null=True,blank=True,related_name='contacts')
    phone = models.CharField(max_length=50)
    whatsapp = models.CharField(max_length=50)
    email = models.EmailField()
    location = models.TextField()
    location_link = models.URLField(null=True,blank=True)

    
    def __str__(self):
        return "Contact"
    

class Social_media(models.Model):
    contact_card = models.OneToOneField(Contact_card_section,on_delete=models.SET_NULL,null=True,blank=True,related_name='social_media')
    facebook = models.URLField(null=True,blank=True)
    instagram = models.URLField(null=True,blank=True)
    linkedin = models.URLField(null=True,blank=True)
    youtube = models.URLField(null=True,blank=True)
    twitter = models.URLField(null=True,blank=True)
    
    
    def __str__(self):
        return "Social Media"
    
    
class Office_timings(models.Model):
    contact_card = models.OneToOneField(Contact_card_section,on_delete=models.SET_NULL,null=True,blank=True,related_name='office_timings')
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
    mission_vission = models.ForeignKey(Mission_vission_section,on_delete=models.CASCADE,related_name='mission_vission_items')
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
    core_value = models.ForeignKey(Our_core_values_section,on_delete=models.CASCADE,related_name='core_values')
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
    team_section = models.ForeignKey(Team_section,on_delete=models.SET_NULL,null=True,blank=True,related_name='members')
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
    

class Blogs(models.Model):
    blog_section = models.ForeignKey(Blog_section,on_delete=models.SET_NULL,null=True,blank=True,related_name='blogs')
    cover_image = models.ImageField(upload_to='blog_images/')
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=500)
    content = models.TextField()
    
    def __str__(self):
        return self.title
    

# header menu

class Menu(models.Model):
    label = models.CharField(max_length=100)
    link = models.CharField(max_length=255,blank=True,null=True)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,related_name='submenu')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta :
        ordering = ['order']
        
    def __str__(self):
        return self.label
    