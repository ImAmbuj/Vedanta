# Generated by Django 3.0.1 on 2021-02-19 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VedantaChemistry', '0005_auto_20210219_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification',
            field=models.CharField(max_length=500),
        ),
    ]
