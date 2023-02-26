from django import forms
from device.models import Device

class RegisterDevice(forms.ModelForm):
    class Meta:
        model = Device
        fields =  "__all__"
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows':4, 'cols':30}),
            'register_date': forms.TextInput(attrs={'class': 'form-control', 'type':'date'}),
        }
