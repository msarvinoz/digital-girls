from django.db import models
from phone_field import PhoneField
from django.db.models import Model
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users/', blank=True, null=True)
    bio = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class MainPage(models.Model):
    title = models.CharField(max_length=100)
    text_ru = models.TextField(null=True)
    text_uz = models.TextField(null=True)
    image = models.ImageField(upload_to='media/')


class About(models.Model):
    title_ru = models.CharField(max_length=100)
    title_uz = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)


class AboutItems(models.Model):
    text_ru = models.TextField()
    text_uz = models.TextField()
    image = models.ImageField(upload_to='media/')
    is_active = models.BooleanField(default=False)


class Direction(models.Model):
    title_ru = models.CharField(max_length=100)
    title_uz = models.CharField(max_length=100)


class DirectionItems(models.Model):
    directions_ru = models.CharField(max_length=80)
    directions_uz = models.CharField(max_length=80)
    image = models.ImageField(upload_to='media/')


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
    phone = models.IntegerField()
    created = models.DateField(auto_now_add=True)


class Results(models.Model):
    title_ru = models.CharField(max_length=100)
    title_uz = models.CharField(max_length=100)


class ResultItems(models.Model):
    title_ru = models.CharField(max_length=100)
    title_uz = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')


class Info(models.Model):
    title_ru = models.CharField(max_length=100, null=True, blank=True)
    title_uz = models.CharField(max_length=100, null=True, blank=True)
    website = models.URLField()
    phone = PhoneField()
    email = models.EmailField()
    address_ru = models.CharField(max_length=255)
    address_uz = models.CharField(max_length=255)
    map = models.URLField()
    logo = models.ImageField(upload_to='media/')
    instagram = models.URLField()
    telegram = models.URLField()
    you_tube = models.URLField()
    facebook = models.URLField()

