from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def videocard(request):
    return render(request,  'videocard.html')

def cpu(request):
    return render(request, 'cpu.html')