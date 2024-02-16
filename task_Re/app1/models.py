from django.db import models

#required=False,
class CityInformation(models.Model):
    id = models.AutoField(primary_key=True)
    geonameid = models.IntegerField()
    name = models.CharField(max_length = 200)
    asciiname = models.CharField(max_length = 200)
    alternatenames = models.TextField(blank=True, null =True, max_length = 10000)
    latitude = models.CharField(max_length = 10)
    longitude = models.CharField(max_length = 10)
    feature_class = models.CharField(max_length = 1, null=True, blank=True)
    feature_code = models.CharField(max_length = 10, null = True, blank=True)
    country_code = models.CharField(max_length = 2, null = True, blank=True)
    admin1_code = models.CharField(max_length = 20, null = True, blank=True)
    
    
    population = models.IntegerField(null = True, blank=True)

    dem = models.CharField(max_length = 200, null = True, blank=True)
    timezone = models.CharField(max_length = 40)
    modification_data = models.DateField()