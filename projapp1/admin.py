from django.contrib import admin
from .models import Contact,Careers

class Contactadmin(admin.ModelAdmin):
    list_display = ['first_name','email','message','time']
    list_filter = ['time']
    class meta:
        model = Contact

class Careersadmin(admin.ModelAdmin):
    list_display = ['job_title','req_skills','contact_no','updated_time']
    list_filter = ['job_title','updated_time','job_id']
    class meta:
        model = Careers

admin.site.register(Contact,Contactadmin)
admin.site.register(Careers,Careersadmin)

