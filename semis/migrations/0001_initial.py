# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card_info',
            fields=[
                ('card_id', models.AutoField(serialize=False, primary_key=True)),
                ('card_comment', models.CharField(max_length=20)),
                ('card_num', models.CharField(null=True, max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Cost_type_info',
            fields=[
                ('cost_type_id', models.AutoField(serialize=False, primary_key=True)),
                ('cost_type_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Dept_info',
            fields=[
                ('dept_id', models.AutoField(serialize=False, primary_key=True)),
                ('dept_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite_category',
            fields=[
                ('favorite_id', models.AutoField(serialize=False, primary_key=True)),
                ('cost_type_id', models.ForeignKey(to='semis.Cost_type_info')),
            ],
        ),
        migrations.CreateModel(
            name='Level_info',
            fields=[
                ('level_id', models.AutoField(serialize=False, primary_key=True)),
                ('level_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Project_info',
            fields=[
                ('project_id', models.AutoField(serialize=False, primary_key=True)),
                ('project_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rank_info',
            fields=[
                ('rank_id', models.AutoField(serialize=False, primary_key=True)),
                ('rank_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Spend',
            fields=[
                ('spend_id', models.AutoField(serialize=False, primary_key=True)),
                ('cost', models.IntegerField()),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(max_length=100)),
                ('pay_type', models.CharField(max_length=10)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('cost_type_id', models.ForeignKey(to='semis.Cost_type_info')),
            ],
        ),
        migrations.CreateModel(
            name='Team_info',
            fields=[
                ('team_id', models.AutoField(serialize=False, primary_key=True)),
                ('team_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User_info',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('user_id', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=11)),
                ('employee', models.CharField(max_length=15)),
                ('reg_date', models.DateTimeField(auto_now=True)),
                ('dept_id', models.ForeignKey(to='semis.Dept_info')),
                ('level_id', models.ForeignKey(to='semis.Level_info')),
                ('rank_id', models.ForeignKey(to='semis.Rank_info')),
                ('team_id', models.ForeignKey(to='semis.Team_info')),
            ],
        ),
        migrations.AddField(
            model_name='spend',
            name='id',
            field=models.ForeignKey(to='semis.User_info'),
        ),
        migrations.AddField(
            model_name='spend',
            name='project_id',
            field=models.ForeignKey(to='semis.Project_info'),
        ),
        migrations.AddField(
            model_name='favorite_category',
            name='id',
            field=models.ForeignKey(to='semis.User_info'),
        ),
        migrations.AddField(
            model_name='card_info',
            name='id',
            field=models.ForeignKey(to='semis.User_info'),
        ),
    ]
