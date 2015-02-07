from django.conf.urls import patterns, url

from faq import views


urlpatterns = patterns(
    '',
    url(r'^$', views.FAQListView.as_view(), name='index'),
)
