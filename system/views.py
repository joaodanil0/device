from django.http import HttpResponse
from django.shortcuts import render
from device.forms import RegisterDevice

# Create your views here.
def home(request):
    form = RegisterDevice()
    return render(request, 'home.html', {"form":form})
