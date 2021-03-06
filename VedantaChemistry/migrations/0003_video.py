# Generated by Django 3.0.1 on 2021-02-09 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VedantaChemistry', '0002_profile_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='Videos')),
                ('title', models.TextField(max_length=1000)),
                ('standard', models.CharField(choices=[('11th', '11th'), ('12th', '12th')], max_length=50)),
            ],
        ),
    ]
