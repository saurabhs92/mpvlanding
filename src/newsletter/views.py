from django.shortcuts import render
from .forms import ContactForm, SignUpForm
# Create your views here.

def home(request):
    title = 'Welcome'
    form = SignUpForm(request.POST or None)
    
    context = {
        'title': title,
        'form': form,
    }

    if form.is_valid():
        # form.save()
        instance = form.save(commit=False)
        if not instance.full_name:
            instance.full_name = "Undefined Full Name"
        instance.save()
        context = {
            'title': "Thank You for registering"
        }
    return render(request, "home.html", context)

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        for key in form.cleaned_data:
            value = form.cleaned_data.get(key)
            print (key, value)
            
        email = form.cleaned_data.get('email')
        full_name = form.cleaned_data.get('full_name')
        message = form.cleaned_data.get('message')        
    context = {
        'form': form,
    }
    return render(request, "contact.html", context)
