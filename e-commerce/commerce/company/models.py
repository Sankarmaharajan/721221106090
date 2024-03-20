from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    owner_name = models.CharField(max_length=50)
    roll_number = models.IntegerField()
    owner_email = models.CharField(max_length=50)
    access_code = models.CharField(max_length=50)

class Product(models.Model):
    productname  = models.CharField(max_length=50)
    price        = models.IntegerField()
    rating       = models.FloatField()
    discount     = models.IntegerField()
    availability = models.CharField(max_length=50)