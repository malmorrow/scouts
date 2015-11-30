# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('scout', '0004_remove_group_mal'),
    ]

    operations = [
        migrations.AddField(
            model_name='ward',
            name='home_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+27829944364', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ward',
            name='residential_address',
            field=models.CharField(default='545 Reitz St, Sunnyside, Pretoria 0002', max_length=200),
            preserve_default=False,
        ),
    ]
