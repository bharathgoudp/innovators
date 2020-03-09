from django.db import models

class Bloodonate(models.Model):
    name = models.CharField(max_length=20)
    group = models.CharField(max_length=20)
    email = models.EmailField()
    contact = models.IntegerField()
    address = models.CharField(max_length=20)
    def __str__(self):
        return self.name


    
