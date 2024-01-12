from django.db import models

# Create your models here.
class Phone (models.Model):
    name = models.CharField(max_length=25)
    model = models.CharField(max_length=22)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.ImageField(upload_to='media')
    at_data = models.DateTimeField(auto_now_add=True)
