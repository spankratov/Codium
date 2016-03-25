from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import mixins
from userdata.serializers import CharacterSerializer, UserSerializer, \
    AttributeLevelsSerializer, CharacterPropertiesSerializer, CharacterUniversitiesSerializer, \
    CharacterProjectsSerializer, CharacterJobsSerializer, KnowledgeLevelsSerializer
from userdata.models import Character, AttributeLevels, CharacterJobs, CharacterProjects, CharacterProperties, \
    CharacterUniversities, KnowledgeLevels


class CharacterViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):
    """ Сущность  \"Персонаж\" """
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def list(self, request, *args, **kwargs):
        """
        Список всех персонажей.
        """
        return super(CharacterViewSet, self).list(request, *args, **kwargs)

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


class UserViewSet(viewsets.ModelViewSet):
    """ Сущность  \"Пользователь\" """
    queryset = User.objects.filter(is_staff=False)
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
        Частично обновить атрибут персонажа по id атрибута.
        """
        kwargs['partial'] = True
        return super(AttributeLevelsViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Частично обновить атрибут персонажа по id атрибута.
        """
        return super(AttributeLevelsViewSet, self).partial_update(request, *args, **kwargs)


class CharacterPropertiesViewSet(viewsets.ModelViewSet):
    """Собственность персонажа"""
    serializer_class = CharacterPropertiesSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def get_queryset(self):
        return CharacterProperties.objects.filter(character__id=self.kwargs['character_id'])

    def get_object(self):
        return CharacterProperties.objects.get(character__id=self.kwargs['character_id'],
                                               property__id=self.kwargs['pk'])

    def list(self, request, *args, **kwargs):
        """
        Список всей собственности персонажа.
        """
        return super(CharacterPropertiesViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Присвоить собственность персонажу

        ---
        parameters:
            - name: character_id
              required: true
              type: string
              paramType: path
        """
        request.data['character_id'] = self.kwargs['character_id']
        return super(CharacterPropertiesViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Получить собственность персонажа по id собственности.
        """
        return super(CharacterPropertiesViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Полностью обновить собственность персонажа по id собственности.

        ---
        parameters:
            - name: character_id
              required: true
              type: string
              paramType: path
        """
        request.data['character_id'] = self.kwargs['character_id']
        return super(CharacterPropertiesViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Частично обновить собственность персонажа по id атрибута.

        ---
        parameters:
            - name: character_id
              required: true
              type: string
              paramType: path
        """
        return super(CharacterPropertiesViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Удалить собственность у персонажа.
        """
        return super(CharacterPropertiesViewSet, self).destroy(request, *args, **kwargs)


class CharacterUniversitiesViewSet(viewsets.ModelViewSet):
    """Университеты персонажа"""
    serializer_class = CharacterUniversitiesSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def get_queryset(self):
        return CharacterUniversities.objects.filter(character__id=self.kwargs['character_id'])

    def get_object(self):
        return CharacterUniversities.objects.get(character__id=self.kwargs['character_id'],
                                                 university__id=self.kwargs['pk'])

    def list(self, request, *args, **kwargs):
        """
        Список всех университетов персонажа.
        """
        return super(CharacterUniversitiesViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Присвоить университет персонажу.

        ---
        parameters:
            - name: character_id
              required: true
              type: string
              paramType: path
        """
        request.data['character_id'] = self.kwargs['character_id']
        return super(CharacterUniversitiesViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Получить университет персонажа по id университета.
        """
        return super(CharacterUniversitiesViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Полностью обновить университет персонажа по id университета.

        ---
        parameters:
            - name: character_id
              required: true
              type: string
              paramType: path
        """
        request.data['character_id'] = self.kwargs['character_id']
        return super(CharacterUniversitiesViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Частично обновить университет персонажа по id университета.

        ---
        parameters:
            - name: character_id
              required: true
              type: string
              paramType: path
        """
        return super(CharacterUniversitiesViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Удалить университет у персонажа.
        """
        return super(CharacterUniversitiesViewSet, self).destroy(request, *args, **kwargs)


class CharacterProjectsViewSet(viewsets.ModelViewSet):
    """Проекты персонажа"""
    serializer_class = CharacterProjectsSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def get_queryset(self):
        return CharacterProjects.objects.filter(character__id=self.kwargs['character_id'])

    def get_object(self):
        return CharacterProjects.objects.get(character__id=self.kwargs['character_id'], project__id=self.kwargs['pk'])

    def list(self, request, *args, **kwargs):
        """
        Список всех проектов персонажа.
        """
        return super(CharacterProjectsViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Присвоить проект персонажу.

        ---
        parameters:
            - name: character_id
              required: true
              type: string
              paramType: path
        """
        request.data['character_id'] = self.kwargs['character_id']
        return super(CharacterProjectsViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Получить проект персонажа по id проекта.
        """
        return super(CharacterProjectsViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Полностью обновить проект персонажа по id проекта.

        ---
        parameters:
            - name: character_id
              required: true
              type: string
              paramType: path
        """
        request.data['character_id'] = self.kwargs['character_id']
        return super(CharacterProjectsViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Частично обновить проект персонажа по id проекта.

        ---
        parameters:
            - name: character_id
              required: true
              type: string
              paramType: path
        """
        return super(CharacterProjectsViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Удалить проект у персонажа.
        """
        return super(CharacterProjectsViewSet, self).destroy(request, *args, **kwargs)


class CharacterJobsViewSet(viewsets.ModelViewSet):
    """Работа персонажа"""
    serializer_class = CharacterJobsSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def get_queryset(self):
        return CharacterJobs.objects.filter(character__id=self.kwargs['character_id'])

    def get_object(self):
        return CharacterJobs.objects.get(character__id=self.kwargs['character_id'], job__id=self.kwargs['pk'])

    def list(self, request, *args, **kwargs):
        """
        Список всех работ персонажа.
        """
        return super(CharacterJobsViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Присвоить работу персонажу.

        ---
        parameters:
            - name: character_id
              required: true
              type: string
              paramType: path
        """
        request.data['character_id'] = self.kwargs['character_id']
        return super(CharacterJobsViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Получить работу персонажа по id работы.
        """
        return super(CharacterJobsViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Полностью обновить работу персонажа по id работы.

        ---
        parameters:
            - name: character_id
              required: true
              type: string
              paramType: path
        """
        request.data['character_id'] = self.kwargs['character_id']
        return super(CharacterJobsViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Частично обновить работу персонажа по id работы.

        ---
        parameters:
            - name: character_id
              required: true
              type: string
              paramType: path
        """
        return super(CharacterJobsViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Удалить работу у персонажа.
        """
        return super(CharacterJobsViewSet, self).destroy(request, *args, **kwargs)


class KnowledgeLevelsViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                             viewsets.GenericViewSet):
    """Навыки персонажа"""
    serializer_class = KnowledgeLevelsSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def get_queryset(self):
        return KnowledgeLevels.objects.filter(character__id=self.kwargs['character_id'])

    def get_object(self):
        return KnowledgeLevels.objects.get(character__id=self.kwargs['character_id'], knowledge__id=self.kwargs['pk'])

    def list(self, request, *args, **kwargs):
        """
        Список всех навыков персонажа.
        """
        return super(KnowledgeLevelsViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Получить навык персонажа по id навыка.
        """
        return super(KnowledgeLevelsViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Частично обновить навык персонажа по id навыка.
        """
        kwargs['partial'] = True
        return super(KnowledgeLevelsViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Частично обновить навык персонажа по id навыка.
        """
        return super(KnowledgeLevelsViewSet, self).partial_update(request, *args, **kwargs)
