from django.contrib import admin
from .models import Resident, Property, Event, Payment, Announcement

admin.site.register(Resident)
admin.site.register(Property)
admin.site.register(Event)
admin.site.register(Payment)
admin.site.register(Announcement)
