"""
This module provides basic structure of content database.

Tables:

Attribute -- attributes of characters (health, mood, motivation, money, etc.
Event -- random events like finding cash and non-random like losing one's job.
Action -- actions like eating food, going to a party or sleeping.
Property -- property that character holds: cars, houses, etc.
University -- universities where character can study in.
Project -- projects where character can be involved.
Job -- regular job for a character.
Knowledge -- character skills like Python programming and skill areas like backend programming.
"""
from django.db import models
from hvad.models import TranslatableModel, TranslatedFields


# TODO: validator for all models
# TODO: representation of 'affects' and 'requirements' fields
# TODO: somehow represent version of database

class Attribute(TranslatableModel):
    """
    Attributes of characters (health, mood, motivation, money, etc.

    Attributes of class:
    name -- full name of the attribute (can be translated)
    short_name -- short name for referring in formulas
    min_value -- minimal value that attribute can hold
    max_value -- maximal value that attribute can hold
    """
    translations = TranslatedFields(
        name=models.CharField(max_length=50)
    )
    short_name = models.SlugField(unique=True)
    default = models.IntegerField(default=None)
    min_value = models.IntegerField(null=True, blank=True)
    max_value = models.IntegerField(null=True, blank=True)


class Event(TranslatableModel):
    """
    Random events like finding cash and non-random like losing one's job.

    Attributes of class:
    name -- full name of the event (can be translated)
    description -- full description of the event (can be translated)
    short_name -- short name for referring in formulas
    affects -- what parameters this event affects
    requirements -- what requirements this event has
    chance -- chance of the event
    """
    translations = TranslatedFields(
        name=models.CharField(max_length=100),
        description=models.TextField()
    )
    short_name = models.SlugField(unique=True)
    affects = models.CharField(max_length=500)
    requirements = models.CharField(max_length=500)
    chance = models.FloatField()


class Action(TranslatableModel):
    """
    Actions like eating food, going to a party or sleeping.

    Attributes of class:
    name -- full name of the action (can be translated)
    description -- full description of the action (can be translated)
    type -- type like working actions, relaxing actions, etc. (can be translated)
    short_name -- short name for referring in formulas
    affects -- what parameters this action affects
    requirements -- what requirements this action has
    """
    translations = TranslatedFields(
        name=models.CharField(max_length=50),
        description=models.TextField(),
        type=models.CharField(max_length=30)
    )
    short_name = models.SlugField(unique=True)
    affects = models.CharField(max_length=500)
    requirements = models.CharField(max_length=500)


class Property(TranslatableModel):
    """
    Property -- property that character holds: cars, houses, etc.

    Attributes of class:
    name -- full name of the property (can be translated)
    description -- full description of the property (can be translated)
    type -- type like cars, houses, mobile phones, etc. (can be translated)
    short_name -- short name for referring in formulas
    cost -- cost of the property
    """
    translations = TranslatedFields(
        name=models.CharField(max_length=50),
        description=models.TextField(),
        type=models.CharField(max_length=30)
    )
    short_name = models.SlugField(unique=True)
    cost = models.PositiveIntegerField()


class University(TranslatableModel):
    """
    Universities where character can study in.

    Attributes of class:
    name -- full name of the university (can be translated)
    description -- full description of the university (can be translated)
    short_name -- short name for referring in formulas
    affects -- what parameters this action affects
    requirements -- what requirements this action has
    """
    translations = TranslatedFields(
        name=models.CharField(max_length=50),
        description=models.TextField()
    )
    short_name = models.SlugField(unique=True)
    affects = models.CharField(max_length=500)
    requirements = models.CharField(max_length=500)


class Project(TranslatableModel):
    """
    Projects where character can be involved. Name can be specified by user.

    Attributes of class:
    description -- full description of the project (can be translated)
    type -- type like freelance, open source, startup, etc. (can be translated)
    short_name -- short name for referring in formulas
    affects -- what parameters this action affects
    requirements -- what requirements this action has
    time_spending -- number of game days that project requires to be spent for ending the project (can be skipped)
    """
    translations = TranslatedFields(
        description=models.TextField(),
        type=models.CharField(max_length=30)
    )
    short_name = models.SlugField(unique=True)
    affects = models.CharField(max_length=500)
    requirements = models.CharField(max_length=500)
    time_spending = models.PositiveIntegerField(null=True, blank=True)


class Job(TranslatableModel):
    """
    Regular job for a character.

    Attributes of class:
    name -- full name of the job (can be translated)
    description -- full description of the job (can be translated)
    company_name -- company that offers this job
    short_name -- short name for referring in formulas
    affects -- what parameters this job affects
    requirements -- what requirements this job has
    """
    translations = TranslatedFields(
        name=models.CharField(max_length=50),
        description=models.TextField()
    )
    company_name = models.CharField(max_length=50)
    short_name = models.SlugField(unique=True)
    affects = models.CharField(max_length=500)
    requirements = models.CharField(max_length=500)


class Knowledge(TranslatableModel):
    """
    Character skills like Python programming and skill areas like backend programming.
    Knowledge relationships form oriented graph, where link from knowledge1 to knowledge2 means:
    'knowledge2' skill or area belongs to 'knowledge2' area.
    For example, Python skill belongs to 'backend languages' area, and 'backend languages' belongs to
    'backend programming' area, so there are link from 'backend programming' to 'backend languages'
    and from 'backend languages' to 'Python'.

    Simple skills (with no link to other knowledge instances) have level of knowledge (stored in userdata database).
    Area level of knowledge is calculated by taking the arithmetic mean of all knowledge levels in this area.
    There can be areas of type 'one-of' areas. Knowledge level for these areas is calculated by taking maximal
    level from knowledge instances in these areas.

    For example, 'backend languages' is 'one-of' area. If it consists of 'Python' (80% level), 'PHP' (0% level),
    'Ruby' (15% level) and Java (60% level), 'backend languages' level is 80% (as the maximum level in it is 80%).

    Attributes of class:
    name -- full name of the knowledge (can be translated)
    description -- full description of the knowledge (can be translated)
    type -- skill, area or one-from-area
    short_name -- short name for referring in formulas
    requirements -- what requirements this knowledge has (knowledge can't be above neither of the required skills level)
    edges -- creating table with edges of oriented knowledge graph
    """
    translations = TranslatedFields(
        name=models.CharField(max_length=50),
        description=models.TextField(),
        type=models.CharField(max_length=30)
    )
    short_name = models.SlugField(unique=True)
    requirements = models.CharField(max_length=500)
    edges = models.ManyToManyField('self', symmetrical=False)
