# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(default=b'male', max_length=16),
        ),
    ]
