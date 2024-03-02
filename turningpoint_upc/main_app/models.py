from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User



class StaffMember(models.Model):
    name = models.CharField(max_length=250)
    role = models.CharField(max_length=250)
    about = models.TextField(default = 'about')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.CharField(max_length=500, default = 'Upload Image URL')

    def __def__(self):
        return self.name
    
class Event(models.Model):
    name = models.CharField(max_length=250)
    date = models.DateField(default = date.today)
    time = models.TimeField(default = '00:00')
    location = models.CharField(max_length=250)
    description = models.TextField(default = 'description')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __def__(self):
        return self.name
    
class Photo(models.Model):
    url = models.CharField(max_length=200)
    staffmember = models.ForeignKey(StaffMember, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for staffmember_id: {self.staffmember_id} @{self.url}"