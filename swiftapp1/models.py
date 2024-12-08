from django.db import models

# Create your models here.


class Material(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='material_images/')

    def __str__(self):
        return self.name                                            
    
class Contact(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.email