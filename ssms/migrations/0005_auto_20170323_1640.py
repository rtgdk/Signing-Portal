# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssms', '0004_auto_20170216_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='meal',
            field=models.CharField(default='Workshop', max_length=16, verbose_name='Event Type', choices=[('Workshop', 'Workshop'), ('Prof Shows', 'Prof Shows')]),
        ),
        migrations.AlterField(
            model_name='wear_student',
            name='meal',
            field=models.CharField(default='S', max_length=16, verbose_name='Size Selected', choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')]),
        ),
    ]
