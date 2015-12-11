from django.core.exceptions import ValidationError
from rest_framework import serializers, validators
from rest_framework.compat import unicode_to_repr
from hvad.contrib.restframework import TranslatableModelSerializer
from content.models import Attribute, Event, Action, Property, University, Project, Job, Knowledge
from django.contrib.auth.models import User
from userdata.models import Character, AttributeLevels, CharacterProperties, CharacterUniversities, CharacterProjects, \
    CharacterJobs, KnowledgeLevels


class CurrentCharacterDaysLivedDefault(object):
    days_lived = 0

    def set_context(self, serializer_field):
        self.days_lived = serializer_field.context['request'].user.character.days_lived

    def __call__(self):
        return self.days_lived

    def __repr__(self):
        return unicode_to_repr('%s()' % self.__class__.__name__)

    def to_json(self):
        return ""


class AttributeSerializer(TranslatableModelSerializer):
    class Meta:
        model = Attribute
        fields = ('id', 'name', 'short_name', 'default', 'min_value', 'max_value', 'language_code')

    def create(self, validated_data):
        attribute = super(AttributeSerializer, self).create(validated_data)
        for character in Character.objects.all():
            AttributeLevels.objects.create(character=character, attribute=attribute, level=attribute.default)
        return attribute


class EventSerializer(TranslatableModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id', 'name', 'description', 'short_name', 'affects', 'requirements', 'chance', 'language_code')


class ActionSerializer(TranslatableModelSerializer):
    class Meta:
        model = Action
        fields = (
            'id', 'name', 'description', 'type', 'short_name', 'affects', 'requirements', 'language_code')


class PropertySerializer(TranslatableModelSerializer):
    class Meta:
        model = Property
        fields = (
            'id', 'name', 'description', 'type', 'short_name', 'cost', 'language_code')


class UniversitySerializer(TranslatableModelSerializer):
    class Meta:
        model = University
        fields = (
            'id', 'name', 'description', 'short_name', 'affects', 'requirements', 'language_code')


class ProjectSerializer(TranslatableModelSerializer):
    class Meta:
        model = Project
        fields = (
            'id', 'description', 'type', 'short_name', 'affects', 'requirements', 'time_spending',
            'language_code')


class JobSerializer(TranslatableModelSerializer):
    class Meta:
        model = Job
        fields = (
            'id', 'name', 'description', 'company_name', 'short_name', 'affects', 'requirements',
            'language_code')


class KnowledgeSerializer(TranslatableModelSerializer):
    parents = serializers.PrimaryKeyRelatedField(many=True, queryset=Knowledge.objects.all(), allow_null=True)
    children = serializers.PrimaryKeyRelatedField(many=True, queryset=Knowledge.objects.all(), allow_null=True)

    class Meta:
        model = Knowledge
        fields = ('id', 'name', 'description', 'type', 'short_name', 'requirements', 'parents', 'children')

    def create(self, validated_data):
        knowledge = super(KnowledgeSerializer, self).create(validated_data)
        for character in Character.objects.all():
            KnowledgeLevels.objects.create(character=character, knowledge=knowledge, level=0)
        return knowledge


class UserSerializer(serializers.ModelSerializer):
    character = serializers.PrimaryKeyRelatedField(queryset=Character.objects.all(), required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'character')


class CharacterSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Character
        fields = ('id', 'days_lived', 'seconds_in_current_day', 'last_update', 'user')

    def create(self, validated_data):
        character = super(CharacterSerializer, self).create(validated_data)
        for attribute in Attribute.objects.all():
            AttributeLevels.objects.create(character=character, attribute=attribute, level=attribute.default)
        for knowledge in Knowledge.objects.all():
            KnowledgeLevels.objects.create(character=character, knowledge=knowledge, level=0)
        return character


class AttributeLevelsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='attribute.id', read_only=True)
    name = serializers.CharField(max_length=50, source='attribute.name', read_only=True)
    short_name = serializers.SlugField(source='attribute.short_name', read_only=True)
    default = serializers.IntegerField(source='attribute.default', read_only=True)
    min_value = serializers.IntegerField(source='attribute.min_value', read_only=True)
    max_value = serializers.IntegerField(source='attribute.max_value', read_only=True)

    class Meta:
        model = AttributeLevels
        fields = ('id', 'name', 'short_name', 'default', 'min_value', 'max_value', 'level')


