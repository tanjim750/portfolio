from django.db import models

# sidebar section starts
class SocialLinks(models.Model):
    platform = models.CharField(max_length=1000)
    logo = models.FileField(upload_to="logos")
    link = models.TextField()


class Menus(models.Model):
    name = models.CharField(max_length=1000)
    link = models.TextField()


class SideBar(models.Model):
    name = models.CharField(max_length=1000)
    copyright_text = models.CharField(max_length=50000)
    profile = models.FileField(upload_to="profile")
    social_links = models.ManyToManyField(SocialLinks)
    menus = models.ManyToManyField(Menus)


# Home section starts
class HomeContactInfo(models.Model):
    media = models.CharField(max_length=1000)
    contact = models.CharField(max_length=10000)


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
    title = models.TextField(default=default_title)
    subtitle = models.TextField(default=default_subtitle)
    image = models.ImageField(upload_to="images")
    btn1_text = models.CharField(max_length=500, default= "Got a Project")
    btn1_link = models.TextField(default="project.html")
    btn2_text = models.CharField(max_length=1000, default="Let's talk")
    btn2_link = models.TextField(default="contact.html")
    contact_info = models.ManyToManyField(HomeContactInfo)
    
# about section starts
class Skills(models.Model):
    field = models.CharField(max_length=10000)
    subtitle = models.CharField(max_length=10000, default="")
    text = models.TextField()
    skill = models.TextField()
    date = models.CharField(max_length=1000, default="2016-2023")


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
    title = models.TextField(default=default_title)
    description = models.TextField(default=default_text)
    btn_text = models.CharField(max_length=500, default= "Got a Project")
    btn_link = models.TextField(default="project.html")
    contact_info = models.ManyToManyField(HomeContactInfo)
    skill = models.ManyToManyField(Skills)

