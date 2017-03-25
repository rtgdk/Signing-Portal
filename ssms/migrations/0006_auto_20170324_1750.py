# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ssms', '0005_auto_20170323_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateMailStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('mails', models.IntegerField(default=0, verbose_name='Mails Sent')),
            ],
        ),
        migrations.AlterField(
            model_name='event_student',
            name='meal',
            field=models.CharField(default='Workshop', max_length=16, verbose_name='Size Selected', choices=[('Workshop', 'Workshop'), ('Prof Shows', 'Prof Shows')]),
        ),
        migrations.AlterField(
            model_name='wear',
            name='meal',
            field=models.CharField(default='T Shirt', max_length=16, verbose_name='Wear Type', choices=[('T Shirt', 'T Shirt'), ('Sweat Shirt', 'Sweat Shirt')]),
        ),
    ]
