from django.db import models
from datetime import date

# Create your models here.
class Device(models.Model):
    image = models.ImageField(upload_to='devices')
    model = models.CharField(max_length=30)
    name = models.CharField(max_length=30)    
    register_date = models.DateField(default=date.today)
    quantity = models.IntegerField()
    description = models.TextField(blank=True)
    