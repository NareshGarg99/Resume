from django.shortcuts import render

# Create your views here.

def home(request):
    context = {'home': 'active', 'title':'Resume'}
    return render(request, 'base/home.html', context)   

def contact(request):
    context = {'contact': 'active', 'title':'contact us'}
    return render(request, 'base/contact.html', context) 