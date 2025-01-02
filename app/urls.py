from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    AdminDashboardView,
    ResidentListView,
    ResidentCreateView,
    ResidentUpdateView,
    ResidentDeleteView,
    EventListView,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
    PropertyListView,
    AnnouncementListView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('admin_dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    
    path('residents/', ResidentListView.as_view(), name='resident_list'),
    path('residents/add/', ResidentCreateView.as_view(), name='add_resident'),
    path('residents/edit/<int:pk>/', ResidentUpdateView.as_view(), name='edit_resident'),
    path('residents/delete/<int:pk>/', ResidentDeleteView.as_view(), name='delete_resident'),

    path('events/', EventListView.as_view(), name='event_list'),
    path('events/add/', EventCreateView.as_view(), name='event_create'),
    path('events/edit/<int:pk>/', EventUpdateView.as_view(), name='event_edit'),
    path('events/delete/<int:pk>/', EventDeleteView.as_view(), name='event_delete'),

    path('properties/', PropertyListView.as_view(), name='property_list'),
    path('announcements/', AnnouncementListView.as_view(), name='announcement_list'),
]
