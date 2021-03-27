from django.contrib import admin

# Register your models here.
from .models import Venue,Event,Registration
admin.site.register(Venue)
#admin.site.register(MyClubUser)
admin.site.register(Event)
admin.site.register(Registration)
