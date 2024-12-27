from django.db import models

# Create your models here.

class Devos(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='devos/')
    bio = models.TextField()

    def __str__(self):
       return  self.name

class Features(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='features/')


    def __str__(self):
        return self.name

class Cars(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='cars/')
    bio = models.TextField()

    def __str__(self):
       return  self.name


class Featuresdetail(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='Devos/')

    def __str__(self):
        return self.name


class Carsdetail(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='Devos/')
    bio = models.TextField()

    def __dir__(self):
        return self.name

