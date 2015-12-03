# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scout', '0006_auto_20151203_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ward',
            name='email',
        ),
        migrations.RemoveField(
            model_name='ward',
            name='first_names',
        ),
        migrations.RemoveField(
            model_name='ward',
            name='surname',
        ),
    ]
