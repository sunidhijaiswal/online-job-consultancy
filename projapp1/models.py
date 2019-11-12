from django.db import models
class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    message = models.CharField(max_length=1000)
    mob_no  =  models.CharField(max_length=10)
    time = models.DateTimeField(auto_now_add=True)
                                #sys date
          #if data are in no aur ascii then it covert
    def __unicode__(self):
        return "%s" %(self.first_name)

    def __str__(self):
        return "%s" %(self.first_name)


class Careers(models.Model):
    job_title = models.CharField(max_length=30,editable=True)
    experience_reqiured = models.IntegerField(default = '0',editable=True)
    req_skills = models.CharField(max_length=100,default='skils required',null = False,editable=True)
    job_description = models.TextField(max_length=5000,null = True,editable = True)
    contact_no = models.CharField(max_length = 10, editable = True,default='0000000')
    updated_time = models.DateTimeField(auto_now_add=False,auto_now=True)
    job_id = models.CharField(max_length=8,default=0)
    job_location = models.CharField(max_length = 15,default = 'location')
