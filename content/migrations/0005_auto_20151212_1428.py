# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20151204_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='knowledgetranslation',
            name='type',
        ),
        migrations.AddField(
            model_name='knowledge',
            name='type',
            field=models.CharField(max_length=30, default='skill'),
            preserve_default=False,
        ),
    ]
