# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150114_1720'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bibliouser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
