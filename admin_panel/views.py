# coding=utf-8
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from admin_panel.serializers import AttributeSerializer, EventSerializer, ActionSerializer, PropertySerializer, \
    UniversitySerializer, ProjectSerializer, JobSerializer, CharacterSerializer, UserSerializer
from userdata.models import Character
from content.models import Attribute, Event, Action, Property, University, Project, Job


class AttributeViewSet(viewsets.ModelViewSet):
    """ Сущность  \"Атрибут\" """
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def list(self, request, *args, **kwargs):
        """
        Список всех атрибутов.
        """
        super(AttributeViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Создать атрибут.
        """
        super(AttributeViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Получить атрибут.
        """
        super(AttributeViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Полностью обновить атрибут.
        """
        super(AttributeViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Частично обновить атрибут.
        """
        super(AttributeViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Удалить атрибут.
        """
        super(AttributeViewSet, self).destroy(request, *args, **kwargs)


class EventViewSet(viewsets.ModelViewSet):
    """ Сущность  \"Событие\" """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def list(self, request, *args, **kwargs):
        """
        Список всех событий.
        """
        super(EventViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Создать событие.
        """
        super(EventViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Получить событие.
        """
        super(EventViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Полностью обновить событие.
        """
        super(EventViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Частично обновить событие.
        """
        super(EventViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Удалить событие.
        """
        super(EventViewSet, self).destroy(request, *args, **kwargs)


class ActionViewSet(viewsets.ModelViewSet):
    """ Сущность  \"Действие\" """
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def list(self, request, *args, **kwargs):
        """
        Список всех действий.
        """
        super(ActionViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Создать действие.
        """
        super(ActionViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Получить действие.
        """
        super(ActionViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Полностью обновить действие.
        """
        super(ActionViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Частично обновить действие.
        """
        super(ActionViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Удалить действие.
        """
        super(ActionViewSet, self).destroy(request, *args, **kwargs)


class PropertyViewSet(viewsets.ModelViewSet):
    """ Сущность  \"Собственность\" """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def list(self, request, *args, **kwargs):
        """
        Список всей собственности.
        """
        super(PropertyViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Создать собственность.
        """
        super(PropertyViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Получить собственность.
        """
        super(PropertyViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Полностью обновить собственность.
        """
        super(PropertyViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Частично обновить собственность.
        """
        super(PropertyViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Удалить собственность.
        """
        super(PropertyViewSet, self).destroy(request, *args, **kwargs)


class UniversityViewSet(viewsets.ModelViewSet):
    """ Сущность  \"Университет\" """
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def list(self, request, *args, **kwargs):
        """
        Список всех университетов.
        """
        super(UniversityViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Создать университет.
        """
        super(UniversityViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Получить университет.
        """
        super(UniversityViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Полностью обновить университет.
        """
        super(UniversityViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Частично обновить университет.
        """
        super(UniversityViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Удалить университет.
        """
        super(UniversityViewSet, self).destroy(request, *args, **kwargs)


class ProjectViewSet(viewsets.ModelViewSet):
    """ Сущность  \"Проект\" """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def list(self, request, *args, **kwargs):
        """
        Список всех проектов.
        """
        super(ProjectViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Создать проект.
        """
        super(ProjectViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Получить проект.
        """
        super(ProjectViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Полностью обновить проект.
        """
        super(ProjectViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Частично обновить проект.
        """
        super(ProjectViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Удалить проект.
        """
        super(ProjectViewSet, self).destroy(request, *args, **kwargs)


class JobViewSet(viewsets.ModelViewSet):
    """ Сущность  \"Работа\" """
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def list(self, request, *args, **kwargs):
        """
        Список всех работ.
        """
        super(JobViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Создать работу.
        """
        super(JobViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Получить работу.
        """
        super(JobViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Полностью обновить работу.
        """
        super(JobViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Частично обновить работу.
        """
        super(JobViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Удалить работу.
        """
        super(JobViewSet, self).destroy(request, *args, **kwargs)


class CharacterViewSet(viewsets.ModelViewSet):
    """ Сущность  \"Персонаж\" """
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)


class UserViewSet(viewsets.ModelViewSet):
    """ Сущность  \"Пользователь\" """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def list(self, request, *args, **kwargs):
        """
        Список всех пользователей.
        """
        super(UserViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Создать пользователя.
        """
        super(UserViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Получить пользователя.
        """
        super(UserViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Полностью обновить пользователя.
        """
        super(UserViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Частично обновить пользователя.
        """
        super(UserViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Удалить пользователя.
        """
        super(UserViewSet, self).destroy(request, *args, **kwargs)
