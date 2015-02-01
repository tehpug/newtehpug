from django.conf.urls import patterns, url

from media import views

urlpatterns = patterns(
    '',
    url(r'^$', views.MediaListView.as_view(), name='index'),
    url(                        # One view to rule them all
        r'^(?P<type>\w+)/(?P<pk>\w+)$',
        views.MediaDetailView.as_view(),
        name='detail'
    ),
)
