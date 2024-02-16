
# api_for_GeoNames
Тестовый проект с реализацией запросов данных из БД по api


# Описание методов 
**Слеш в конце url недопустим
Метод запросов: GET
Для запросов использовался Postman**
## http://127.0.0.1:8000/api/v1/CityByGeonameid
**Запрос**
```
{
"geonameid": 546230
}
```

**Ответ**
```
{
"geonameid": 546230,
"name": "Kolomna",
"asciiname": "Kolomna",
"alternatenames": "Columna,Kalomna,Kolom’na,Kolomna,Kolomnae,Kolomno,Kołomna,ke luo mu na,kollomna,koromuna,kwlwmna,qwlwmnh,Каломна,Коломнæ,Коломна,Коломна балһсн,Коломно,Коломьна,Կոլոմնա,קולומנה,كولومنا,کولومنا,コロムナ,科洛姆纳,콜롬나",
"latitude": "55.07108",
"longitude": "38.78399",
"feature_class": "P",
"feature_code": "PPLA2",
"country_code": "RU",
"admin1_code": "47",
"population": 147690,
"dem": "136",
"timezone": "Europe/Moscow",
"modification_data": "2023-07-11"
}
```

**Входные параметры**
`geonameid` - number

**Выходные параметры**
Успешный запрос
```
geonameid         : integer id of record in geonames database
name              : name of geographical point (utf8)
asciiname         : name of geographical point in plain ascii characters, 
alternatenames    : alternatenames, comma separated, ascii names automatically transliterated, convenience attribute from alternatename table
latitude          : latitude in decimal degrees
longitude         : longitude in decimal degrees
feature class     : see http://www.geonames.org/export/codes.html
feature code      : see http://www.geonames.org/export/codes.html
country code      : ISO-3166 2-letter country code
admin1 code       : fipscode (subject to change to iso code), see exceptions 
population        : bigint (8 byte int) 
elevation         : in meters, integer
dem               : digital elevation model, srtm3 or gtopo30, average elevation of 3''x3'' (ca 90mx90m) or 30''x30'' (ca 900mx900m) area in meters, integer. srtm processed by cgiar/ciat.
timezone          : the iana timezone id (see file timeZone.txt) varchar(40)
modification date : date of last modification in yyyy-MM-dd format
```

Возможные ошибки
```
{
    "Error": "Нет населенного пункта с таким параметром"
}
```
Либо
```
{
    "Error": "Некорректный ввод"
}
```

## http://127.0.0.1:8000/api/v1/PageOfCities
**Запрос**
```
{
    "countOfRecords": 2,
    "numberOfPage": 2
}
```

**Ответ**
```
[
    {
        "id": 3,
        "geonameid": 451749,
        "name": "Zhukovo",
        "asciiname": "Zhukovo",
        "alternatenames": "",
        "latitude": "57.26429",
        "longitude": "34.20956",
        "feature_class": "P",
        "feature_code": "PPL",
        "country_code": "RU",
        "admin1_code": "77",
        "population": 0,
        "dem": "237",
        "timezone": "Europe/Moscow",
        "modification_data": "2011-07-09"
    },
    {
        "id": 4,
        "geonameid": 451750,
        "name": "Zhitovo",
        "asciiname": "Zhitovo",
        "alternatenames": "",
        "latitude": "57.29693",
        "longitude": "34.41848",
        "feature_class": "P",
        "feature_code": "PPL",
        "country_code": "RU",

        "admin1_code": "77",

        "population": 0,

        "dem": "247",

        "timezone": "Europe/Moscow",

        "modification_data": "2011-07-09"

    }
]
```

**Входные параметры**
`countOfRecords` - number, количество отображаемых на странице городов
`numberOfPage` - number, страница 

**Выходные параметры**
Успешный запрос
Arrray of objects, информация о городах (см метод `CityByGeonameid`), также `id` - номер города в списке

**Возможные ошибки**
Пустой ответ в случае неверных данных
```
[]
```
Либо
```
{
    "Error": "Некорректный ввод"
}
```

#### http://127.0.0.1:8000/api/v1/CoupleOfCities
**Запрос**
```
{
    "firstCityName": "Коломна",
    "secondCityName": "Рязань"
}
```

**Ответ**
```
{
    "first_city": {
        "geonameid": 546230,
        "name": "Kolomna",
        "asciiname": "Kolomna",
        "alternatenames": "Columna,Kalomna,Kolom’na,Kolomna,Kolomnae,Kolomno,Kołomna,ke luo mu na,kollomna,koromuna,kwlwmna,qwlwmnh,Каломна,Коломнæ,Коломна,Коломна балһсн,Коломно,Коломьна,Կոլոմնա,קולומנה,كولومنا,کولومنا,コロムナ,科洛姆纳,콜롬나",
        "latitude": "55.07108",
        "longitude": "38.78399",
        "feature_class": "P",
        "feature_code": "PPLA2",
        "country_code": "RU",
        "admin1_code": "47",
        "population": 147690,
        "dem": "136",
        "timezone": "Europe/Moscow",
        "modification_data": "2023-07-11"
    },
    "second_city": {
        "geonameid": 500096,
        "name": "Ryazan’",
        "asciiname": "Ryazan’",
        "alternatenames": "RZN,Resania,Riazan,Riazań,Rjasan,Rjazan,Rjazan’,Rjazanj,Rjazaň,Ryazan,Ryazan’,Ryazan’,liang zan,lyajan,ryazan,Рязань,リャザン,梁赞,랴잔",
        "latitude": "54.6269",
        "longitude": "39.6916",
        "feature_class": "P",
        "feature_code": "PPLA",
        "country_code": "RU",
        "admin1_code": "62",
        "population": 538962,
        "dem": "102",
        "timezone": "Europe/Moscow",
        "modification_data": "2023-01-11"
    },
    "northest_city": "Коломна",
    "isTimezoneSame": true,
    "deltaTime": 0.0
}
```

**Входные параметры**
`secondCityName` - string, название первого города
`numberOfPage` - string, название второго города 

**Выходные параметры**
Успешный запрос
Object, информация о городах (см метод `CityByGeonameid`)
`northest_city` - string, название северного города
`isTimezoneSame` - boolean, одинаковый ли часовой пояс
`deltaTime` - number, разница во времени

**Возможные ошибки**
```
{
    "Error": "Нет населенного пункта с таким названием"
}
```
Либо
```
{
    "Error": "Некорректный ввод"
}
```

#### http://127.0.0.1:8000/api/v1/SearchingOfNames
**Запрос**
```
{
    "geoname": "Коломна"
}
```

**Ответ**
```
[
    "Коломна",
    "Коломна балһсн",
    "Городской Округ Коломна"
]
```

**Входные параметры**
`geoname` - string, частичное название города

**Выходные параметры**
Успешный запрос
Array of strings - возможные названия

**Возможные ошибки**
Пустой ответ при отсутствии вариантов названия
```
[]
```
Либо
```
{
    "Error": "Некорректный ввод"
}
```

## Зависимости
Python 3.11.7, файл requirements.txt

## Запуск сервера
cd task_Re
python.exe manage.py runserver