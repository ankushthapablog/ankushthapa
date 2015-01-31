# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accesslogs',
            name='page_name',
            field=models.CharField(max_length=100, null=True, verbose_name=b'page name', blank=True),
            preserve_default=True,
        ),
    ]
