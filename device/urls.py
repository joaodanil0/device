
from django.urls import path
from device import views

urlpatterns = [
    path("register/", views.register, name="device_register"),
]