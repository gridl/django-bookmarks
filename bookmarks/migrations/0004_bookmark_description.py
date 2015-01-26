# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0003_bookmark_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='description',
            field=models.CharField(max_length=200, default=''),
            preserve_default=False,
        ),
    ]
