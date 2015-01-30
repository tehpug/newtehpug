from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from shortlinks.views import ShortlinkView


urlpatterns = patterns(
    '',
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sessions/', include('pug_sessions.urls', namespace='sessions')),
    url(r'^slideshows/', include('slideshows.urls')),
    url(r'^projects/', include('projects.urls')),
    url(r'^(?P<slug>\w+)$', ShortlinkView.as_view()),  # This must be last item
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
