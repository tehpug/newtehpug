# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
        ('pug_sessions', '0004_auto_20150208_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='pugsession',
            name='memberss',
            field=models.ManyToManyField(to='members.Member'),
            preserve_default=True,
        ),
    ]
