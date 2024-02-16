from django.core.management.base import BaseCommand, CommandParser
from app1.models import CityInformation
import codecs

class Command(BaseCommand):
    help = 'update db'
    

    def handle(self, *args, **options):
        f = codecs.open( "RU.txt", "r", "utf_8_sig" )

        mas = []
        i=0
        for line in f:
            line.replace("'", "’")
            ar = line.split("\t")
            i+=1
            #self.stdout.write(str(len(list(f))), ending="")

            self.stdout.write(str(round(i/377303*100, 2))+'% of Task 1\n', ending="")
            mas.append(CityInformation(geonameid = ar[0], name = ar[1], asciiname = ar[2], alternatenames = ar[3],  latitude = ar[4], longitude = ar[5], feature_class = ar[6], feature_code = ar[7], country_code = ar[8], admin1_code = ar[10], population = ar[14], dem = ar[16], timezone = ar[17], modification_data = ar[18]))
        n=0
        for i in mas:
            n+=1
            self.stdout.write(str(round(n/377303*100, 2))+'% of Task 2\n', ending="")

            i.save()
        