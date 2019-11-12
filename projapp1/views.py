from __future__ import unicode_literals
from django.conf import settings
import requests
# import mammoth
from django.shortcuts import render
from django.core.mail import send_mail
import random
from .forms import ContactForm
from .models import Contact , Careers

def home(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        mob_no = form.cleaned_data['mob_no']
        message = form.cleaned_data['message']
        create = Contact.objects.get.objects.get_or_create(first_name=first_name,last_name=last_name,email=email,message=message)
        subject = 'ThankYou for contacting us'
        email_message = 'we get in few moments'
        Form_mail = settings.EMAIL_HOST_USER
        to_list = [email,settings.EMAIL_HOST_USER]
        send_mail(subject,email_message,Form_mail,to_list,fail_silently=False)
        res = requests.post('https://textbelt.com/text',{
            'phone': mob_no,
            'message':'Hello World',
            'key': 'textbelt',
        })
        print(res.json())
    return render(request,'index.html',{})

def careers(request):
    order_by = Careers.objects.order_by('-id')

    template = "careers.html"
    context = {'order':order_by,'id':id}

    return render(request,template,context)

def ourprojects(request):
    template = 'ourprojects.html'
    return render(request,template)

def dammi(request):
    template = 'dammi.html'
    context = {
        }
    return render(request,template,context)
