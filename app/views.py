from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from django.core.mail import EmailMultiAlternatives

from .models import *
from app.serializers import AllInfoSerializer

class AllInfoJsonView(View):
    def get(self, request):
        data = {
            "sidebar": SideBar.objects.first(),
            "home": Home.objects.first(),
            "about": About.objects.first(),
            "contact": Contact.objects.first(),
        }
        serializer = AllInfoSerializer(data)
        if serializer.is_valid():
            return JsonResponse(serializer.data, safe=True)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def visitor_view(request):
    if request.method == 'POST':
        visitor_id = request.POST.get('visitor_id', None)
        visited_url = request.POST.get('visited_url', None)

        if visitor_id and visited_url:
            visitor = Visitor.objects.filter(visitor_id=visitor_id)

            if visitor.exists():
                visitor = visitor.first()
                visitor.total_visit += 1
                visitor.save()
                
                get_visited_url = VisitedUrl.objects.filter(url=visited_url)
                if get_visited_url.exists():
                    get_visited_url = get_visited_url.first()
                    get_visited_url.total_visit += 1
                    get_visited_url.save()
                else:
                    VisitedUrl.objects.create(
                        visitor=visitor,
                        url = visited_url
                        )
                
                context = {
                    "success": True,
                    "action": "Already Exists",
                }
            else:
                obj = Visitor.objects.create(
                    visitor_id=visitor_id
                    )
                
                VisitedUrl.objects.create(
                    visitor=obj,
                    url = visited_url
                    )

                context = {
                    "success": True,
                    "action": "New Visitor Added",
                }
        else:
            context = {
                    "success": False,
                    "action": "Please provide a valid visitor id and the url",
            }
    else:
        context = {
            "success": False,
            "error": "Invalid request",
        }

    return JsonResponse(context,safe=True)
            


class SideBarView(View):
    def __init__(self):
        self.obj = SideBar.objects.first()

    def get(self,request):
        name = self.obj.name
        copyright = self.obj.copyright_text
        profile = self.obj.profile
        logo = self.obj.logo
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
            "profile":profile.url,"menus":menus,"social":social,
            "logo": logo.url if logo else None
            }
        return JsonResponse(context, safe=True)


class HomeView(View):
    def __init__(self):
        self.obj = Home.objects.first()
    
    def get(self,requests):
        page_title = self.obj.page_title
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
            "contact": contact,"page_title": page_title
        }
        return JsonResponse(context, safe=True)
    

class AboutView(View):
    def __init__(self):
        self.obj = About.objects.first()
    
    def get(self,requests):
        page_title = self.obj.page_title
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
            "contact": contact,"page_title": page_title
        }
        return JsonResponse(context, safe=True)
    
class ServiceView(View):
    def __init__(self):
        self.video = IntroVideo.objects.first()
        self.obj = Service.objects.all()
    
    def get(self, request):
        services = list(self.obj.values())
        domain_url = request.build_absolute_uri('/')[:-1]

        video_title = self.video.title
        thumbnail = self.video.thumbnail.url
        play_btn = self.video.play_btn.url
        video = self.video.video
        video_url = self.video.video_link

        context = {
            "services": services,
            "video_title": video_title, "thumbnail": thumbnail,
            "play_btn": play_btn,"video_url": video_url if video_url else domain_url+video.url
        
        }
        return JsonResponse(context,safe=True)

class ProjectView(View):
    def __init__(self):
        self.obj = Project.objects.all()
        self.tstm = Testimonial.objects.all()
    
    def get(self,request):
        domain_url = request.build_absolute_uri('/')[:-1]
        projects = []

        for project in self.obj:
            dict = {}
            dict['id'] = project.id
            dict['title'] = project.title
            dict["page_title"] = project.page_title
            dict['short_text'] = project.short_text
            dict['description'] = project.description
            dict['video'] = domain_url+project.video.url if project.video else project.video_url
            dict['image'] = project.image.url if project.image else None
            dict['date'] = project.date

            projects.append(dict)
        
        testimonial = list(self.tstm.values())

        context = {
            "projects": projects,"testimonials": testimonial if testimonial else None,
        }
        return JsonResponse(context, safe=True)

@csrf_exempt
def project_details(request):
    domain_url = request.build_absolute_uri('/')[:-1]

    if request.method == 'POST':
        project = request.POST.get('project', None)
        if project is not None:
            split_project = project.split('@') # ['12 unique examples of portfolio websites12', '34', '2023-12-10'] ==> [title,id,date]
            project_id = split_project[1] 

            get_project = Project.objects.filter(id=project_id)
            if get_project.exists():
                get_project = get_project.first()
                project_dict = {}
                project_dict['id'] = get_project.id
                project_dict['title'] = get_project.title
                project_dict["page_title"] = get_project.page_title
                project_dict['short_text'] = get_project.short_text
                project_dict['description'] = get_project.description
                project_dict['video'] = domain_url+get_project.video.url if get_project.video else get_project.video_url
                project_dict['image'] = get_project.image.url if get_project.image else None
                project_dict['date'] = get_project.date

                context = {
                    "status": 200,
                    "project":project_dict
                }
            else:
                context = {
                    "status": 500,
                    "error": "This project is not exist"
                }
        else:
            context = {
                "status": 500,
                "error": "Required parameter missing"
            }

    else:
        context = {
            "status": 500,
            "error": "Invalid requests"
        }
                   
    return JsonResponse(context, safe=True)

