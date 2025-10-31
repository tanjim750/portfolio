from rest_framework import serializers

from .models import (
    SideBar, Menus, SocialLinks,
    Home, About, Skills,
    Service, IntroVideo,
    Project, Testimonial,
    Blog, Contact, ContactInfo
)

# --- Sidebar Serializers ---
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menus
        fields = ["id", "name", "link"]

class SocialLinkSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="platform")          # expose "platform" as "name"
    logo = serializers.SerializerMethodField()

    class Meta:
        model = SocialLinks
        fields = ["name", "link", "logo"]

    def get_logo(self, obj):
        return obj.logo.url if obj.logo else None

class SideBarSerializer(serializers.ModelSerializer):
    menus = MenuSerializer(many=True, read_only=True)
    social = SocialLinkSerializer(source="social_links", many=True, read_only=True)
    profile = serializers.SerializerMethodField()
    logo = serializers.SerializerMethodField()
    textLogo = serializers.SerializerMethodField()
    copyright = serializers.CharField(source="copyright_text", read_only=True)

    class Meta:
        model = SideBar
        # return friendly JSON keys while sourcing from actual model fields
        fields = ["name", "textLogo", "profile", "logo", "copyright", "menus", "social"]

    def get_profile(self, obj):
        return obj.profile.url if obj.profile else None

    def get_logo(self, obj):
        return obj.logo.url if obj.logo else None

    def get_textLogo(self, obj):
        parts = obj.name.split()
        return f"{parts[0][0]}.{parts[-1]}" if len(parts) > 1 else obj.name


# --- Home Serializer ---
class HomeSerializer(serializers.ModelSerializer):
    heroImage = serializers.SerializerMethodField()

    class Meta:
        model = Home
        fields = ["title", "subtitle", "heroImage", "btn1_text", "btn1_link", "btn2_text", "btn2_link"]

    def get_heroImage(self, obj):
        return obj.image.url if obj.image else None

# --- About + Skills ---
class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ["field", "subtitle", "text", "skill", "date"]

class AboutSerializer(serializers.ModelSerializer):
    skills = SkillsSerializer(many=True, read_only=True, source="skill")

    class Meta:
        model = About
        fields = ["title", "description", "btn_text", "btn_link", "skills"]

# --- Services ---
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["page_title", "title", "description", "btn", "btn_link"]

class IntroVideoSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()
    play_btn = serializers.SerializerMethodField()

    class Meta:
        model = IntroVideo
        fields = ["title", "video_link", "thumbnail", "play_btn"]

    def get_thumbnail(self, obj):
        return obj.thumbnail.url if obj.thumbnail else None

    def get_play_btn(self, obj):
        return obj.play_btn.url if obj.play_btn else None

# --- Project & Testimonials ---
class ProjectSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ["title", "description", "image", "date", "video_url"]

    def get_image(self, obj):
        return obj.image.url if obj.image else None

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ["name", "service", "description"]

# --- Blog ---
class BlogSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ["id", "page_title", "title", "image", "description", "date"]

    def get_image(self, obj):
        return obj.image if isinstance(obj.image, str) else (obj.image.url if obj.image else None)

# --- Contact ---
class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ["media", "contact"]

class ContactSerializer(serializers.ModelSerializer):
    contacts = ContactInfoSerializer(source="contact", many=True, read_only=True)
    title = ContactInfoSerializer(source="page_title", many=True, read_only=True)

    class Meta:
        model = Contact
        fields = ["page_title", "title", "heading", "text", "btn_text", "contacts", "location"]


class AllInfoSerializer(serializers.Serializer):
    page_title = serializers.CharField(default="Portfolio @Tanjim Abubokor")
    sidebar = SideBarSerializer()
    home = HomeSerializer()
    about = AboutSerializer()
    service = serializers.SerializerMethodField()
    project = serializers.SerializerMethodField()
    blog = serializers.SerializerMethodField()
    contact = ContactSerializer()
    testimonial = serializers.SerializerMethodField()

    def get_service(self, obj):
        return {
            "title": "My Services",
            "services": ServiceSerializer(Service.objects.all(), many=True).data,
            "intro_video": IntroVideoSerializer(IntroVideo.objects.first()).data if IntroVideo.objects.exists() else None,
        }

    def get_project(self, obj):
        return {
            "projects": ProjectSerializer(Project.objects.all(), many=True).data,
        }

    def get_blog(self, obj):
        return {
            "blogs": BlogSerializer(Blog.objects.all(), many=True).data,
        }

    def get_testimonial(self, obj):
        return {
            "testimonials": TestimonialSerializer(Testimonial.objects.all(), many=True).data,
        }
