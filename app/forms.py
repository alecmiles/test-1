from django import forms
from .models import Resident, Property, Event, Announcement

class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = '__all__'
        
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location']
