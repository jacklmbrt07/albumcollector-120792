# Generated by Django 3.1.1 on 2020-09-16 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_listen_album'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listen',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='listen',
            name='date',
            field=models.DateTimeField(verbose_name='listen date'),
        ),
    ]