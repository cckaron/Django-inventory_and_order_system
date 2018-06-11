# Generated by Django 2.0.6 on 2018-06-06 18:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cName', models.CharField(max_length=20)),
                ('cSpot', models.CharField(default='自取', max_length=20)),
                ('cPhone', models.CharField(max_length=10)),
                ('cDate', models.DateField()),
                ('c1T100', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(0)])),
                ('c1T120', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(0)])),
                ('c1T130', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(0)])),
                ('c1T140', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(0)])),
                ('c1T150', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(0)])),
                ('c2T100', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(0)])),
                ('c2T120', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(0)])),
                ('c2T130', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(0)])),
                ('c2T140', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(0)])),
                ('c2T150', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(0)])),
                ('c3M50', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]