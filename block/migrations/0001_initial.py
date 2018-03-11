# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Block_name', max_length=100)),
                ('desc', models.CharField(verbose_name='Block_Desc', max_length=100)),
                ('manager_name', models.CharField(verbose_name='Block_Admin', max_length=100)),
            ],
        ),
    ]