class BlogView(View):
    def __init__(self):
        self.obj = Blog.objects.all().order_by("-date")
    
    def get(self, request):
        blogs = list(self.obj.values())

        context = {
            "blogs":blogs
        }
        return JsonResponse(context, safe=True)

@csrf_exempt
def blog_details(request):
    if request.method == 'POST':
        blog = request.POST.get('blog', None)
        if blog is not None:
            split_blog = blog.split('@') # ['12 unique examples of portfolio websites12', '34', '2023-12-10'] ==> [title,id,date]
            blog_id = split_blog[1] 

            get_blog = Blog.objects.filter(id=blog_id)
            if get_blog.exists():
                get_blog = list(get_blog.values())

                context = {
                    "status": 200,
                    "blog":get_blog
                }
            else:
                context = {
                    "status": 500,
                    "error": "This blog is not exist"
                }
        else:
            context = {
                "status": 500,
                "error": "Required parameter missing"
            }

    else:
        context = {
            "status": 500,
            "error": "Invalid requests"
        }
                   
    return JsonResponse(context, safe=True)


class ContactView(View):
    def __init__(self):
        self.obj = Contact.objects.first()
    
    def get(self, request):
        page_title = self.obj.page_title
        text = self.obj.text
        btn_text = self.obj.btn_text
        contact = self.obj.contact.all()
        location = self.obj.location

        contact = list(contact.values())

        context = {
            "text": text, "btn_text": btn_text, "page_title":page_title,
            "contact": contact, "location": location
        }
        return JsonResponse(context, safe=True)
    
    @csrf_exempt
    def post(self, request):
        print(request.POST)
        return JsonResponse({"success": "message successfully received"})

def send_contact_mail(name,user_email,subject,message):
    # send mail that user made a leave request
    email_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>{subject}</title>
    <style>
        body {{
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 20px;
            color: #333;
        }}
        .container {{
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
            overflow: hidden;
            padding: 20px;
        }}
        .header {{
            text-align: center;
            padding-bottom: 20px;
            border-bottom: 1px solid #eee;
        }}
        .header h1 {{
            margin: 0;
            font-size: 24px;
            color: #4A90E2;
        }}
        .content {{
            margin-top: 20px;
            font-size: 16px;
            line-height: 1.6;
        }}
        .applicationBox {{
            width: 100%;
            height: auto;
            min-height: 200px;
            background-color: #e8f0fe;
            border-radius: 4px;
            font-family: 'Courier New', Courier, monospace;
            font-size: 14px;
            padding: 15px;
            border: 1px solid #cfd8dc;
            box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
            white-space: pre-wrap;
            overflow-wrap: break-word;
            margin-top: 20px;
        }}
        .footer {{
            margin-top: 30px;
            font-size: 14px;
            color: #777;
            text-align: center;
        }}
        /* Optional: Responsive adjustments */
        @media (max-width: 600px) {{
            body {{
                padding: 10px;
            }}
            .container {{
                padding: 15px;
            }}
        }}
    </style>
    </head>
    <body>
    <div class="container">
        <div class="header">
            <h1>{subject}</h1>
        </div>
        <div class="content">
            <p><strong>From email:</strong> {email}</p>
            <p><strong>Name:</strong> {name}</p>
            <div class="applicationBox" readonly>
    {message}
            </div>
        </div>
        <div class="footer">
            &copy; {year} By Tanjim Abubokor. All rights reserved.
        </div>
    </div>
    </body>
    </html>
    """.format(
        subject=subject,
        email=user_email,
        name=name,
        message=message,
        year=2023
    )

    email_to = "abubokortanjim@gmail.com"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email_to, ]
    email = EmailMultiAlternatives(
            subject,
            message,
            email_from,
            recipient_list
    )
    email.attach_alternative(email_template, 'text/html')
    response = email.send()
    if response:
        return {'success': True}
    else:
        return {'success': False}

@csrf_exempt
def contact_view(request):

    if request.method == "POST":
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        subject = request.POST.get('subject', None)
        message = request.POST.get('message', None)

        response = send_contact_mail(name, email, subject, message)
        return JsonResponse(response,safe=True)

    elif request.method == "GET":
        obj = Contact.objects.first()

        page_title = obj.page_title
        text = obj.text
        btn_text = obj.btn_text
        contact = obj.contact.all()
        location = obj.location

        contact = list(contact.values())

        context = {
            "text":text,"btn_text":btn_text,"page_title":page_title,
            "contacts":contact,"location":location
        }
        return JsonResponse(context,safe=True)