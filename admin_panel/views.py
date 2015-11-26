from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from admin_panel.serializers import AttributeSerializer, EventSerializer, ActionSerializer, PropertySerializer, \
    UniversitySerializer, ProjectSerializer, JobSerializer, CharacterSerializer, UserSerializer
from userdata.models import Character
from content.models import Attribute, Event, Action, Property, University, Project, Job


class AttributeViewSet(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)
