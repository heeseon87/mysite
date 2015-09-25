# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('semis', '0002_auto_20150924_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pay_info',
            fields=[
                ('pay_id', models.AutoField(primary_key=True, serialize=False)),
                ('pay_name', models.CharField(max_length=20)),
                ('card_num', models.CharField(null=True, max_length=4)),
                ('id', models.ForeignKey(to='semis.User_info')),
            ],
        ),
        migrations.RemoveField(
            model_name='card_info',
            name='id',
        ),
        migrations.AlterField(
            model_name='spend',
            name='pay_type',
            field=models.ForeignKey(to='semis.Pay_info'),
        ),
        migrations.DeleteModel(
            name='Card_info',
        ),
    ]
