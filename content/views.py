from rest_framework import viewsets
from rest_framework import permissions
from content.serializers import AttributeSerializer, EventSerializer, ActionSerializer, PropertySerializer, \
    UniversitySerializer, ProjectSerializer, JobSerializer, KnowledgeSerializer
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
