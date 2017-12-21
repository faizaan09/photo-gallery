# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0005_auto_20150919_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='time_registered',
            field=models.TimeField(default=datetime.datetime(2015, 9, 19, 11, 27, 10, 820301, tzinfo=utc)),
        ),
    ]
