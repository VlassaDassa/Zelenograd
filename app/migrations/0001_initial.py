# Generated by Django 5.0.6 on 2024-06-02 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование работ')),
                ('unit', models.CharField(max_length=50, verbose_name='Ед. изм.')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена, руб.')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название услуги')),
                ('first_paragraph', models.TextField(max_length=300, verbose_name='Первый абзац')),
                ('second_paragraph', models.TextField(max_length=300, verbose_name='Первый абзац')),
                ('third_paragraph', models.TextField(max_length=300, verbose_name='Первый абзац')),
                ('fourth_paragraph', models.TextField(max_length=300, verbose_name='Первый абзац')),
                ('icon', models.ImageField(upload_to='images', verbose_name='Иконка')),
                ('photo', models.ImageField(upload_to='images', verbose_name='photo')),
            ],
        ),
    ]