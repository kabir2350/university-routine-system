# Generated by Django 3.0.4 on 2020-04-07 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0011_auto_20200328_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='section',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=20, null=True),
        ),
    ]
