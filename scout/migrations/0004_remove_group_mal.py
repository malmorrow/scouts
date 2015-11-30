# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scout', '0003_auto_20151130_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='mal',
        ),
    ]
