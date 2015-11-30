# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(blank=True, null=True, default=None)),
                ('mal', models.CharField(max_length=2)),
                ('district', models.ForeignKey(to='scout.District')),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('first_names', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=2, choices=[('BR', 'Brownie'), ('CU', 'Cub'), ('GU', 'Guide'), ('SC', 'Scout')], default='CU')),
                ('application_date', models.DateField(default=datetime.date.today)),
                ('sa_id_number', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField(default=datetime.date.today)),
                ('group', models.ForeignKey(to='scout.Group')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='province',
            field=models.ForeignKey(to='scout.Province'),
        ),
    ]
