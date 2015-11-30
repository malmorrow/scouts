# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scout', '0005_auto_20151130_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ward',
            name='sa_id_number',
            field=models.CharField(max_length=13),
        ),
    ]
