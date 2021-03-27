from django.shortcuts import render
from django.http import HttpResponse 
from django.http import HttpResponseRedirect
from datetime import date
import calendar
from calendar import HTMLCalendar
from .models import Event
from .forms import VenueForm
from .forms import RegistrationForm


# Create your views here.
'''def index(request,year=date.today().year,month=date.today().month):
    #return HttpResponse("<h1>My Event Calender</h1>")
    year = int(year)
    month=int(month)
    if year < 1900 or year > 2099:
        year = date.today().year
    month_name=calendar.month_name[month]
    title="My Event Calendar - %s %s" % (month_name,year)
    cal=HTMLCalendar().formatmonth(year,month)
    #return HttpResponse("<h1>%s</h1><p>%s</p>" % (title,cal))
    return render(request,'base.html',{'title':title,'cal':cal})'''
      
def index(request, year=date.today().year, month=date.today().month):
    year = int(year)
    month = int(month)
    if year < 1900 or year > 2099: year = date.today().year
    month_name = calendar.month_name[month]
    title = "MyClub Event Calendar - %s %s" % (month_name,year)
    cal = HTMLCalendar().formatmonth(year, month)
    announcements = [
    {
        'date': '6-10-2020',
        'announcement': "Club Registrations Open"
    },
    {
        'date': '6-15-2020',
        'announcement': "Joe Smith Elected New Club President"
    }
    ]
    return render(request, 'events/calendar_base.html', {'title': title, 'cal': cal,'announcements': announcements})
##....................
def add_venue(request):
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue/?submitted=True')
    else:
        form = VenueForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_venue.html', {'form': form, 'submitted': submitted})

def registration(request):
    submitted = False
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/registration/?submitted=True')
    else:
        form = RegistrationForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/registration_form.html', {'form': form, 'submitted': submitted})


