# Generated by Django 4.1.4 on 2023-01-04 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_rename_email_contactdb_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdb',
            name='Email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]