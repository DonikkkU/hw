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



class Specialty(models.Model):
    name = models.CharField(blank=True, null=True, max_length=50)



class Teacher(models.Model):
    first_name = models.CharField(blank=True, null=True, max_length=50)
    last_name = models.CharField(blank=True, null=True, max_length=50)
    phone = models.CharField(blank=True, null=True, max_length=50)
    specialty = models.ForeignKey(Specialty, on_delete=models.SET_NULL, null=True)




class Group(models.Model):
    name = models.CharField(blank=True, null=True, max_length=50)
    start_date = models.DateField()
    start_time = models.TimeField()
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    speciality = models.ForeignKey(Specialty, on_delete=models.SET_NULL, null=True)


class Group_info(models.Model):
    name = models.CharField(blank=True, null=True, max_length=50)
    start_date = models.DateField()
    start_time = models.TimeField()
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    speciality = models.ForeignKey(Specialty, on_delete=models.SET_NULL, null=True)
    created = models.DateField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)


class Theme(models.Model):
    name = models.CharField(blank=True, null=True, max_length=50)


class Lesson(models.Model):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    is_active = models.BooleanField(default=True)
    about = models.CharField(max_length=100)
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True)

class Student(models.Model):
    first_name = models.CharField(blank=True, null=True, max_length=50)
    last_name = models.CharField(blank=True, null=True, max_length=50)
    birth_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='portfolio', blank=True, default='default.png')
    phone = models.CharField(blank=True, null=True, max_length=50)
    email = models.CharField(blank=True, null=True, max_length=50)
    payment = models.BooleanField(default=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)



class Lesson_student(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    homework_check = models.BooleanField(blank=True, null=True)
    participation = models.BooleanField(blank=True, null=True)




class Payer(models.Model):
    first_name = models.CharField(blank=True, null=True, max_length=50)
    last_name = models.CharField(blank=True, null=True, max_length=50)
    payer = models.CharField(blank=True, null=True, max_length=50)
    phone_number = models.CharField(blank=True, null=True, max_length=50)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)


