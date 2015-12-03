# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scout', '0005_ward_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='email',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='first_names',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='surname',
        ),
    ]
