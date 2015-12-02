# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('work_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(default=None, blank=True, null=True)),
                ('branches', models.ManyToManyField(to='scout.Branch')),
                ('district', models.ForeignKey(to='scout.District')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('first_names', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=50)),
                ('sa_id_number', models.CharField(max_length=13)),
                ('date_of_birth', models.DateField()),
                ('postal_address', models.CharField(max_length=200)),
                ('work_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('cell_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('sex', models.CharField(default='F', max_length=1, choices=[('F', 'Female'), ('M', 'Male')])),
                ('marital_status', models.CharField(default='SI', max_length=2, choices=[('SI', 'Single'), ('MA', 'Married'), ('PA', 'Partnership'), ('CI', 'Civil union'), ('DI', 'Divorced'), ('SE', 'Separated'), ('WI', 'Widowed')])),
                ('occupation', models.CharField(max_length=50)),
                ('employer', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('first_names', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=50)),
                ('application_date', models.DateField(default=datetime.date.today)),
                ('sa_id_number', models.CharField(max_length=13)),
                ('date_of_birth', models.DateField(default=datetime.date.today)),
                ('email', models.EmailField(max_length=254)),
                ('sex', models.CharField(default='F', max_length=1, choices=[('F', 'Female'), ('M', 'Male')])),
                ('residential_address', models.CharField(max_length=200)),
                ('home_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('cell_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('religious_denomination', models.CharField(max_length=100)),
                ('special_conditions', models.CharField(max_length=200)),
                ('medical_aid_scheme', models.CharField(max_length=50)),
                ('medical_aid_number', models.CharField(max_length=20)),
                ('medical_aid_principal_member', models.CharField(max_length=200)),
                ('branch', models.ForeignKey(to='scout.Branch')),
                ('doctor', models.ForeignKey(to='scout.Doctor')),
                ('group', models.ForeignKey(to='scout.Group')),
                ('parent1', models.ForeignKey(related_name='ward_parent1', to='scout.Parent')),
                ('parent2', models.ForeignKey(related_name='ward_parent2', to='scout.Parent')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='province',
            field=models.ForeignKey(to='scout.Province'),
        ),
    ]
