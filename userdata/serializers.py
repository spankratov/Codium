from rest_framework import serializers, validators
from rest_framework.compat import unicode_to_repr
from content.models import Property, University, Project, Job, Knowledge
from django.contrib.auth.models import User
from userdata.models import Character, AttributeLevels, CharacterProperties, CharacterUniversities, CharacterProjects, \
    CharacterJobs, KnowledgeLevels
from userdata.validators import LevelFromMinToMax, NotBiggerThanCharacterDaysLived, \
    from_zero_to_hundred


class CurrentCharacterDaysLivedDefault(object):
    days_lived = 0

    def set_context(self, serializer_field):
        instance = getattr(serializer_field.parent, 'instance', None)
        request = serializer_field.context['request']
        if 'character_id' in request.data:
            self.days_lived = Character.objects.get(id=int(request.data['character_id'])).days_lived
        elif instance is not None:
            self.days_lived = instance.character.days_lived
        else:
            self.days_lived = 0

    def __call__(self):
        return self.days_lived

    def __repr__(self):
        return unicode_to_repr('%s()' % self.__class__.__name__)

    def to_json(self):
        return ""


class UserSerializer(serializers.ModelSerializer):
    character = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'character')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class CharacterSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Character
        fields = ('id', 'days_lived', 'seconds_in_current_day', 'last_update', 'user')


class AttributeLevelsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='attribute.id', read_only=True)
    name = serializers.CharField(max_length=50, source='attribute.name', read_only=True)
    short_name = serializers.SlugField(source='attribute.short_name', read_only=True)
    default = serializers.IntegerField(source='attribute.default', read_only=True)
    min_value = serializers.IntegerField(source='attribute.min_value', read_only=True)
    max_value = serializers.IntegerField(source='attribute.max_value', read_only=True)
    level = serializers.IntegerField(validators=[LevelFromMinToMax()])

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
    purchase_date = serializers.IntegerField(default=CurrentCharacterDaysLivedDefault(),
                                             validators=[NotBiggerThanCharacterDaysLived()])

    class Meta:
        model = CharacterProperties
        fields = (
            'character_id', 'property', 'id', 'name', 'description', 'type', 'short_name', 'cost', 'purchase_date')
        validators = [
            validators.UniqueTogetherValidator(
                    queryset=CharacterProperties.objects.all(),
                    fields=('character', 'property')
            )
        ]


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
    entering_date = serializers.IntegerField(default=CurrentCharacterDaysLivedDefault(),
                                             validators=[NotBiggerThanCharacterDaysLived()])
    finished = serializers.BooleanField(default=False)

    class Meta:
        model = CharacterUniversities
        fields = (
            'character_id', 'university', 'id', 'name', 'description', 'short_name', 'affects', 'requirements',
            'entering_date', 'finished')
        validators = [
            validators.UniqueTogetherValidator(
                    queryset=CharacterUniversities.objects.all(),
                    fields=('character', 'university')
            )
        ]


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
    taking_date = serializers.IntegerField(default=CurrentCharacterDaysLivedDefault(),
                                           validators=[NotBiggerThanCharacterDaysLived()])
    finished = serializers.BooleanField(default=False)

    class Meta:
        model = CharacterProjects
        fields = (
            'character_id', 'project', 'id', 'name', 'description', 'type', 'short_name', 'affects', 'requirements',
            'time_spending', 'taking_date', 'finished')
        validators = [
            validators.UniqueTogetherValidator(
                    queryset=CharacterProjects.objects.all(),
                    fields=('character', 'project')
            )
        ]


class CharacterJobsSerializer(serializers.ModelSerializer):
    character_id = serializers.PrimaryKeyRelatedField(source='character', write_only=True,
                                                      queryset=Character.objects.all())
    job = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Job.objects.all())
    id = serializers.IntegerField(source='job.id', read_only=True)
    name = serializers.CharField(max_length=50, source='job.name', read_only=True)
    description = serializers.CharField(source='job.description', read_only=True)
    company_name = serializers.CharField(max_length=50, source='job.company_name', read_only=True)
    short_name = serializers.SlugField(source='job.short_name', read_only=True)
    affects = serializers.CharField(max_length=500, source='job.affects', read_only=True)
    requirements = serializers.CharField(max_length=500, source='job.requirements', read_only=True)
    taking_date = serializers.IntegerField(default=CurrentCharacterDaysLivedDefault(),
                                           validators=[NotBiggerThanCharacterDaysLived()])
    finished = serializers.BooleanField(default=False)

    class Meta:
        model = CharacterJobs
        fields = (
            'character_id', 'job', 'id', 'name', 'description', 'company_name', 'short_name', 'affects', 'requirements',
            'taking_date', 'finished')
        validators = [
            validators.UniqueTogetherValidator(
                    queryset=CharacterJobs.objects.all(),
                    fields=('character', 'job')
            )
        ]


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
    level = serializers.IntegerField(default=0, validators=[from_zero_to_hundred])

    class Meta:
        model = KnowledgeLevels
        fields = (
            'id', 'name', 'description', 'type', 'short_name', 'requirements', 'parents', 'children', 'level')
