from django.shortcuts import render

def home(request):
    return render(request, 'coins/home.html')
