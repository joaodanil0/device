from django.http import HttpResponse
from django.shortcuts import redirect
from device.forms import RegisterDevice

# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterDevice(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return HttpResponse(form)