from django.db import models
import os
# Create your models here.
from rest_framework.exceptions import ValidationError


def validate_file_extension(value):
    """
    Agar fayl kengaytmasi berilganlarning orasida bo'lmasa, xatolik beradi
    """
    # [0]  yo'li + fayl nomi
    # [1] fayl kengaytmasi,: .docx, .jpg

    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

def validate_video_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.MP4']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

def validate_audies_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.MP3']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class Profile(models.Model):
    name = models.CharField(max_length=100,blank=False, null=True)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    created = models.DateField(auto_now_add=True)


class Order(models.Model):
    date = models.DateField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)


class Categories(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True)


class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True)
    image = models.ImageField(upload_to='portfolio', blank=True, default='default.png')
    description = models.TextField(blank=False, null=True)
    price = models.IntegerField(blank=False, null=False)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, related_name="product")


class Order_detail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    count = models.IntegerField(blank=True, null=True, default=0)