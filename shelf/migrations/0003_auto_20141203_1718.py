# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0002_auto_20141125_2345'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name_plural': 'Authors', 'verbose_name': 'Author', 'ordering': ('last_name', 'first_name')},
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(verbose_name='first name', max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(verbose_name='last name', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bookedition',
            name='isbn',
            field=models.CharField(blank=True, max_length=17),
            preserve_default=True,
        ),
    ]
