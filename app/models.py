from django.db import models
import os
from django.utils.deconstruct import deconstructible
from django.utils.crypto import get_random_string

@deconstructible
class PathGenerator:
    def __init__(self, sub_path):
        self.sub_path = sub_path

    def __call__(self, instance, filename):
        ext = os.path.splitext(filename)[1]
        filename = get_random_string(length=10) + ext
        return os.path.join(self.sub_path, filename)


class PriceList(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование работ')
    unit = models.CharField(max_length=50, verbose_name='Ед. изм.')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена, руб.')

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название услуги')
    first_paragraph = models.TextField(max_length=300, verbose_name='Первый абзац')
    second_paragraph = models.TextField(max_length=300, verbose_name='Второй абзац')
    third_paragraph = models.TextField(max_length=300, verbose_name='Третий абзац')
    fourth_paragraph = models.TextField(max_length=300, verbose_name='Четвёртый абзац')
    icon = models.ImageField(upload_to=PathGenerator('images/'), verbose_name='Иконка')
    photo = models.ImageField(upload_to=PathGenerator('images/'), verbose_name='photo')

    def __str__(self):
        return self.name


class Author(models.Model):
    fullname = models.CharField(max_length=200, verbose_name='ФИО')
    photo = models.ImageField(upload_to=PathGenerator('images/'), default='images/default_photo.jpg', verbose_name='Фотография', null=True, blank=True)
    description = models.TextField(max_length=300, verbose_name='Описание', null=True, blank=True)
    
    def __str__(self):
        return self.fullname
    

class Works(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='Название проекта')
    description = models.TextField(max_length=300, verbose_name='Описание')
    first_paragraph = models.TextField(verbose_name='Первый параграф')
    second_paragraph = models.TextField(verbose_name='Второй параграф')
    third_paragraph = models.TextField(verbose_name='Третий параграф')
    fourth_paragraph = models.TextField(verbose_name='Четвёртый параграф')
    photo = models.ImageField(upload_to=PathGenerator('images/'), verbose_name='Фотография')
    category = models.CharField(max_length=200, verbose_name='Категория')
    day = models.CharField(max_length=15, verbose_name='День')
    mounth = models.CharField(max_length=15, verbose_name='Месяц')
    year = models.CharField(max_length=15, verbose_name='Год')

    def __str__(self):
        return self.name
    

class Comments(models.Model):
    work = models.ForeignKey(Works, on_delete=models.CASCADE, related_name='comments', verbose_name='Проект')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    message = models.TextField(verbose_name='Сообщение')
    date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.work.name


class Gallery(models.Model):
    image = models.ImageField(upload_to=PathGenerator('images/'), verbose_name='Фотография')


class Mail(models.Model):
    mail = models.CharField(max_length=50, verbose_name='Адрес почты')
    password = models.CharField(max_length=50, verbose_name='Пароль')

    def __str__(self):
        return self.mail


class Contacts(models.Model):
    phone_number = models.CharField(max_length=50, verbose_name='Номер телефона')

    def __str__(self):
        return self.phone_number








