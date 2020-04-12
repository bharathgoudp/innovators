from django.db import models

class Bloodonate(models.Model):
    name = models.CharField(max_length=20)
    group = models.CharField(max_length=20)
    email = models.EmailField()
    contact = models.IntegerField()
    address = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class President(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='president')
    phone = models.IntegerField()
    Address = models.CharField(max_length=20)
    email = models.EmailField()
    def __str__(self):
        return self.name

class VicePres(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='vicepres')
    phone = models.IntegerField()
    Address = models.CharField(max_length=20)
    email = models.EmailField()
    def __str__(self):
        return self.name   
    
class Secretory(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='secretory')
    phone = models.IntegerField()
    Address = models.CharField(max_length=20)
    email = models.EmailField()
    def __str__(self):
        return self.name 

class Jointsecretory(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='jointsecretory')
    phone = models.IntegerField()
    Address = models.CharField(max_length=20)
    email = models.EmailField()
    def __str__(self):
        return self.name

class Members(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to = 'members')
    phone = models.IntegerField()
    Address = models.CharField(max_length=20)
    email = models.EmailField()
    def __str__(self):
        return self.name


class All(models.Model):
    allimage = models.ImageField(upload_to = 'allimages')

class Bloodimg(models.Model):
    bloodimage = models.ImageField(upload_to = 'allimages')

class Moneyimg(models.Model):
    moneyimage = models.ImageField(upload_to = 'allimages')

class Foodimg(models.Model):
    foodimage = models.ImageField(upload_to = 'allimages')
