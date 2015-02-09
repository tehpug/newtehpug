# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pug_sessions', '0005_pugsession_memberss'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pugsession',
            old_name='memberss',
            new_name='members',
        ),
    ]
