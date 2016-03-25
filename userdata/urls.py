from django.conf.urls import patterns, url, include, handler404
from rest_framework.routers import DefaultRouter
from userdata import views

router = DefaultRouter()
router.register(r'characters', views.CharacterViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'characters/(?P<character_id>[0-9]+)/attributes', views.AttributeLevelsViewSet,
                base_name='attributelevels')
router.register(r'characters/(?P<character_id>[0-9]+)/properties', views.CharacterPropertiesViewSet,
                base_name='characterproperties')
router.register(r'characters/(?P<character_id>[0-9]+)/universities', views.CharacterUniversitiesViewSet,
                base_name='characteruniversities')
router.register(r'characters/(?P<character_id>[0-9]+)/projects', views.CharacterProjectsViewSet,
                base_name='characterprojects')
router.register(r'characters/(?P<character_id>[0-9]+)/jobs', views.CharacterJobsViewSet,
                base_name='characterjobs')
router.register(r'characters/(?P<character_id>[0-9]+)/knowledges', views.KnowledgeLevelsViewSet,
                base_name='knowledgelevels')

urlpatterns = patterns('', url(r'^', include(router.urls)))
