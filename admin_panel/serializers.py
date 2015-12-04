from rest_framework import serializers, validators
from hvad.contrib.restframework import TranslatableModelSerializer
from content.models import Attribute, Event, Action, Property, University, Project, Job, Knowledge
from django.contrib.auth.models import User
from userdata.models import Character, AttributeLevels, KnowledgeLevels


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
    character = serializers.PrimaryKeyRelatedField(queryset=Character.objects.all())

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
