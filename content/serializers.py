from rest_framework import serializers, validators
from hvad.contrib.restframework import TranslatableModelSerializer
from content.models import Attribute, Event, Action, Property, University, Project, Job, Knowledge
from content.validators import DefaultFromMinToMax, from_zero_to_hundred


class AttributeSerializer(TranslatableModelSerializer):
    short_name = serializers.SlugField(validators=[validators.UniqueValidator(queryset=Attribute.objects.all())])
    default = serializers.IntegerField(validators=[DefaultFromMinToMax()])

    class Meta:
        model = Attribute
        fields = ('id', 'name', 'short_name', 'default', 'min_value', 'max_value', 'language_code')


class EventSerializer(TranslatableModelSerializer):
    short_name = serializers.SlugField(validators=[validators.UniqueValidator(queryset=Event.objects.all())])
    chance = serializers.FloatField(validators=[from_zero_to_hundred])

    class Meta:
        model = Event
        fields = (
            'id', 'name', 'description', 'short_name', 'affects', 'requirements', 'chance', 'language_code')


class ActionSerializer(TranslatableModelSerializer):
    short_name = serializers.SlugField(validators=[validators.UniqueValidator(queryset=Action.objects.all())])

    class Meta:
        model = Action
        fields = (
            'id', 'name', 'description', 'type', 'short_name', 'affects', 'requirements', 'language_code')


class PropertySerializer(TranslatableModelSerializer):
    short_name = serializers.SlugField(validators=[validators.UniqueValidator(queryset=Property.objects.all())])

    class Meta:
        model = Property
        fields = (
            'id', 'name', 'description', 'type', 'short_name', 'cost', 'language_code')


class UniversitySerializer(TranslatableModelSerializer):
    short_name = serializers.SlugField(validators=[validators.UniqueValidator(queryset=University.objects.all())])

    class Meta:
        model = University
        fields = (
            'id', 'name', 'description', 'short_name', 'affects', 'requirements', 'language_code')


class ProjectSerializer(TranslatableModelSerializer):
    short_name = serializers.SlugField(validators=[validators.UniqueValidator(queryset=Project.objects.all())])

    class Meta:
        model = Project
        fields = (
            'id', 'description', 'type', 'short_name', 'affects', 'requirements', 'time_spending',
            'language_code')


class JobSerializer(TranslatableModelSerializer):
    short_name = serializers.SlugField(validators=[validators.UniqueValidator(queryset=Job.objects.all())])

    class Meta:
        model = Job
        fields = (
            'id', 'name', 'description', 'company_name', 'short_name', 'affects', 'requirements',
            'language_code')


class KnowledgeSerializer(TranslatableModelSerializer):
    short_name = serializers.SlugField(validators=[validators.UniqueValidator(queryset=Knowledge.objects.all())])
    parents = serializers.PrimaryKeyRelatedField(many=True, queryset=Knowledge.objects.all(), allow_null=True)
    children = serializers.PrimaryKeyRelatedField(many=True, queryset=Knowledge.objects.all(), allow_null=True)

    class Meta:
        model = Knowledge
        fields = ('id', 'name', 'description', 'type', 'short_name', 'requirements', 'parents', 'children')
