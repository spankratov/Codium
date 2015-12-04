# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20151201_0809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='knowledge',
            name='edges',
        ),
        migrations.AddField(
            model_name='knowledge',
            name='children',
            field=models.ManyToManyField(related_name='parents', to='content.Knowledge'),
        ),
    ]
