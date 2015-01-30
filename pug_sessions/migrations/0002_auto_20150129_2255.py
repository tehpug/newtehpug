# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pug_sessions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pugsession',
            name='date',
        ),
        migrations.AlterField(
            model_name='place',
            name='address',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pugsession',
            name='description',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
