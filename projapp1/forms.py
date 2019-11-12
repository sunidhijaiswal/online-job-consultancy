from django import forms
from .models import Contact,Careers

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=50)
    mob_no = forms.IntegerField(max_value=10)
    message = forms.CharField(max_length=1000)
class contact(forms.Form):
    class Meta:
        model = Contact
        field = ('first_name','last_name','email','message')

class CareersForm(forms.Form):
    job_title = forms.CharField(max_length=30)
    experience_required = forms.CharField(max_length=8)
    req_skills = forms.CharField(max_length=100)
    job_description = forms.CharField(max_length=10)

class Careersform(forms.Form):
    class Meta:
        model = Careers
        fields = ['id','job_title','experiance_required','req_skills','job_description','conact_no','job_location']

