# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AttributeLevels',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('level', models.FloatField()),
                ('attribute', models.ForeignKey(to='content.Attribute')),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('days_lived', models.BigIntegerField(default=0)),
                ('seconds_in_current_day', models.PositiveSmallIntegerField(default=0)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('attributes', models.ManyToManyField(to='content.Attribute', through='userdata.AttributeLevels')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterJobs',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('taking_date', models.PositiveIntegerField()),
                ('finished', models.BooleanField(default=False)),
                ('character', models.ForeignKey(to='userdata.Character')),
                ('job', models.ForeignKey(to='content.Job')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterProjects',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('taking_date', models.PositiveIntegerField()),
                ('finished', models.BooleanField(default=False)),
                ('character', models.ForeignKey(to='userdata.Character')),
                ('project', models.ForeignKey(to='content.Project')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterProperties',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('purchase_date', models.PositiveIntegerField()),
                ('character', models.ForeignKey(to='userdata.Character')),
                ('property', models.ForeignKey(to='content.Property')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterUniversities',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('entering_date', models.PositiveIntegerField()),
                ('finished', models.BooleanField(default=False)),
                ('character', models.ForeignKey(to='userdata.Character')),
                ('university', models.ForeignKey(to='content.University')),
            ],
        ),
        migrations.CreateModel(
            name='KnowledgeLevels',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('level', models.FloatField()),
                ('character', models.ForeignKey(to='userdata.Character')),
                ('knowledge', models.ForeignKey(to='content.Knowledge')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='jobs',
            field=models.ManyToManyField(to='content.Job', through='userdata.CharacterJobs'),
        ),
        migrations.AddField(
            model_name='character',
            name='projects',
            field=models.ManyToManyField(to='content.Project', through='userdata.CharacterProjects'),
        ),
        migrations.AddField(
            model_name='character',
            name='properties',
            field=models.ManyToManyField(to='content.Property', through='userdata.CharacterProperties'),
        ),
        migrations.AddField(
            model_name='character',
            name='skills',
            field=models.ManyToManyField(to='content.Knowledge', through='userdata.KnowledgeLevels'),
        ),
        migrations.AddField(
            model_name='character',
            name='universities',
            field=models.ManyToManyField(to='content.University', through='userdata.CharacterUniversities'),
        ),
        migrations.AddField(
            model_name='character',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='attributelevels',
            name='character',
            field=models.ForeignKey(to='userdata.Character'),
        ),
    ]
