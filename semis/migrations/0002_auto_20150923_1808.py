# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('semis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
