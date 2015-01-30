from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView

from shortlinks.models import Shortlink


class ShortlinkView(RedirectView):
    permanent = True

    def get_redirect_url(self, *args, **kwargs):
        shortlink = get_object_or_404(Shortlink, slug=kwargs['slug'])
        self.url = shortlink.url
        return super(ShortlinkView, self).get_redirect_url(*args, **kwargs)
