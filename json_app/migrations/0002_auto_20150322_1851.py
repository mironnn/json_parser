# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('json_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='area',
            field=models.IntegerField(default=None, max_length=4),
            preserve_default=True,
        ),
    ]
