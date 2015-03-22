# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('json_app', '0002_auto_20150322_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='area',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
