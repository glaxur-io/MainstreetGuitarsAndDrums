from django.db import models


class Instruments(models.Model):
    type = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=2000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField()
    instagram = models.URLField(max_length=300, default="https://www.instagram.com/mainstreetvintageguitar/")


class Equipment(models.Model):
    type = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=2000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField()
    instagram = models.URLField(max_length=300, default="https://www.instagram.com/mainstreetvintageguitar/")

