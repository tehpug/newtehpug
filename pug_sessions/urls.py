from django.conf.urls import patterns, url

from pug_sessions import views

urlpatterns = patterns(
    '',
    url(r'^$', views.SessionIndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.SessionDetailView.as_view(), name='detail'),
    url(r'^places/$', views.PlaceIndexView.as_view(), name='place')
)
