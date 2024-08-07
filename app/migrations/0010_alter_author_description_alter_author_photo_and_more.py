# Generated by Django 5.0.6 on 2024-06-02 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_gallery_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.ImageField(blank=True, default='images/default_photo.jpg', null=True, upload_to='images', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='Фотография'),
        ),
    ]
