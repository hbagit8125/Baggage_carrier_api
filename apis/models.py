from django.db import models

class carrier(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    available_weight = models.FloatField()
    price_per_kg = models.FloatField()

