# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('user_id', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=10)),
                ('dept_id', models.IntegerField()),
                ('team_id', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=11)),
                ('employee', models.CharField(max_length=15)),
                ('rank_id', models.IntegerField()),
                ('level_id', models.IntegerField()),
                ('reg_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
