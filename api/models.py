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


class Category(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name
class Items(models.Model):
    name=models.CharField(max_length=250)
    pictures=models.ImageField(upload_to='items/')
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

class Basket(models.Model):
    name=models.CharField(max_length=250)
    phone = models.CharField(max_length=250)


    def __str__(self):
        return self.name


class Basketproducts(models.Model):
    basket=models.ForeignKey(Basket,on_delete=models.CASCADE,related_name='products')
    items=models.ForeignKey(Items,on_delete=models.CASCADE)
    count=models.IntegerField()

    def __str__(self):
        return f"Basket {self.basket.id} - Item {self.items.id} (Count: {self.count})"

class Cat(models.Model):
    name=models.CharField(max_length=250)


    def __str__(self):
        return self.name
class Case(models.Model):
    name = models.CharField(max_length=250)
    pictures = models.ImageField(upload_to='case/')
    description=models.TextField()
    categories=models.ForeignKey(Cat,on_delete=models.CASCADE,related_name='cat')



    def __str__(self):
        return self.name


class Reels(models.Model):
    link=models.URLField()


    def __str__(self):
        return self.link
