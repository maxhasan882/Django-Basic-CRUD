from django.db import models

# Create your models here.


class Price(models.Model):
    first = models.IntegerField()
    last = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return str(self.first)+" to "+str(self.last)+" price is "+str(self.price)


class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    code = models.CharField(max_length=20, null=False)
    slug = models.SlugField(max_length=30, null=False, unique=True)
    color = models.CharField(max_length=30, null=True)
    size = models.IntegerField(null=True)
    price = models.ManyToManyField(Price, related_name='product_price')

    def __str__(self):
        return self.name