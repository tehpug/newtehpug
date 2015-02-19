from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from slideshows import views

router = DefaultRouter()
router.register(r'slideshows', views.SlideshowViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
