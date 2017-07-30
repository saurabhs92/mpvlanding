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
    context = {
        'context_title': title,
        'form': form,
    }
    return render(request, "home.html", context)
