from django.http import HttpResponse
from django.shortcuts import render
from device.forms import RegisterDevice
from device.models import Device

# Create your views here.
def home(request):
    form = RegisterDevice()
    status = request.GET.get('status')
    devices = Device.objects.all()
    return render(request, 'home.html', {"form":form, 'status': status, 'devices': devices})
