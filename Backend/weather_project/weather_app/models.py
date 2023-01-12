from django.db import models

# Create your models here.
class Data(models.Model):
    temperature = models.IntegerField()
    city = models.CharField(max_length=50)
    wind_speed = models.IntegerField()
    humidity = models.FloatField()
    date = models.CharField(max_length=11)
    plz = models.IntegerField(primary_key=True)
