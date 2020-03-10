from django.db import models


class Bloodonate(models.Model):
    name = models.CharField(max_length=20)
    group = models.CharField(max_length=20)
    email = models.EmailField()
    contact = models.IntegerField()
    address = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class President(models.Model):
    pname = models.CharField(max_length=50)
    mblno = models.IntegerField()
    paddress = models.CharField(max_length=300)
    pemail = models.EmailField()
    desg = models.CharField(max_length=20)
    pimg = models.FileField(upload_to='pimg/')


class Secretary(models.Model):
    sname = models.CharField(max_length=50)
    smblno = models.IntegerField()
    saddress = models.CharField(max_length=300)
    semail = models.EmailField()
    simg = models.FileField(upload_to='simg/')


class Members(models.Model):
    mname = models.CharField(max_length=50)
    mblno = models.IntegerField()
    maddress = models.CharField(max_length=300)
    memail = models.EmailField()
    mimg = models.FileField(upload_to='mimg/')



