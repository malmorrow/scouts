# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scout', '0002_auto_20151203_0830'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parent',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='ward',
            old_name='user_id',
            new_name='user',
        ),
    ]
