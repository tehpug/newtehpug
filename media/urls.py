from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from media import views

router = DefaultRouter()
router.register(r'audios', views.AudioViewSet)
router.register(r'images', views.ImageViewSet)
router.register(r'presentations', views.PresentationViewSet)
router.register(r'videos', views.VideoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
