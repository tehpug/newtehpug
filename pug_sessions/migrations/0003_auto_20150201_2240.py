# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0003_presentation_preview'),
        ('pug_sessions', '0002_auto_20150129_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='pugsession',
            name='audio',
            field=models.ForeignKey(blank=True, to='media.Audio', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pugsession',
            name='image',
            field=models.ForeignKey(blank=True, to='media.Image', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pugsession',
            name='presentation',
            field=models.ForeignKey(blank=True, to='media.Presentation', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pugsession',
            name='video',
            field=models.ForeignKey(blank=True, to='media.Video', null=True),
            preserve_default=True,
        ),
    ]
