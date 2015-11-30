# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ward',
            name='branch',
        ),
        migrations.AddField(
            model_name='branch',
            name='name',
            field=models.CharField(max_length=20, default='empty'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ward',
            name='branches',
            field=models.ManyToManyField(to='scout.Branch'),
        ),
        migrations.AddField(
            model_name='ward',
            name='email',
            field=models.EmailField(max_length=254, default='empty'),
            preserve_default=False,
        ),
    ]
