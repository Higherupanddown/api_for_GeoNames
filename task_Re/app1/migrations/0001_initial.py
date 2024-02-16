# Generated by Django 5.0.1 on 2024-02-05 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityInformation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('geonameid', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('asciiname', models.CharField(max_length=200)),
                ('alternatenames', models.TextField(blank=True, max_length=10000, null=True)),
                ('latitude', models.CharField(max_length=10)),
                ('longitude', models.CharField(max_length=10)),
                ('feature_class', models.CharField(blank=True, max_length=1, null=True)),
                ('feature_code', models.CharField(blank=True, max_length=10, null=True)),
                ('country_code', models.CharField(blank=True, max_length=2, null=True)),
                ('admin1_code', models.CharField(blank=True, max_length=20, null=True)),
                ('population', models.IntegerField(blank=True, null=True)),
                ('dem', models.CharField(blank=True, max_length=200, null=True)),
                ('timezone', models.CharField(max_length=40)),
                ('modification_data', models.DateField()),
            ],
        ),
    ]