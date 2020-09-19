from django.shortcuts import render

# Create your views here.
def skill(request):
    context = {'skill': 'active', 'title': 'skills'}
    return render(request, 'education/education.html', context)