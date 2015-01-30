# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20150130_1643'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='technology',
            new_name='technologies',
        ),
    ]
