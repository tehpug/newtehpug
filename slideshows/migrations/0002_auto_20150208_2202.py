# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tehpug.utils


class Migration(migrations.Migration):

    dependencies = [
        ('slideshows', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slideshow',
            name='image',
            field=models.ImageField(upload_to=tehpug.utils.set_upload_path),
            preserve_default=True,
        ),
    ]
