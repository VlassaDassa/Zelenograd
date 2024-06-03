from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from . import models

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from django.conf import settings



def get_contacts(request):
    phone_number = models.Contacts.objects.all().values()[0]
    mail = models.Mail.objects.all().values()[0]    

    context = {
        'data': {
            'phone_number': phone_number,
            'mail': mail,
        }
    }
    return JsonResponse(context)


def index(request):
    services = models.Service.objects.all().values()
    works = models.Works.objects.all().values()
    photos = models.Gallery.objects.all().values()
    
    context = {'data': {
        'services': services,
        'works': works,
        'photos': photos,
        
    }}
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    data = models.Works.objects.all().values()
    context = {'data': data}
    return render(request, 'blog.html', context)

def blog_detail(request, id):
    data = models.Works.objects.get(id=id)
    context = {'data': data}
    return render(request, 'blog-detail.html', context)

def company(request):
    return render(request, 'company.html')

def projects_detail(request):
    return render(request, 'projects-detail.html')

def projects(request):
    return render(request, 'projects.html')

def services(request):
    data = models.Service.objects.all().values()
    context = {'data': data}
    return render(request, 'services.html', context)


@csrf_exempt
def send_mail(request):
    mail = models.Mail.objects.all()[0]

    data = request.POST 
    name = data.get('name', 'No name')

    email = data.get('email', 'No name')
    user_message = data.get('message', 'No message')
    
    smtp_server  = 'smtp.yandex.ru'
    smtp_port  = 587
    sender_email = mail.mail
    password = mail.password

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls() 
    server.login(sender_email, password)

    message = MIMEMultipart()
    message['From'] = sender_email  
    message['To'] = email
    message['Subject'] = f'Здравствуйте, {name}. Вы оставляли у нас свою почту'

    body = f'Здравствуйте, {name}. Вы оставляли у нас свою почту с таким сообщением: "{user_message}"'
    message.attach(MIMEText(body, 'plain'))

    server.send_message(message)

    server.quit()

    return JsonResponse({'success': True})


def get_price_list(request):
    data = list(models.PriceList.objects.all().values())
    return JsonResponse({'data': data})

def get_services(request):
    data = list(models.Service.objects.all().values())
    return JsonResponse({'data': data})

def get_service(request, id):
    data = models.Service.objects.get(id=id)
    context = {'data': data}
    return render(request, 'service-detail.html', context)

@csrf_exempt
def add_comment(request):
    try:
        data = request.POST
        author = models.Author.objects.create(
            fullname=data['name']
        )
        author.save()

        comment = models.Comments.objects.create(
            work = models.Works.objects.get(id=data['work_id']),
            author = author,
            message = data['message'],   
        )
        comment.save()

        return JsonResponse({'success': True})
    except Exception as _ex:
        print(_ex)
        return JsonResponse({'success': False})

    


    
