# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tehpug.utils
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shortlinks', '0002_shortlink_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortlink',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to=tehpug.utils.set_upload_path, blank=True),
            preserve_default=True,
        ),
    ]
