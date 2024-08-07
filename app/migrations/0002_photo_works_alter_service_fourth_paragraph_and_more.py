# Generated by Django 5.0.6 on 2024-06-02 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/', verbose_name='Фотография')),
            ],
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название проекта')),
                ('description', models.TextField(max_length=300, verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='images', verbose_name='Фотография')),
                ('day', models.CharField(max_length=15, verbose_name='День')),
                ('mounth', models.CharField(max_length=15, verbose_name='Месяц')),
                ('year', models.CharField(max_length=15, verbose_name='Год')),
            ],
        ),
        migrations.AlterField(
            model_name='service',
            name='fourth_paragraph',
            field=models.TextField(max_length=300, verbose_name='Четвёртый абзац'),
        ),
        migrations.AlterField(
            model_name='service',
            name='second_paragraph',
            field=models.TextField(max_length=300, verbose_name='Второй абзац'),
        ),
        migrations.AlterField(
            model_name='service',
            name='third_paragraph',
            field=models.TextField(max_length=300, verbose_name='Третий абзац'),
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photos', models.ManyToManyField(to='app.photo', verbose_name='Фотография')),
            ],
        ),
    ]
