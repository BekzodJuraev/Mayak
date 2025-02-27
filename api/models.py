from django.db import models

# Create your models here.
class Parnters(models.Model):
    pictures=models.ImageField(upload_to='images/')




class Staff(models.Model):
    photo=models.ImageField(upload_to='staff/')
    status=models.CharField(max_length=250)
    name=models.CharField(max_length=250)
    description=models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Orders(models.Model):
    name=models.CharField(max_length=250)
    phone=models.CharField(max_length=250)
    email=models.EmailField()
    message=models.TextField()


    def __str__(self):
        return self.name




