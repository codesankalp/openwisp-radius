# Generated by Django 3.1.2 on 2020-11-13 01:58

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample_radius', '0004_allowed_mobile_prefixes'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonetoken',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True, max_length=128, null=True, region=None
            ),
        ),
    ]
