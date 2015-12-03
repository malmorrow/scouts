# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scout', '0003_auto_20151203_0830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ward',
            name='user',
        ),
    ]
