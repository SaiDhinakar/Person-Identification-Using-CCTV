from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def outsiders(request):
    return render(request, 'outsider.html')

def id_detection(request):
    return render(request, 'IDdetection.html')