class CharacterPropertiesSerializer(serializers.ModelSerializer):
    character_id = serializers.PrimaryKeyRelatedField(source='character', write_only=True,
                                                      queryset=Character.objects.all())
    property = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Property.objects.all())
    id = serializers.IntegerField(source='property.id', read_only=True)
    name = serializers.CharField(max_length=50, source='property.name', read_only=True)
    description = serializers.CharField(source='property.description', read_only=True)
    type = serializers.CharField(max_length=30, source='property.type', read_only=True)
    short_name = serializers.SlugField(source='property.short_name', read_only=True)
    cost = serializers.IntegerField(source='property.cost', read_only=True)
    purchase_date = serializers.IntegerField(default=CurrentCharacterDaysLivedDefault)

    class Meta:
        model = CharacterProperties
        fields = ('character_id', 'property', 'id', 'name', 'description', 'type', 'short_name', 'cost', 'purchase_date')


class CharacterUniversitiesSerializer(serializers.ModelSerializer):
    character_id = serializers.PrimaryKeyRelatedField(source='character', write_only=True,
                                                      queryset=Character.objects.all())
    university = serializers.PrimaryKeyRelatedField(write_only=True, queryset=University.objects.all())
    id = serializers.IntegerField(source='university.id', read_only=True)
    name = serializers.CharField(max_length=50, source='university.name', read_only=True)
    description = serializers.CharField(source='university.description', read_only=True)
    short_name = serializers.SlugField(source='university.short_name', read_only=True)
    affects = serializers.CharField(max_length=500, source='university.affects', read_only=True)
    requirements = serializers.CharField(max_length=500, source='university.requirements', read_only=True)
    entering_date = serializers.IntegerField(default=CurrentCharacterDaysLivedDefault())
    finished = serializers.BooleanField(default=False)

    class Meta:
        model = CharacterUniversities
        fields = (
            'character_id', 'university', 'id', 'name', 'description', 'short_name', 'affects', 'requirements',
            'entering_date', 'finished')


class CharacterProjectsSerializer(serializers.ModelSerializer):
    character_id = serializers.PrimaryKeyRelatedField(source='character', write_only=True,
                                                      queryset=Character.objects.all())
    project = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Project.objects.all())
    id = serializers.IntegerField(source='project.id', read_only=True)
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(source='project.description', read_only=True)
    type = serializers.CharField(max_length=30, source='project.type', read_only=True)
    short_name = serializers.SlugField(source='project.short_name', read_only=True)
    affects = serializers.CharField(max_length=500, source='project.affects', read_only=True)
    requirements = serializers.CharField(max_length=500, source='project.requirements', read_only=True)
    time_spending = serializers.IntegerField(source='project.time_spending', read_only=True)
    taking_date = serializers.IntegerField(default=CurrentCharacterDaysLivedDefault())
    finished = serializers.BooleanField(default=False)

    class Meta:
        model = CharacterProjects
        fields = (
            'character_id', 'project', 'id', 'name', 'description', 'type', 'short_name', 'affects', 'requirements',
            'time_spending', 'taking_date', 'finished')


class CharacterJobsSerializer(serializers.ModelSerializer):
    character_id = serializers.PrimaryKeyRelatedField(source='character', write_only=True,
                                                      queryset=Character.objects.all())
    job = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Job.objects.all())
    # id = serializers.IntegerField(source='job.id', read_only=True)
    name = serializers.CharField(max_length=50, source='job.name', read_only=True)
    description = serializers.CharField(source='job.description', read_only=True)
    company_name = serializers.CharField(max_length=50, source='job.company_name', read_only=True)
    short_name = serializers.SlugField(source='job.short_name', read_only=True)
    affects = serializers.CharField(max_length=500, source='job.affects', read_only=True)
    requirements = serializers.CharField(max_length=500, source='job.requirements', read_only=True)
    taking_date = serializers.IntegerField(default=CurrentCharacterDaysLivedDefault())
    finished = serializers.BooleanField(default=False)

    class Meta:
        model = CharacterJobs
        fields = (
            'character_id', 'job', 'id', 'name', 'description', 'company_name', 'short_name', 'affects', 'requirements',
            'taking_date', 'finished')


class KnowledgeLevelsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='knowledge.id', read_only=True)
    name = serializers.CharField(max_length=50, source='knowledge.name', read_only=True)
    description = serializers.CharField(source='knowledge.description', read_only=True)
    type = serializers.CharField(max_length=30, source='knowledge.type', read_only=True)
    short_name = serializers.SlugField(source='knowledge.short_name', read_only=True)
    requirements = serializers.CharField(max_length=500, source='knowledge.requirements', read_only=True)
    parents = serializers.PrimaryKeyRelatedField(source='knowledge.parents', many=True,
                                                 queryset=Knowledge.objects.all(), allow_null=True)
    children = serializers.PrimaryKeyRelatedField(source='knowledge.children', many=True,
                                                  queryset=Knowledge.objects.all(), allow_null=True)
    level = serializers.IntegerField(default=0)

    class Meta:
        model = KnowledgeLevels
        fields = (
            'id', 'name', 'description', 'type', 'short_name', 'requirements', 'parents', 'children', 'level')
