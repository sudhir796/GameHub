from django.shortcuts import render

def home(request):
    return render(request, 'Home.html')

def features(request):
    return render(request, 'Features.html')

