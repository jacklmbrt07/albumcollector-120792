# Generated by Django 3.1.1 on 2020-09-16 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20200915_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='instruments',
            field=models.ManyToManyField(to='main_app.Instrument'),
        ),
    ]