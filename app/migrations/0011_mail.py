# Generated by Django 5.0.6 on 2024-06-02 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_author_description_alter_author_photo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.CharField(max_length=50, verbose_name='Адрес почты')),
                ('password', models.CharField(max_length=50, verbose_name='Пароль')),
            ],
        ),
    ]
