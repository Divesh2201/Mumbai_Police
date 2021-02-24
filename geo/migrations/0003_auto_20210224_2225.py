# Generated by Django 3.1.6 on 2021-02-24 16:55

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0002_auto_20210221_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maha1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_0', models.BigIntegerField()),
                ('iso', models.CharField(max_length=3)),
                ('name_0', models.CharField(max_length=75)),
                ('id_1', models.BigIntegerField()),
                ('name_1', models.CharField(max_length=75)),
                ('type_1', models.CharField(max_length=50)),
                ('engtype_1', models.CharField(max_length=50)),
                ('nl_name_1', models.CharField(max_length=50)),
                ('varname_1', models.CharField(max_length=150)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.DeleteModel(
            name='Maha0',
        ),
    ]