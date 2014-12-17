# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0003_auto_20141203_1718'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name_plural': 'authors', 'ordering': ('last_name', 'first_name'), 'verbose_name': 'author'},
        ),
        migrations.AlterField(
            model_name='bookedition',
            name='book',
            field=models.ForeignKey(to='shelf.Book', related_name='editions'),
            preserve_default=True,
        ),
    ]
