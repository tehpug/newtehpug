from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from shortlinks.views import ShortlinkView


urlpatterns = patterns(
    '',
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    url(r'^pug_login/', include(admin.site.urls)),
    url(r'^api/sessions/', include('pug_sessions.urls', namespace='sessions')),
    url(r'^api/slideshows/', include('slideshows.urls')),
    url(r'^api/projects/', include('projects.urls')),
    url(r'^api/media/', include('media.urls')),
    url(r'^api/faq/', include('faq.urls')),
    url(r'^api/members/', include('members.urls')),
    url(r'^(?P<slug>\w+)$', ShortlinkView.as_view()),  # This must be last item
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
