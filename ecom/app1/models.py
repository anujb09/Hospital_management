from django.db import models


# Create your models here.

class Product(models.Model):

    c1=((1,'Clothes'),(2,'Mobile'),(3,'Shoes'))

    name=models.CharField(max_length=50,verbose_name='Product')

    price=models.FloatField()

    cat=models.IntegerField(choices=c1)

    details=models.CharField(max_length=100)

    is_active=models.BooleanField(default=True)


class Demo(models.Model):

    name=models.CharField(max_length=30)

    email=models.EmailField()

    mobile=models.BigIntegerField()