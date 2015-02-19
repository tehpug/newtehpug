from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from projects import views

router = DefaultRouter()
router.register(r'licenses', views.LicenseViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'technologies', views.TechnologyViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
