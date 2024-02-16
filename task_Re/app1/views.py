from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CityInformation
from .serializers import CitySerializer

import pytz
from datetime import datetime


class CityByGeonameid(APIView):
    def get(self, request):
        try:
            geonameid = request.data['geonameid']
        except:
            return Response({"Error": "Некорректный ввод"})
        try:
            inf = model_to_dict(CityInformation.objects.get(geonameid = geonameid))
            del inf['id']
            return Response(inf)
        except:
            return Response({'Error':'Нет населенного пункта с таким параметром'})


class PageOfCities(APIView):
    def get(self, request):

        lenOfTable = 377304 
        try:
            countOfRecords = request.data['countOfRecords']
            numberOfPage = request.data['numberOfPage']
        except:
            return Response({"Error": "Некорректный ввод"})
        if (numberOfPage * countOfRecords) > lenOfTable:
            inf = CityInformation.objects.filter(id__range = ( ((numberOfPage-1) * countOfRecords)+1, lenOfTable)).values()
        else:
            inf = CityInformation.objects.filter(id__range = ( ((numberOfPage-1) * countOfRecords)+1, (numberOfPage-1) * countOfRecords +countOfRecords)).values()
        return Response(list(inf))


class CoupleOfCities(APIView):
    def get(self, request):
        try:
            firstCityName =  request.data['firstCityName']
            secondCityName =  request.data['secondCityName']
        except:
            return Response({"Error": "Некорректный ввод"})
        try:
            firstCity = model_to_dict(CityInformation.objects.filter(alternatenames__contains = firstCityName).order_by("population").last())
            secondCity = model_to_dict(CityInformation.objects.filter(alternatenames__contains = secondCityName).order_by("population").last())
            del firstCity['id']
            del secondCity['id']
            if float(firstCity.get('latitude')) > float(secondCity.get('latitude')):
                northestCity = firstCityName
            elif float(firstCity.get('latitude')) < float(secondCity.get('latitude')):
                northestCity = firstCityName
            else:
                northestCity = "The same..."

            timeZone = abs(int(datetime.now(pytz.timezone(firstCity.get('timezone'))).strftime('%z'))/100 - int(datetime.now(pytz.timezone(secondCity.get('timezone'))).strftime('%z'))/100)
            if timeZone != 0:
                isTimezoneSame = False
            else:
                isTimezoneSame = True
            inf = {
                'first_city': firstCity,
                'second_city': secondCity,
                'northest_city': northestCity,
                'isTimezoneSame': isTimezoneSame,
                'deltaTime': timeZone
                
            }
            return Response(inf)
        except:
            return Response({'Error':'Нет населенного пункта с таким названием'})


class SearchingOfNames(APIView):
    def get(self, request):
        try:
            geoname = request.data['geoname']
        except:
           return Response({"Error": "Некорректный ввод"}) 
        inf = CityInformation.objects.filter(alternatenames__contains = geoname).values()
        mas=[]
        for i in inf:
            for k in i.get('alternatenames').split(','):
                if (geoname in k) & (k not in mas):
                    mas.append(k) 
        return Response(mas)