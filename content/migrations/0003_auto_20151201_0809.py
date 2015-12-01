# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_attribute_default'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='default',
            field=models.IntegerField(),
        ),
    ]
