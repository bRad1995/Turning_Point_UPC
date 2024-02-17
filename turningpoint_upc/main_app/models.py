from django.db import models


class StaffMember (models.Model):
    name = models.CharField(max_length=250)
    role = models.CharField(max_length=250)
    about = models.TextField

    def __def__(self):
        return self.name
    
class Event (models.Model):
    name = models.CharField(max_length=250)
    date = models.DateField
    time = models.TimeField
    location = models.CharField(max_length=250)
    description = models.TextField

    def __def__(self):
        return self.name