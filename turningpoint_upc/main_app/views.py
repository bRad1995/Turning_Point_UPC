from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import StaffMember, Event

def home(request):
    return render(request, 'home.html')

def our_story(request):
    return render(request, 'our_story.html')

def staff_index(request):
    staffs = StaffMember.objects.all()
    return render(request, 'staff_members/staff_index.html', {'staffmembers': staffs})

def events_index(request):
    return render(request, 'events/events_index.html')

def contact_us(request):
    return render(request, 'contact.html')

class AddStaff(CreateView):
    model = StaffMember
    fields = '__all__'
    success_url = '/members/'

class StaffUpdate(UpdateView):
    model = StaffMember
    fields = '__all__'
    success_url = '/members/'

class StaffDelete(DeleteView):
    model = StaffMember
    success_url = '/members/'