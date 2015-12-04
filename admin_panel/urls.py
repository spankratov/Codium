from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from admin_panel import views

router = DefaultRouter()
router.register(r'attributes', views.AttributeViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'actions', views.ActionViewSet)
router.register(r'properties', views.PropertyViewSet)
router.register(r'universities', views.UniversityViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'jobs', views.JobViewSet)
router.register(r'knowledges', views.KnowledgeViewSet)
router.register(r'characters', views.CharacterViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       url(r'^auth/login/?$', 'rest_framework_jwt.views.obtain_jwt_token'))
