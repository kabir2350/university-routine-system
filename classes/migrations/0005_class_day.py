# Generated by Django 3.0.4 on 2020-03-28 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_auto_20200328_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='day',
            field=models.CharField(default='', max_length=100),
        ),
    ]
