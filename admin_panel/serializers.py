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
    id = serializers.IntegerField(source='property.id', read_only=True)
    name = serializers.CharField(max_length=50, source='property.name', read_only=True)
    description = serializers.CharField(source='property.description', read_only=True)
    type = serializers.CharField(max_length=30, source='property.type', read_only=True)
    short_name = serializers.SlugField(source='property.short_name', read_only=True)
    cost = serializers.IntegerField(source='property.cost', read_only=True)
    purchase_date=serializers.IntegerField(default=CurrentCharacterDaysLivedDefault)

    class Meta:
        model = CharacterProperties
        fields = ('id', 'name', 'description', 'type', 'short_name', 'cost', 'purchase_date')

    def to_internal_value(self, data):
        validated_data = super(CharacterPropertiesSerializer, self).to_internal_value(data)
        if not self.partial:
            character_id = data.get('character_id')
            if not character_id:
                raise ValidationError({
                    'character_id': 'This field is required.'
                })
            character_id = int(character_id)
            validated_data['character'] = Character.objects.get(id=character_id)
            property_id = data.get('property')
            if not property_id:
                raise ValidationError({
                    'property': 'This field is required.'
                })
            property_id = int(property_id)
            validated_data['property'] = Property.objects.get(id=property_id)
        return validated_data


class CharacterUniversitiesSerializer(serializers.ModelSerializer):
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
        fields = ('id', 'name', 'description', 'short_name', 'affects', 'requirements', 'entering_date', 'finished')

    def to_internal_value(self, data):
        validated_data = super(CharacterUniversitiesSerializer, self).to_internal_value(data)
        if not self.partial:
            character_id = data.get('character_id')
            if not character_id:
                raise ValidationError({
                    'character_id': 'This field is required.'
                })
            character_id = int(character_id)
            validated_data['character'] = Character.objects.get(id=character_id)
            university_id = data.get('university')
            if not university_id:
                raise ValidationError({
                    'university': 'This field is required.'
                })
            university_id = int(university_id)
            validated_data['university'] = University.objects.get(id=university_id)
        return validated_data
