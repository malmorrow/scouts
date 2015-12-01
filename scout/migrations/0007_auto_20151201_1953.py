# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('scout', '0006_auto_20151130_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('work_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('first_names', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=50)),
                ('sa_id_number', models.CharField(max_length=13)),
                ('date_of_birth', models.DateField()),
                ('postal_address', models.CharField(max_length=200)),
                ('work_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('cell_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('sex', models.CharField(max_length=1, choices=[('F', 'Female'), ('M', 'Male')], default='F')),
                ('marital_status', models.CharField(max_length=2, choices=[('SI', 'Single'), ('MA', 'Married'), ('PA', 'Partnership'), ('CI', 'Civil union'), ('DI', 'Divorced'), ('SE', 'Separated'), ('WI', 'Widowed')], default='SI')),
                ('occupation', models.CharField(max_length=50)),
                ('employer', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='ward',
            name='cell_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, default='+27821234567'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ward',
            name='medical_aid_number',
            field=models.CharField(max_length=20, default='123456789'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ward',
            name='medical_aid_principal_member',
            field=models.CharField(max_length=200, default='Malachy Morrow'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ward',
            name='medical_aid_scheme',
            field=models.CharField(max_length=50, default='Discovery Classic Priority'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ward',
            name='religious_denomination',
            field=models.CharField(max_length=100, default='None'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ward',
            name='sex',
            field=models.CharField(max_length=1, choices=[('F', 'Female'), ('M', 'Male')], default='F'),
        ),
        migrations.AddField(
            model_name='ward',
            name='special_conditions',
            field=models.CharField(max_length=200, default='None'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ward',
            name='doctor',
            field=models.ForeignKey(to='scout.Doctor', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ward',
            name='parent1',
            field=models.ForeignKey(default=1, related_name='ward_parent1', to='scout.Parent'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ward',
            name='parent2',
            field=models.ForeignKey(default=2, related_name='ward_parent2', to='scout.Parent'),
            preserve_default=False,
        ),
    ]
