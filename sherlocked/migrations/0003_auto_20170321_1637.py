# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sherlocked', '0002_auto_20170321_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_story',
            field=models.TextField(max_length=10000, null=True, blank=True),
        ),
    ]
