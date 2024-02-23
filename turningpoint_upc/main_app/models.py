from django.db import models
from django.urls import reverse
from datetime import date



class StaffMember(models.Model):
    name = models.CharField(max_length=250)
    role = models.CharField(max_length=250)
    about = models.TextField(default = 'about')

    def __def__(self):
        return self.name
    # def get_absolute_url(self):
    #     return reverse('staff_index', kwargs={'staffmember_id': self.id})
    
class Event(models.Model):
    name = models.CharField(max_length=250)
    date = models.DateField(default = date.today)
    time = models.TimeField(default = '00:00')
    location = models.CharField(max_length=250)
    description = models.TextField(default = 'description')

    def __def__(self):
        return self.name