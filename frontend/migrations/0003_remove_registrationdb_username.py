# Generated by Django 4.1.4 on 2022-12-30 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_rename_registarction_registrationdb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationdb',
            name='Username',
        ),
    ]
