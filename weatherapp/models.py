from django.db import models

# Create your models here.
class Weather(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.city