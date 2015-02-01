# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields
import tehpug.utils


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='thumbnail',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=tehpug.utils.set_upload_path),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='video',
            name='preview',
            field=imagekit.models.fields.ProcessedImageField(upload_to=tehpug.utils.set_upload_path),
            preserve_default=True,
        ),
    ]
