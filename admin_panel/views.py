# coding=utf-8
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import mixins
from admin_panel.serializers import AttributeSerializer, EventSerializer, ActionSerializer, PropertySerializer, \
    UniversitySerializer, ProjectSerializer, JobSerializer, KnowledgeSerializer, CharacterSerializer, UserSerializer, \
    AttributeLevelsSerializer
from userdata.models import Character, AttributeLevels, CharacterJobs, CharacterProjects, CharacterProperties, \
    CharacterUniversities, KnowledgeLevels
from content.models import Attribute, Event, Action, Property, University, Project, Job, Knowledge


class AttributeViewSet(viewsets.ModelViewSet):
    """ Сущность  \"Атрибут\" """
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def list(self, request, *args, **kwargs):
        """
        Список всех атрибутов.
        """
        return super(AttributeViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Создать атрибут.
        """
        return super(AttributeViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Получить атрибут.
        """
        return super(AttributeViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Полностью обновить атрибут.
        """
        return super(AttributeViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Частично обновить атрибут.
        """
        return super(AttributeViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Удалить атрибут.
        """
        return super(AttributeViewSet, self).destroy(request, *args, **kwargs)

    def perform_destroy(self, instance):
        AttributeLevels.objects.filter(attribute=instance).delete()
        super(AttributeViewSet, self).perform_destroy(instance)


class EventViewSet(viewsets.ModelViewSet):
    """ Сущность  \"Событие\" """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def list(self, request, *args, **kwargs):
        """
        Список всех событий.
        """
        return super(EventViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Создать событие.
        """
        return super(EventViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Получить событие.
        """
        return super(EventViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Полностью обновить событие.
        """
        return super(EventViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Частично обновить событие.
        """
        return super(EventViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Удалить событие.
        """
        return super(EventViewSet, self).destroy(request, *args, **kwargs)


class ActionViewSet(viewsets.ModelViewSet):
    """ Сущность  \"Действие\" """
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def list(self, request, *args, **kwargs):
        """
        Список всех действий.
        """
        return super(ActionViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Создать действие.
        """
        return super(ActionViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Получить действие.
        """
        return super(ActionViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Полностью обновить действие.
        """
        return super(ActionViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Частично обновить действие.
        """
        return super(ActionViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Удалить действие.
        """
        return super(ActionViewSet, self).destroy(request, *args, **kwargs)


class PropertyViewSet(viewsets.ModelViewSet):
    """ Сущность  \"Собственность\" """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def list(self, request, *args, **kwargs):
        """
        Список всей собственности.
        """
        return super(PropertyViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Создать собственность.
        """
        return super(PropertyViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Получить собственность.
        """
        return super(PropertyViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Полностью обновить собственность.
        """
        return super(PropertyViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Частично обновить собственность.
        """
        return super(PropertyViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Удалить собственность.
        """
        return super(PropertyViewSet, self).destroy(request, *args, **kwargs)

    def perform_destroy(self, instance):
        CharacterProperties.objects.filter(property=instance).delete()
        super(PropertyViewSet, self).perform_destroy(instance)


class UniversityViewSet(viewsets.ModelViewSet):
    """ Сущность  \"Университет\" """
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def list(self, request, *args, **kwargs):
        """
        Список всех университетов.
        """
        return super(UniversityViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Создать университет.
        """
        return super(UniversityViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Получить университет.
        """
        return super(UniversityViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Полностью обновить университет.
        """
        return super(UniversityViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Частично обновить университет.
        """
        return super(UniversityViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Удалить университет.
        """
        return super(UniversityViewSet, self).destroy(request, *args, **kwargs)

    def perform_destroy(self, instance):
        CharacterUniversities.objects.filter(university=instance).delete()
        super(UniversityViewSet, self).perform_destroy(instance)


class ProjectViewSet(viewsets.ModelViewSet):
    """ Сущность  \"Проект\" """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def list(self, request, *args, **kwargs):
        """
        Список всех проектов.
        """
        return super(ProjectViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Создать проект.
        """
        return super(ProjectViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Получить проект.
        """
        return super(ProjectViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Полностью обновить проект.
        """
        return super(ProjectViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Частично обновить проект.
        """
        return super(ProjectViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Удалить проект.
        """
        return super(ProjectViewSet, self).destroy(request, *args, **kwargs)

    def perform_destroy(self, instance):
        CharacterProjects.objects.filter(project=instance).delete()
        super(ProjectViewSet, self).perform_destroy(instance)


class JobViewSet(viewsets.ModelViewSet):
    """ Сущность  \"Работа\" """
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def list(self, request, *args, **kwargs):
        """
        Список всех работ.
        """
        return super(JobViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Создать работу.
        """
        return super(JobViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Получить работу.
        """
        return super(JobViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Полностью обновить работу.
        """
        return super(JobViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Частично обновить работу.
        """
        return super(JobViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Удалить работу.
        """
        return super(JobViewSet, self).destroy(request, *args, **kwargs)

    def perform_destroy(self, instance):
        CharacterJobs.objects.filter(job=instance).delete()
        super(JobViewSet, self).perform_destroy(instance)


class KnowledgeViewSet(viewsets.ModelViewSet):
    """ Сущность  \"Навык\" """
    queryset = Knowledge.objects.all()
    serializer_class = KnowledgeSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def list(self, request, *args, **kwargs):
        """
        Список всех навыков.
        """
        return super(KnowledgeViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Создать навык.
        """
        return super(KnowledgeViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Получить навык.
        """
        return super(KnowledgeViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Полностью обновить навык.
        """
        return super(KnowledgeViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Частично обновить навык.
        """
        return super(KnowledgeViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Удалить навык.
        """
        return super(KnowledgeViewSet, self).destroy(request, *args, **kwargs)

    def perform_destroy(self, instance):
        KnowledgeLevels.objects.filter(knowledge=instance).delete()
        super(KnowledgeViewSet, self).perform_destroy(instance)


class CharacterViewSet(viewsets.ModelViewSet):
    """ Сущность  \"Персонаж\" """
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def list(self, request, *args, **kwargs):
        """
        Список всех персонажей.
        """
        return super(CharacterViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Создать персонажа.
        """
        return super(CharacterViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Получить персонажа.
        """
        return super(CharacterViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Полностью обновить персонажа.
        """
        return super(CharacterViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Частично обновить персонажа.
        """
        return super(CharacterViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Удалить персонажа.
        """
        return super(CharacterViewSet, self).destroy(request, *args, **kwargs)

    def perform_destroy(self, instance):
        AttributeLevels.objects.filter(character=instance).delete()
        CharacterJobs.objects.filter(character=instance).delete()
        CharacterProjects.objects.filter(character=instance).delete()
        CharacterProperties.objects.filter(character=instance).delete()
        CharacterUniversities.objects.filter(character=instance).delete()
        KnowledgeLevels.objects.filter(character=instance).delete()
        super(CharacterViewSet, self).perform_destroy(instance)


class UserViewSet(viewsets.ModelViewSet):
    """ Сущность  \"Пользователь\" """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def list(self, request, *args, **kwargs):
        """
        Список всех пользователей.
        """
        return super(UserViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Создать пользователя.
        """
        return super(UserViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Получить пользователя.
        """
        return super(UserViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Полностью обновить пользователя.
        """
        return super(UserViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Частично обновить пользователя.
        """
        return super(UserViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Удалить пользователя.
        """
        return super(UserViewSet, self).destroy(request, *args, **kwargs)

    def perform_destroy(self, instance):
        character = instance.character
        AttributeLevels.objects.filter(character=character).delete()
        CharacterJobs.objects.filter(character=character).delete()
        CharacterProjects.objects.filter(character=character).delete()
        CharacterProperties.objects.filter(character=character).delete()
        CharacterUniversities.objects.filter(character=character).delete()
        KnowledgeLevels.objects.filter(character=character).delete()
        character.delete()
        super(UserViewSet, self).perform_destroy(instance)


class AttributeLevelsViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                             viewsets.GenericViewSet):
    """Атрибуты персонажа"""
    serializer_class = AttributeLevelsSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def get_queryset(self):
        return AttributeLevels.objects.filter(character__id=self.kwargs['character_id'])

    def get_object(self):
        return AttributeLevels.objects.get(character__id=self.kwargs['character_id'], attribute__id=self.kwargs['pk'])

    def list(self, request, *args, **kwargs):
        """
        Список всех атрибутов персонажа.
        """
        return super(AttributeLevelsViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Получить атрибут персонажа по id атрибута.
        """
        return super(AttributeLevelsViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Полностью обновить атрибут персонажа по id атрибута.
        """
        return super(AttributeLevelsViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Частично обновить атрибут персонажа по id атрибута.
        """
        return super(AttributeLevelsViewSet, self).partial_update(request, *args, **kwargs)
