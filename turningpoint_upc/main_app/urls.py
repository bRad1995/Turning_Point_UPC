from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('our_story/', views.our_story, name='our_story_index'),
    path('members/', views.staff_index, name='staff_index'),
    path('events/', views.events_index, name='events_index'),
    path('contact/', views.contact_us, name='contact_us'),
]