from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns(
    '',
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sessions/', include('pug_sessions.urls', namespace='sessions')),
    url(r'^slideshows/', include('slideshows.urls'))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
