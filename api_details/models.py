from django.db import models

# Create your models here.

class WellData(models.Model):
    well_id = models.CharField(max_length=20, unique=True)
    oil = models.IntegerField()
    gas = models.IntegerField()
    brine = models.IntegerField()

    def __str__(self):
        return self.well_id