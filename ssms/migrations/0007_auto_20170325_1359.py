# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ssms', '0006_auto_20170324_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wear',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Final Submission Date'),
        ),
    ]
