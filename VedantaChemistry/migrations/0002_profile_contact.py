# Generated by Django 3.0.1 on 2021-02-08 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VedantaChemistry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contact',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]