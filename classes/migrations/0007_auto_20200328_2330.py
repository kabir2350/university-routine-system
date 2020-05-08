# Generated by Django 3.0.4 on 2020-03-28 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timings', '0002_auto_20200328_2327'),
        ('days', '0002_auto_20200328_2327'),
        ('classes', '0006_remove_class_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='days.Day'),
        ),
        migrations.AlterField(
            model_name='class',
            name='timing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timings.Timing'),
        ),
    ]
