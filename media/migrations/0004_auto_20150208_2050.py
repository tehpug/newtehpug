# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pug_sessions', '0004_auto_20150208_2050'),
        ('media', '0003_presentation_preview'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='session',
            field=models.ForeignKey(default=1, to='pug_sessions.PugSession'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='session',
            field=models.ForeignKey(default=1, to='pug_sessions.PugSession'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='presentation',
            name='session',
            field=models.ForeignKey(default=1, to='pug_sessions.PugSession'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='session',
            field=models.ForeignKey(default=1, to='pug_sessions.PugSession'),
            preserve_default=False,
        ),
    ]
