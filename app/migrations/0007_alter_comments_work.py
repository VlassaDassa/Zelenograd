# Generated by Django 5.0.6 on 2024-06-02 13:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_works_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app.works', verbose_name='Проект'),
        ),
    ]