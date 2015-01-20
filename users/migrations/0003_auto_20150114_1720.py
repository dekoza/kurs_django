# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20141217_1725'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bibliouser',
            options={'permissions': (('can_rent', 'Can rent a book'),)},
        ),
    ]
