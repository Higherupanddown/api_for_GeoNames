from rest_framework import serializers
from .models import CityInformation

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CityInformation
        fields = ('geonameid', 'name', 'alternatenames', 'latitude', 'longitude', 'feature_class', 'feature_code', 'feature_code', 'country_code', 'admin1_code', 'population', 'dem', 'timezone', 'modification_data')