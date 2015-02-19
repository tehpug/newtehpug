from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from faq import views

router = DefaultRouter()
router.register(r'faqs', views.FAQViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
