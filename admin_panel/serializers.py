from rest_framework import serializers
from hvad.contrib.restframework import HyperlinkedTranslatableModelSerializer
from content.models import Attribute, Event, Action, Property, University, Project, Job
from django.contrib.auth.models import User
from userdata.models import Character


class AttributeSerializer(HyperlinkedTranslatableModelSerializer):
    class Meta:
        model = Attribute
        fields = ('url', 'id', 'name', 'short_name', 'min_value', 'max_value', 'language_code')


class EventSerializer(HyperlinkedTranslatableModelSerializer):
    class Meta:
        model = Event
        fields = (
            'url', 'id', 'name', 'description', 'short_name', 'affects', 'requirements', 'chance', 'language_code')


class ActionSerializer(HyperlinkedTranslatableModelSerializer):
    class Meta:
        model = Action
        fields = (
            'url', 'id', 'name', 'description', 'type,' 'short_name', 'affects', 'requirements', 'language_code')


class PropertySerializer(HyperlinkedTranslatableModelSerializer):
    class Meta:
        model = Property
        fields = (
            'url', 'id', 'name', 'description', 'type,' 'short_name', 'cost', 'language_code')


class UniversitySerializer(HyperlinkedTranslatableModelSerializer):
    class Meta:
        model = University
        fields = (
            'url', 'id', 'name', 'description', 'short_name', 'cost', 'affects', 'requirements', 'language_code')


class ProjectSerializer(HyperlinkedTranslatableModelSerializer):
    class Meta:
        model = Project
        fields = (
            'url', 'id', 'description', 'type', 'short_name', 'affects', 'requirements', 'time_spending',
            'language_code')


class JobSerializer(HyperlinkedTranslatableModelSerializer):
    class Meta:
        model = Job
        fields = (
            'url', 'id', 'name', 'description', 'company_name', 'short_name', 'affects', 'requirements',
            'language_code')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    character = serializers.HyperlinkedRelatedField(queryset=Character.objects.all(), view_name='character-detail')

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'character')


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(queryset=User.objects.all(), view_name='user-detail')

    class Meta:
        model = Character
        fields = ('url', 'id', 'days_lived', 'seconds_in_current_day', 'last_update', 'user')
