# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('json_app', '0004_auto_20150322_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='area',
            field=models.FloatField(default=None, max_length=4, null=True, blank=True),
            preserve_default=True,
        ),
    ]
