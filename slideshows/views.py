from django.views import generic

from slideshows.models import Slideshow


class IndexView(generic.ListView):
    context_object_name = 'slideshows'

    def get_queryset(self):
        return Slideshow.objects.all().order_by('-created')
