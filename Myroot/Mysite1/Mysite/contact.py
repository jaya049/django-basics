from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
#from .models import Event
#from .forms import ContactForm
  
  
class ContactForm(forms.Form):
    yourname = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(required=False,label='Your e-mail address')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
 
 
def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            #form.save()
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'contact/contact.html', {'form': form, 'submitted': submitted})