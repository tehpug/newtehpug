from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from members import views

router = DefaultRouter()
router.register(r'member', views.MemberViewSet)
router.register(r'links', views.SocialLinkViewSet)
router.register(r'site', views.SocialSiteViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
