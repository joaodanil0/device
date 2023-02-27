from django.http import HttpResponse
from django.shortcuts import redirect
from device.forms import RegisterDevice
from device.models import Device

# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterDevice(request.POST, request.FILES)
        model = request.POST.get("model")
        device_exist = Device.objects.filter(model = model)

        if device_exist:
            return redirect('/?status=2')
        
        if form.is_valid():
            form.save()
            return redirect('/?status=0')
        else:
            return redirect('/?status=1')