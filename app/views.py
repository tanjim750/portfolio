from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from .models import *

class SideBarView(View):
    def __init__(self):
        self.obj = SideBar.objects.first()

    def get(self,request):
        name = self.obj.name
        copyright = self.obj.copyright_text
        profile = self.obj.profile
        menus = self.obj.menus.all()
        social_links = self.obj.social_links.all()

        menus = list(menus.values())
        social = []
        for s in social_links:
            dic = {}
            dic.update({"name":s.platform, "link":s.link,"logo":s.logo.url})
            social.append(dic)

        context = {
            "name":name,"copyright":copyright,
            "profile":profile.url,"menus":menus,"social":social
            }
        return JsonResponse(context, safe=True)


class HomeView(View):
    def __init__(self):
        self.obj = Home.objects.first()
    
    def get(self,requests):
        title = self.obj.title
        subtitle = self.obj.subtitle
        image = self.obj.image.url
        btn1_text = self.obj.btn1_text
        btn1_link = self.obj.btn1_link
        btn2_text = self.obj.btn2_text
        btn2_link = self.obj.btn2_link
        contact = self.obj.contact_info.all()

        contact = list(contact.values())
        buttons = [
            {"text": btn1_text, "url": btn1_link},
            {"text": btn2_text, "url": btn2_link}
        ]

        context = {
            "title": title,"subtitle": subtitle,
            "image": image,"buttons":buttons,
            "contact": contact,
        }
        return JsonResponse(context, safe=True)
    

class AboutView(View):
    def __init__(self):
        self.obj = About.objects.first()
    
    def get(self,requests):
        title = self.obj.title
        description = self.obj.description
        btn_text = self.obj.btn_text
        btn_link = self.obj.btn_link
        skills = self.obj.skill
        contact = self.obj.contact_info.all()

        contact = list(contact.values())
        skills = list(skills.values())

        context = {
            "title": title,"description": description,"btn_text": btn_text,
            "btn_link": btn_link, "skills": skills,
            "contact": contact,
        }
        return JsonResponse(context, safe=True)