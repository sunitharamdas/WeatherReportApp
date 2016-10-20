from django.db import models

class Reading(models.Model):
    location = models.CharField(max_length=100)
    weather = models.CharField(max_length=20)
    wind_str = models.CharField(max_length=100)
    temperature = models.IntegerField()
    humidity = models.CharField(max_length=10)
    precip = models.CharField(max_length=50)
    icon_url = models.URLField()
    observation_time = models.CharField(max_length=100)


