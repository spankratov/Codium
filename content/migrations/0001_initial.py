# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('short_name', models.SlugField(unique=True)),
                ('affects', models.CharField(max_length=500)),
                ('requirements', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ActionTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('type', models.CharField(max_length=30)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(to='content.Action', editable=False, null=True, related_name='translations')),
            ],
            options={
                'default_permissions': (),
                'db_tablespace': '',
                'managed': True,
                'db_table': 'content_action_translation',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('short_name', models.SlugField(unique=True)),
                ('min_value', models.IntegerField(null=True, blank=True)),
                ('max_value', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AttributeTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(to='content.Attribute', editable=False, null=True, related_name='translations')),
            ],
            options={
                'default_permissions': (),
                'db_tablespace': '',
                'managed': True,
                'db_table': 'content_attribute_translation',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('short_name', models.SlugField(unique=True)),
                ('affects', models.CharField(max_length=500)),
                ('requirements', models.CharField(max_length=500)),
                ('chance', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(to='content.Event', editable=False, null=True, related_name='translations')),
            ],
            options={
                'default_permissions': (),
                'db_tablespace': '',
                'managed': True,
                'db_table': 'content_event_translation',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('company_name', models.CharField(max_length=50)),
                ('short_name', models.SlugField(unique=True)),
                ('affects', models.CharField(max_length=500)),
                ('requirements', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JobTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(to='content.Job', editable=False, null=True, related_name='translations')),
            ],
            options={
                'default_permissions': (),
                'db_tablespace': '',
                'managed': True,
                'db_table': 'content_job_translation',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Knowledge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('short_name', models.SlugField(unique=True)),
                ('requirements', models.CharField(max_length=500)),
                ('edges', models.ManyToManyField(to='content.Knowledge')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KnowledgeTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('type', models.CharField(max_length=30)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(to='content.Knowledge', editable=False, null=True, related_name='translations')),
            ],
            options={
                'default_permissions': (),
                'db_tablespace': '',
                'managed': True,
                'db_table': 'content_knowledge_translation',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('short_name', models.SlugField(unique=True)),
                ('affects', models.CharField(max_length=500)),
                ('requirements', models.CharField(max_length=500)),
                ('time_spending', models.PositiveIntegerField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('description', models.TextField()),
                ('type', models.CharField(max_length=30)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(to='content.Project', editable=False, null=True, related_name='translations')),
            ],
            options={
                'default_permissions': (),
                'db_tablespace': '',
                'managed': True,
                'db_table': 'content_project_translation',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('short_name', models.SlugField(unique=True)),
                ('cost', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PropertyTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('type', models.CharField(max_length=30)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(to='content.Property', editable=False, null=True, related_name='translations')),
            ],
            options={
                'default_permissions': (),
                'db_tablespace': '',
                'managed': True,
                'db_table': 'content_property_translation',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('short_name', models.SlugField(unique=True)),
                ('affects', models.CharField(max_length=500)),
                ('requirements', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UniversityTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(to='content.University', editable=False, null=True, related_name='translations')),
            ],
            options={
                'default_permissions': (),
                'db_tablespace': '',
                'managed': True,
                'db_table': 'content_university_translation',
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='universitytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='propertytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='projecttranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='knowledgetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='jobtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='eventtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='attributetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='actiontranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
