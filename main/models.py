from django.db import models
from phone_field import PhoneField


class MainPage(models.Model):
    title = models.CharField(max_length=100)
    text_ru = models.TextField(null=True)
    text_uz = models.TextField(null=True)
    image = models.ImageField(upload_to='mainimage/')


class About(models.Model):
    title_ru = models.CharField(max_length=100)
    title_uz = models.CharField(max_length=100)


class AboutItems(models.Model):
    text_ru = models.TextField()
    text_uz = models.TextField()
    image = models.ImageField(upload_to='aboutimage/')


class Direction(models.Model):
    title_ru = models.CharField(max_length=100)
    title_uz = models.CharField(max_length=100)


class DirectionItems(models.Model):
    directions_ru = models.CharField(max_length=80)
    directions_uz = models.CharField(max_length=80)
    image = models.ImageField(upload_to='directionsimage/')


class Tasks(models.Model):
    title_ru = models.CharField(max_length=100)
    title_uz = models.CharField(max_length=100)


class TaskItems(models.Model):
    number = models.IntegerField(unique=True)
    requirements_ru = models.CharField(max_length=255)
    requirements_uz = models.CharField(max_length=255)


class Register(models.Model):
    title_ru = models.CharField(max_length=100)
    title_uz = models.CharField(max_length=100)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    birth = models.DateField()
    email = models.EmailField()
    address = models.CharField(max_length=255)
    phone = PhoneField()


class Results(models.Model):
    title_ru = models.CharField(max_length=100)
    title_uz = models.CharField(max_length=100)


class ResultItems(models.Model):
    title_ru = models.CharField(max_length=100)
    title_uz = models.CharField(max_length=100)
    image = models.ImageField(upload_to='resultimage')


class Info(models.Model):
    title_ru = models.CharField(max_length=100, null=True, blank=True)
    title_uz = models.CharField(max_length=100, null=True, blank=True)
    website = models.URLField()
    phone = PhoneField()
    email = models.EmailField()
    address_ru = models.CharField(max_length=255)
    address_uz = models.CharField(max_length=255)
    latitude = models.FloatField()
    longtitude = models.FloatField()
    logo = models.ImageField(upload_to='infoimage')
    instagram = models.URLField()
    telegram = models.URLField()
    you_tube = models.URLField()
    facebook = models.URLField()


class RegistrationTab(models.Model):
    tab_ru = models.CharField(max_length=50)
    tab_uz = models.CharField(max_length=50)
