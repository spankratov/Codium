"""
This module contains users-related information.

Tables:
Character -- table that holds exact characters of the game.
AttributeLevels -- many-to-many table with characters and their attributes levels.
CharacterProperties -- many-to-many table with characters and their property.
CharacterUniversities -- many-to-many table with characters and their universities.
CharacterProjects -- many-to-many table with characters and their projects.
CharacterJobs -- many-to-many table with characters and their jobs.
KnowledgeLevels -- many-to-many table with characters and their knowledge levels.
"""
from django.db import models
from django.contrib.auth.models import User


class Character(models.Model):
    """
    Table that holds exact characters of the game.

    Attributes of class:
    user -- link to user that possesses this character
    attributes -- link to many-to-many table with characters and their attributes levels
    properties -- link to many-to-many table with characters and their property
    universities -- link to many-to-many table with characters and their universities
    projects -- link to many-to-many table with characters and their projects
    jobs -- link to many-to-many table with characters and their jobs
    skills -- link to many-to-many table with characters and their knowledge levels
    days_lived -- game days that character played
    seconds_in_current_day -- how much seconds have gone during last saving
    last_update -- real date and time when current character data was loaded on the server
    """
    user = models.OneToOneField(User)
    attributes = models.ManyToManyField('content.Attribute', through='AttributeLevels',
                                        through_fields=('character', 'attribute'))
    properties = models.ManyToManyField('content.Property', through='CharacterProperties',
                                        through_fields=('character', 'property'))
    universities = models.ManyToManyField('content.University', through='CharacterUniversities',
                                          through_fields=('character', 'university'))
    projects = models.ManyToManyField('content.Project', through='CharacterProjects',
                                      through_fields=('character', 'project'))
    jobs = models.ManyToManyField('content.Job', through='CharacterJobs',
                                  through_fields=('character', 'job'))
    skills = models.ManyToManyField('content.Knowledge', through='KnowledgeLevels',
                                    through_fields=('character', 'knowledge'))
    days_lived = models.BigIntegerField(default=0)
    seconds_in_current_day = models.PositiveSmallIntegerField(default=0)
    last_update = models.DateTimeField(auto_now=True)


class AttributeLevels(models.Model):
    """
    Many-to-many table with characters and their attributes levels.

    Attributes of class:
    character -- link to the character
    attribute -- link to the attribute
    level -- level of this attribute for this character
    """
    character = models.ForeignKey(Character)
    attribute = models.ForeignKey('content.Attribute')
    level = models.FloatField()


class CharacterProperties(models.Model):
    """
    Many-to-many table with characters and their property they hold right now
    (so there is no property that character had in past and doesn't have right now).

    Attributes of class:
    character -- link to the character
    property -- link to the property
    purchase_date -- game date when character purchased this property
    (in days that passed since the beginning of the game)
    """
    character = models.ForeignKey(Character)
    property = models.ForeignKey('content.Property')
    purchase_date = models.PositiveIntegerField()


class CharacterUniversities(models.Model):
    """
    Many-to-many table with characters and their universities. There can be universities the character already graduated

    Attributes of class:
    character -- link to the character
    university -- link to the university
    entering_date -- game date when character entered the university
    (in days that passed since the beginning of the game)
    finished -- did character graduate this university?
    """
    character = models.ForeignKey(Character)
    university = models.ForeignKey('content.University')
    entering_date = models.PositiveIntegerField()
    finished = models.BooleanField(default=False)


class CharacterProjects(models.Model):
    """
    Many-to-many table with characters and their projects. There can be projects the character already finished

    Attributes of class:
    character -- link to the character
    project -- link to the project
    name -- name, specified by player
    taking_date -- game date when character took this project
    (in days that passed since the beginning of the game)
    finished -- did character finish this project?
    """
    character = models.ForeignKey(Character)
    project = models.ForeignKey('content.Project')
    name = models.CharField(max_length=50)
    taking_date = models.PositiveIntegerField()
    finished = models.BooleanField(default=False)


class CharacterJobs(models.Model):
    """
    Many-to-many table with characters and their jobs. There can be jobs the character already finished

    Attributes of class:
    character -- link to the character
    job -- link to the job
    taking_date -- game date when character took this job
    (in days that passed since the beginning of the game)
    finished -- did character finish this job?
    """
    character = models.ForeignKey(Character)
    job = models.ForeignKey('content.Job')
    taking_date = models.PositiveIntegerField()
    finished = models.BooleanField(default=False)


class KnowledgeLevels(models.Model):
    """
    Many-to-many table with characters and their knowledge levels. Database stores only skill levels and not area levels
    Area levels are calculated at runtime on clients using values from skill levels of particular area.

    Attributes of class:
    character -- link to the character
    knowledge -- link to the knowledge (only skills)
    level -- knowledge level of this skill for this character
    """
    character = models.ForeignKey(Character)
    knowledge = models.ForeignKey('content.Knowledge', limit_choices_to={'type': 'skill'})
    level = models.FloatField()
