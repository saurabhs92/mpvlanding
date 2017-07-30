from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.

def home(request):
    title = 'Welcome'
    #if request.user.is_authenticated():
    #    title = 'Hi %s' %(request.user)

    if request.method == "POST":
        print (request.POST)
        
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if not instance.full_name:
            instance.full_name = "Undefined Full Name"
        instance.save()
        print (instance.full_name)
        print (instance.email)
        print (instance.timestamp)
    context = {
        'title': title,
        'form': form,
    }
    return render(request, "home.html", context)
