# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('semis', '0002_auto_20150923_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='reg_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
