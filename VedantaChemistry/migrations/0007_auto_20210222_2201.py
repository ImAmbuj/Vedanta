# Generated by Django 3.0.1 on 2021-02-22 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VedantaChemistry', '0006_auto_20210219_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='auth_token',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='contact',
            field=models.IntegerField(),
        ),
    ]
