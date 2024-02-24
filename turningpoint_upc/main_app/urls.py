from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('our_story/', views.our_story, name='our_story_index'),
    path('members/', views.staff_index, name='staff_index'),
    path('events/', views.events_index, name='events_index'),
    path('contact/', views.contact_us, name='contact_us'),
    path('members/create/', views.AddStaff.as_view(), name='add_staff'),
    path('members/<int:pk>/update/', views.StaffUpdate.as_view(), name='staff_update'),
    path('members/<int:pk>/delete/', views.StaffDelete.as_view(), name='staff_delete'),
    path('events/create/', views.AddEvent.as_view(), name='add_event'),
    path('events/<int:pk>/update/', views.EventUpdate.as_view(), name='event_update'),
    path('events/<int:pk>/delete/', views.EventDelete.as_view(), name='event_delete'),

    
]