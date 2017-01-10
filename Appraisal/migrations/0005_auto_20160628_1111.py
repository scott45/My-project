# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Appraisal', '0004_auto_20160619_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Names',
            field=models.ForeignKey(max_length=30, to=settings.AUTH_USER_MODEL, default=1),
        ),
    ]
