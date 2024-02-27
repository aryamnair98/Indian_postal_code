# Generated by Django 4.2.10 on 2024-02-24 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postalapp', '0002_postaladdress'),
    ]

    operations = [
        migrations.AddField(
            model_name='postaladdress',
            name='branch_type',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postaladdress',
            name='country',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postaladdress',
            name='pincode',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postaladdress',
            name='state',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
