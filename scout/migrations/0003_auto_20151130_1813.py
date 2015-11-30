# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scout', '0002_auto_20151130_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ward',
            name='branches',
        ),
        migrations.AddField(
            model_name='group',
            name='branches',
            field=models.ManyToManyField(to='scout.Branch'),
        ),
        migrations.AddField(
            model_name='ward',
            name='branch',
            field=models.ForeignKey(to='scout.Branch', default=1),
            preserve_default=False,
        ),
    ]
