from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from pug_sessions import views

router = DefaultRouter()
router.register(r'places', views.PlaceViewSet)
router.register(r'sessions', views.SessionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
