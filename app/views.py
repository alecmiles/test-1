from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Resident, Event, Property, Announcement
from .forms import ResidentForm, EventForm



class HomePageView(TemplateView):
    template_name = 'app/home.html'


class AboutPageView(TemplateView):
    template_name = 'app/about.html'


# Admin Dashboard 
class AdminDashboardView(TemplateView):
    template_name = 'app/admin_dashboard.html'



class ResidentListView(ListView):
    model = Resident
    template_name = 'app/admin_resident_list.html' 
    context_object_name = 'residents'

    def get_queryset(self):
        queryset = Resident.objects.all()
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                first_name__icontains=search_query) | queryset.filter(
                last_name__icontains=search_query) | queryset.filter(
                email__icontains=search_query)
        return queryset


class ResidentCreateView(CreateView):
    model = Resident
    form_class = ResidentForm
    template_name = 'app/admin_add_resident.html'
    success_url = reverse_lazy('resident_list')


class ResidentUpdateView(UpdateView):
    model = Resident
    form_class = ResidentForm
    template_name = 'app/admin_edit_resident.html'
    success_url = reverse_lazy('resident_list')


class ResidentDeleteView(DeleteView):
    model = Resident
    template_name = 'app/admin_resident_confirm_delete.html'
    success_url = reverse_lazy('resident_list')


# Event Views using Class-Based Views (CBVs)
class EventListView(ListView):
    model = Event
    template_name = 'app/event_list.html'
    template_name = 'app/admin_event_list.html'
    context_object_name = 'events'


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'app/event_form.html'
    success_url = reverse_lazy('event_list')


class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'app/event_form.html'
    success_url = reverse_lazy('event_list')


class EventDeleteView(DeleteView):
    model = Event
    template_name = 'app/event_confirm_delete.html'
    success_url = reverse_lazy('event_list')


# Property and Announcement Views
class PropertyListView(ListView):
    model = Property
    template_name = 'app/property_list.html'
    context_object_name = 'properties'


class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'app/announcement_list.html'
    context_object_name = 'announcements'

