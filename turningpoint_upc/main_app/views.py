from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def our_story(request):
    return render(request, 'our_story.html')

def staff_index(request):
    return render(request, 'staff_members/staff_index.html')

def events_index(request):
    return render(request, 'events/events_index.html')

def contact_us(request):
    return render(request, 'contact.html')
