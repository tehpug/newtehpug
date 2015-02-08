# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tehpug.utils


class Migration(migrations.Migration):

    dependencies = [
        ('pug_sessions', '0003_auto_20150201_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pugsession',
            name='audio',
        ),
        migrations.RemoveField(
            model_name='pugsession',
            name='image',
        ),
        migrations.RemoveField(
            model_name='pugsession',
            name='presentation',
        ),
        migrations.RemoveField(
            model_name='pugsession',
            name='video',
        ),
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(upload_to=tehpug.utils.set_upload_path),
            preserve_default=True,
        ),
    ]
