# Generated by Django 3.1.1 on 2020-09-15 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_instrument'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('method', models.CharField(choices=[('1', 'In the Car'), ('2', 'With Headphones'), ('3', 'In a Video')], default='1', max_length=1)),
            ],
        ),
    ]
