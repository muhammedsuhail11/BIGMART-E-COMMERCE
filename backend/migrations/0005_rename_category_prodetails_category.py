# Generated by Django 4.1.4 on 2022-12-23 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_rename_discription_prodetails_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prodetails',
            old_name='CATEGORY',
            new_name='Category',
        ),
    ]
