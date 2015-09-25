# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('semis', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card_info',
            old_name='card_comment',
            new_name='card_name',
        ),
    ]
