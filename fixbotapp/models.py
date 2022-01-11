from django.db import models

#the model for the telemetric data
class TelemetricModel(models.Model):
    temperature = models.CharField(max_length=20)
    car_speed = models.CharField(max_length=20)
    car_longitude = models.CharField(max_length=20)
    car_latitude = models.CharField(max_length=20)
    fuel_consumption_rate = models.CharField(max_length=20)
    