from typing import Iterable, Optional
from django.db import models
from django.core.exceptions import ValidationError

from ckeditor.fields import RichTextField

class Visitor(models.Model):
    visitor_id = models.CharField(max_length=10000)
    total_visit = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.visitor_id)

class VisitedUrl(models.Model):
    visitor = models.ForeignKey(Visitor,on_delete=models.CASCADE)
    url = models.URLField()
    total_visit = models.IntegerField(default=1)

# Upload Images 
class UploadImage(models.Model):
    name = models.CharField(max_length=1000)
    image = models.FileField(upload_to="images")

    def __str__(self):
        return self.name

class Button(models.Model):
    text = models.CharField(max_length=1000)
    url = models.TextField()

    def __str__(self):
        return self.text
    
#contact Section starts
class ContactInfo(models.Model):
    media = models.CharField(max_length=1000)
    contact = models.CharField(max_length=10000)

    def __str__(self):
        return self.media

class Contact(models.Model):
    default_loc = "https://www.google.com/maps?q=Bangladesh+Agricultural+Research+Institute/@23.9916906,90.4033221,15z/data=!3m1!4b1?entry=ttu=&output=embed"
    
    page_title = models.CharField(max_length=100000,default="Tanjim Abubokor")
    title = models.CharField(max_length=100000,default="- Let's Connect")
    heading = models.CharField(max_length=100000,default="Get in touch")
    text = models.TextField()
    contact = models.ManyToManyField(ContactInfo, related_name="Contact_info")
    btn_text = models.CharField(max_length=300)
    location = models.TextField(default=default_loc)

    def __str__(self):
        return self.text[:20]

# sidebar section starts
class SocialLinks(models.Model):
    platform = models.CharField(max_length=1000)
    logo = models.FileField(upload_to="logos")
    link = models.TextField()

    def __str__(self):
        return self.platform


class Menus(models.Model):
    name = models.CharField(max_length=1000)
    link = models.TextField()

    def __str__(self):
        return self.name


class SideBar(models.Model):
    name = models.CharField(max_length=1000)
    copyright_text = models.CharField(max_length=50000)
    profile = models.FileField(upload_to="profile")
    logo = models.FileField(upload_to="logo",null=True,blank=True)
    social_links = models.ManyToManyField(SocialLinks)
    menus = models.ManyToManyField(Menus)

    def __str__(self):
        return self.name


# Home section starts

class Home(models.Model):
    default_title = """
        <h3>Hi, I'm <span class="blueColor">Elisc!</span></h3>
        <h3>
        <span class="cd-headline rotate-1"> 
        <span class="blc">Creative</span>
        <span class="cd-words-wrapper">
        <b class="is-visible">Designer</b>
        <b>Coder</b>
        <b>Player</b>
        </span>
        </span>
        </h3>
        <h3>Based in Florida</h3>
    """
    default_subtitle = """
        <p>I'm a Florida based web designer &amp; front‑end developer with <span class="blueColor">10+ years</span> of experience</p>
    """
    page_title = models.CharField(max_length=100000,default="Tanjim Abubokor")
    title = models.TextField(default=default_title)
    subtitle = models.TextField(default=default_subtitle)
    image = models.ImageField(upload_to="images")
    contact_info = models.ManyToManyField(ContactInfo)
    buttons = models.ManyToManyField(Button, blank=True,null=True)

    def __str__(self):
        return str(self.id)
    
# about section starts
class Skills(models.Model):
    field = models.CharField(max_length=10000)
    subtitle = models.CharField(max_length=10000, default="")
    text = models.TextField()
    skill = models.TextField()
    date = models.CharField(max_length=1000, default="2016-2023")

    def __str__(self):
        return self.skill


class About(models.Model):
    default_title = """
        <span class="mini">- Nice to meet you!</span>
        <h3 class="name">Robert Elisc</h3>
        <span class="job">
        <span class="cd-headline rotate-1"> 
        <span class="blc">Web designer &amp;</span>
        <span class="cd-words-wrapper">
        <b class="is-visible">Developer</b>
        <b>Coder</b>
        <b>Player</b>
        </span>
        </span>
        </span>
    """
    default_text = """
        <p>Hello there! My name is <span class="yellowColor">Robert Elisc</span>. I am a web designer &amp; developer, and I'm very passionate and dedicated to my work.</p>
        <p>With 20 years experience as a professional a graphic designer, I have acquired the skills and knowledge necessary to make your project a success. I enjoy every step of the design process, from discussion and collaboration.</p>
    """
    page_title = models.CharField(max_length=100000,default="Tanjim Abubokor")
    title = models.TextField(default=default_title)
    description = models.TextField(default=default_text)
    banner = models.JSONField(default=[])
    contact_info = models.ManyToManyField(ContactInfo)
    skill = models.ManyToManyField(Skills)
    buttons = models.ManyToManyField(Button, blank=True,null=True)

    def __str__(self):
        return str(self.id)

# service section starts
class IntroVideo(models.Model):
    title = models.CharField(max_length=10000)
    thumbnail = models.ImageField(upload_to="thumbnail")
    play_btn = models.FileField(upload_to="images")
    video_link = models.URLField(blank=True, null=True)
    video = models.FileField(upload_to="video",blank=True, null=True)

    def __str__(self):
        return self.title

class Service(models.Model):
    page_title = models.CharField(max_length=100000,default="Tanjim Abubokor")
    title = models.CharField(max_length=10000)
    description = models.TextField()
    buttons = models.ManyToManyField(Button, blank=True,null=True)

    def __str__(self):
        return self.title

        
# Projects section starts
class Testimonial(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField()
    service = models.TextField()

    def __str__(self):
        return self.name

class Project(models.Model):
    page_title = models.CharField(max_length=100000,default="Tanjim Abubokor")
    title = models.CharField(max_length=10000)
    short_text = models.TextField()
    video = models.FileField(upload_to="projects", blank=True, null=True)
    video_url = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to="images", blank=True ,null=True)
    description = RichTextField()
    date = models.DateField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.title

# Blog section starts 
class Blog(models.Model):
    page_title = models.CharField(max_length=100000,default="Tanjim Abubokor")
    title = models.CharField(max_length=100000)
    image = models.TextField()
    description = RichTextField()
    date = models.DateField(editable=True)

    def __str__(self):
        return self.title
    

class AllInfoJson(models.Model):
    info = models.JSONField()