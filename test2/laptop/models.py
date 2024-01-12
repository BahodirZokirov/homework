from django.db import models

# Create your models here.






class Laptop (models.Model):
    name = models.CharField(max_length=25)
    model_p = models.CharField(max_length=25)
    color = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.ImageField(upload_to= 'media')



    def __str__(self):
        return self.name
