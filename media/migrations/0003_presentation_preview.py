# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tehpug.utils
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_auto_20150201_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentation',
            name='preview',
            field=imagekit.models.fields.ProcessedImageField(default='file.jpg', upload_to=tehpug.utils.set_upload_path),
            preserve_default=False,
        ),
    ]
