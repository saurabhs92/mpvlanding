from django.conf import settings
from django.core.mail import send_mail
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
    title = 'Contact Us'
    form = ContactForm(request.POST or None)
    if form.is_valid():
        #for key in form.cleaned_data:
        #    value = form.cleaned_data.get(key)
        #    print (key, value)
            
        form_email = form.cleaned_data.get('email')
        form_full_name = form.cleaned_data.get('full_name')
        form_message = form.cleaned_data.get('message')

        subject = 'Site Contact Form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'yourotheremail@mail.com']
        contact_message = "%s: %s via %s" % (
            form_full_name,
            form_message,
            form_email)
        some_html_message = """
        <h1> hello </h1>
        """

        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  html_message=some_html_message,
                  fail_silently=False)
        
    context = {
        'form': form,
        'title': title,
    }
    return render(request, "contact.html", context)
