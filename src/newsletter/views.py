from django.shortcuts import render

# Create your views here.

def home(request):
    title = 'Welcome'
    if request.user.is_authenticated():
        title = 'Hi %s' %(request.user)
    context = {
        'context_title': title,
    }
    return render(request, "home.html", context)
