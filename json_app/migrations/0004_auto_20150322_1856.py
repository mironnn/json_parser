# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('json_app', '0003_auto_20150322_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='area',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
    ]
