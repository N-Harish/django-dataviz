from django.db import models


# Create your models here.
class Customer(models.Model):
    Customer_ID = models.IntegerField()
    region = models.CharField(max_length=50)
    division = models.CharField(max_length=50)
    month = models.CharField(max_length=12)
    year = models.IntegerField()
    payment = models.IntegerField()
    bucket = models.CharField(max_length=5)


